"""add_translations

Revision ID: 3078f1d8a921
Revises: 578db50ca627
Create Date: 2024-04-16 20:00:49.003299

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3078f1d8a921'
down_revision: Union[str, None] = '578db50ca627'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'languages',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('name', sa.String(25), nullable=False),
        sa.Column('code', sa.String(5), nullable=False),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )

    op.create_table(
        'translations',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('content_path', sa.String(255)),
        sa.Column('language_id', sa.Integer(), sa.ForeignKey('languages.id')),
        sa.Column('article_id', sa.Integer(), sa.ForeignKey('articles.id')),
        sa.Column('is_ready', sa.Boolean(), default=False),
        sa.Column('created_at', sa.DateTime()),
        sa.Column('updated_at', sa.DateTime()),
    )


def downgrade():
    op.drop_table('translations')
    op.drop_table('languages')
