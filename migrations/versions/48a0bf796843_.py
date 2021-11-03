"""empty message

Revision ID: 48a0bf796843
Revises: 0a42f504f4b7
Create Date: 2021-11-02 23:44:13.563439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48a0bf796843'
down_revision = '0a42f504f4b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    user_role_table = op.create_table('user_role_tat',
    sa.Column('role_id_tat', sa.Integer(), nullable=False),
    sa.Column('role_tat', sa.String(length=5), nullable=True),
    sa.PrimaryKeyConstraint('role_id_tat')
    )
    op.create_table('user_tat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name_tat', sa.String(length=200), nullable=True),
    sa.Column('user_first_name_tat', sa.String(length=100), nullable=True),
    sa.Column('user_last_name_tat', sa.String(length=100), nullable=True),
    sa.Column('user_email_tat', sa.String(length=200), nullable=True),
    sa.Column('user_password_tat', sa.String(length=200), nullable=True),
    sa.Column('user_role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_role_id'], ['user_role_tat.role_id_tat'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_name_tat')
    )
    # ### end Alembic commands ###
    op.bulk_insert(
        user_role_table, 
        [
            {
                'role_id_tat': 1,
                'role_tat':'ADMIN'
            },
            {
                'role_id_tat': 2,
                'role_tat':'USER'
            }
        ]
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_tat')
    op.drop_table('user_role_tat')
    # ### end Alembic commands ###