"""alert_rules seeder

Revision ID: 8e9314d12ab5
Revises: e6d6a6b04f24
Create Date: 2023-10-18 00:15:39.634548

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e9314d12ab5'
down_revision: Union[str, None] = 'e6d6a6b04f24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'alert_rules',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('name', sa.String),
            sa.Column('threshold_price', sa.Float),
            sa.Column('symbol', sa.String),
            sa.Column('created_at', sa.DateTime(timezone=True)),
            sa.Column('updated_at', sa.DateTime(timezone=True)),
            sa.Column('deleted_at', sa.DateTime(timezone=True))
        ),
        [
            {"id": 1, "name": "Apple", "threshold_price": 100.0, "symbol": "AAPL",
                "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()},
            {"id": 2, "name": "Google", "threshold_price": 700.0, "symbol": "GOOG",
                "created_at": datetime.utcnow(), "updated_at": datetime.utcnow()}
        ]
    )


def downgrade() -> None:
    pass
