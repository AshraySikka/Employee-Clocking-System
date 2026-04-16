"""Initial migration

Revision ID: 0244ba2a6aec
Revises: 
Create Date: 2026-03-29 00:50:02.940447

"""
from typing import Sequence, Union

from alembic import op #noqa
import sqlalchemy as sa #noqa


# revision identifiers, used by Alembic.
revision: str = '0244ba2a6aec'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('positions',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('position_name', sa.String(200), nullable=False, unique=True),
        sa.Column('compensation', sa.Float(), nullable=False)
    )

    op.create_table('employees',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('ssn', sa.String(12), nullable=False, unique=True),
        sa.Column('address', sa.String(250), nullable=False),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone_number', sa.String(12), nullable=False, unique=True),
        sa.Column('position_id', sa.Integer(), sa.ForeignKey('positions.id'), nullable=False),
        sa.Column('emergency_contact', sa.String(255), nullable=False)
    )

    op.create_table('shifts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('emp_id', sa.Integer(), sa.ForeignKey('employees.id'), nullable=False),
        sa.Column('schedule_start_time', sa.DateTime(), nullable=False)
    )

    op.create_table('timestamps',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('emp_id', sa.Integer(), sa.ForeignKey('employees.id'), nullable=False),
        sa.Column('time_stamp', sa.DateTime(), nullable=False),
        sa.Column('entry_type', sa.String(), nullable=False)
    )

    op.create_table('payrolls',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('start_date', sa.Date(), nullable=False),
        sa.Column('end_date', sa.Date(), nullable=False),
        sa.Column('emp_id', sa.Integer(), sa.ForeignKey('employees.id'), nullable=False),
        sa.Column('total_hours_worked', sa.Float(), nullable=True),
        sa.Column('total_compensation', sa.Float(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('payrolls')
    op.drop_table('timestamps')
    op.drop_table('shifts')
    op.drop_table('employees')
    op.drop_table('positions')