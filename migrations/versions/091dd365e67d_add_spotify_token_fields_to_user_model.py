"""Add Spotify token fields to User model

Revision ID: 091dd365e67d
Revises: 17e2d984cb16
Create Date: 2024-12-12 18:16:11.572224

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '091dd365e67d'
down_revision = '17e2d984cb16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('spotify_refresh_token', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('spotify_access_token', sa.String(length=512), nullable=True))
        batch_op.add_column(sa.Column('spotify_token_expires', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('spotify_token_expires')
        batch_op.drop_column('spotify_access_token')
        batch_op.drop_column('spotify_refresh_token')

    # ### end Alembic commands ###
