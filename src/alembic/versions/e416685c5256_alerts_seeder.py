"""alerts seeder

Revision ID: e416685c5256
Revises: 8e9314d12ab5
Create Date: 2023-10-18 00:15:44.949141

"""
from typing import Sequence, Union
from datetime import datetime
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e416685c5256'
down_revision: Union[str, None] = '8e9314d12ab5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            'alerts',
            sa.Column('id', sa.Integer, primary_key=True),
            sa.Column('alert_rule_id', sa.Integer),
            sa.Column('created_at', sa.DateTime(timezone=True)),
            sa.Column('updated_at', sa.DateTime(timezone=True)),
            sa.Column('deleted_at', sa.DateTime(timezone=True))
        ),
        [
            {"id": 1, "alert_rule_id": 1, "created_at": datetime.utcnow(),
             "updated_at": datetime.utcnow()},
            {"id": 2, "alert_rule_id": 2, "created_at": datetime.utcnow(
            ), "updated_at": datetime.utcnow()}
        ]
    )


def downgrade() -> None:
    pass
