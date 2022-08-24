"""table1

Revision ID: 11804102699b
Revises: 481b3f69b88f
Create Date: 2022-08-24 08:44:00.447166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11804102699b'
down_revision = '481b3f69b88f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass

def schema_upgrades():
    """schema upgrade migrations go here."""
    pass

def schema_downgrades():
    """schema downgrade migrations go here."""
    pass

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
