"""rename article content column

Revision ID: 578db50ca627
Revises: d9ecd22295e8
Create Date: 2024-01-13 18:41:25.571848

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '578db50ca627'
down_revision: Union[str, None] = 'd9ecd22295e8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('articles', 'content', type_=sa.String(255), new_column_name='content_path')


def downgrade() -> None:
    op.alter_column('articles', 'content_path', type_=sa.Text(), new_column_name='content')


def downgrade() -> None:
    pass
