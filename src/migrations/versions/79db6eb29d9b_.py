"""empty message

Revision ID: 79db6eb29d9b
Revises: b74c132e4997
Create Date: 2017-03-03 17:33:59.624403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79db6eb29d9b'
down_revision = 'b74c132e4997'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('races',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.Column('running_race_type', sa.Enum('road', 'trail', 'track', 'xc', name='runningracetype'), nullable=True),
    sa.Column('distance', sa.Numeric(precision=3), nullable=True),
    sa.Column('start_date_local', sa.DateTime(), nullable=True),
    sa.Column('city', sa.String(length=256), nullable=True),
    sa.Column('country', sa.String(length=256), nullable=True),
    sa.Column('measurement_preference', sa.Enum('meters', 'feet', name='measurementpreference'), nullable=True),
    sa.Column('url', sa.String(length=256), nullable=True),
    sa.Column('website_url', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('races')
    # ### end Alembic commands ###