"""empty message

Revision ID: 79a44c2d1ff8
Revises: 
Create Date: 2020-01-18 16:41:38.210979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79a44c2d1ff8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('survey',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('observation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('survey_id', sa.Integer(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.Column('frequency', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['survey_id'], ['survey.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('observation')
    op.drop_table('survey')
    # ### end Alembic commands ###