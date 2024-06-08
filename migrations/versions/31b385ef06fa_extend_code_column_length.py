"""extend_code_column_length

Revision ID: 31b385ef06fa
Revises: 3078f1d8a921
Create Date: 2024-05-30 11:30:40.349689

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "31b385ef06fa"
down_revision = "3078f1d8a921"
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("languages", "code", type_=sa.String(10))


def downgrade():
    op.alter_column("languages", "code", type_=sa.String(5))
