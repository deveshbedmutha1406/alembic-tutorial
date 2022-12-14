"""added book table

Revision ID: ab95a2664d58
Revises: 
Create Date: 2022-08-08 19:30:38.545328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab95a2664d58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###

def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###

def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
