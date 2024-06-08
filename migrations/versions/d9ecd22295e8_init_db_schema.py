"""init

Revision ID: d9ecd22295e8
Revises: 
Create Date: 2024-01-10 13:36:20.893094

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d9ecd22295e8"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "categories",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("description", sa.String(255)),
        sa.Column("created_at", sa.DateTime()),
        sa.Column("updated_at", sa.DateTime()),
    )
    op.create_table(
        "tags",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("created_at", sa.DateTime()),
    )
    op.create_table(
        "articles",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("title", sa.String(50), nullable=False),
        sa.Column("content", sa.Text()),
        sa.Column("category_id", sa.Integer(), sa.ForeignKey("categories.id")),
        sa.Column("created_at", sa.DateTime()),
        sa.Column("updated_at", sa.DateTime()),
    )
    op.create_table(
        "article_tags",
        sa.Column(
            "article_id", sa.Integer(), sa.ForeignKey("articles.id"), primary_key=True
        ),
        sa.Column("tag_id", sa.Integer(), sa.ForeignKey("tags.id"), primary_key=True),
        sa.Column("created_at", sa.DateTime()),
    )


def downgrade() -> None:
    op.drop_table("article_tags")
    op.drop_table("articles")
    op.drop_table("tags")
    op.drop_table("categories")
