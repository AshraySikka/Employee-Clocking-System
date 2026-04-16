"""seed data

Revision ID: 3ac29a31e8b9
Revises: 0244ba2a6aec
Create Date: 2026-03-29 00:54:03.737089

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa #noqa
from data.create import Employee, Position, Shift, Timestamp, Payroll
from datetime import datetime, date

# revision identifiers, used by Alembic.
revision: str = '3ac29a31e8b9'
down_revision: Union[str, Sequence[str], None] = '0244ba2a6aec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    positions_data = [
        {'position_name': 'worker', 'compensation': 15.00},
        {'position_name': 'supervisor', 'compensation': 17.50},
        {'position_name': 'manager', 'compensation': 19.75}
    ]

    employees_data = [
        {'first_name': 'John', 'last_name': 'Doe', 'ssn': '123-45-6789', 'address': '123 Main St', 'email': 'john@example.com', 'phone_number': '111-222-3333', 'position_id': 1, 'emergency_contact': 'Jane Doe - 911-321-6543'},
        {'first_name': 'Alice', 'last_name': 'Smith', 'ssn': '304-54-9876', 'address': '234 Broadway St', 'email': 'alice@example.com', 'phone_number': '444-555-6666', 'position_id': 2, 'emergency_contact': 'Brad Smith - 999-888-7777'},
        {'first_name': 'Alex', 'last_name': 'Brown', 'ssn': '909-42-0089', 'address': '999 Down St', 'email': 'alex@example.com', 'phone_number': '999-000-1155', 'position_id': 3, 'emergency_contact': 'Rick Brown - 0123-456-7891'},
        {'first_name': 'Sarah', 'last_name': 'Johnson', 'ssn': '555-66-7788', 'address': '456 Oak Ave', 'email': None, 'phone_number': '222-333-4444', 'position_id': 1, 'emergency_contact': 'Mike Johnson - 333-444-5555'},
        {'first_name': 'Tom', 'last_name': 'Wilson', 'ssn': '111-22-3344', 'address': '789 Pine Rd', 'email': 'tom@example.com', 'phone_number': '666-777-8888', 'position_id': 1, 'emergency_contact': 'Lisa Wilson - 777-888-9999'}
    ]

    shifts_data = [
        {'emp_id': 1, 'schedule_start_time': datetime(2026, 3, 25, 7, 0, 0)},
        {'emp_id': 1, 'schedule_start_time': datetime(2026, 3, 26, 7, 0, 0)},
        {'emp_id': 2, 'schedule_start_time': datetime(2026, 3, 25, 8, 0, 0)},
        {'emp_id': 2, 'schedule_start_time': datetime(2026, 3, 26, 8, 0, 0)},
        {'emp_id': 3, 'schedule_start_time': datetime(2026, 3, 25, 9, 0, 0)},
        {'emp_id': 4, 'schedule_start_time': datetime(2026, 3, 25, 7, 0, 0)},
        {'emp_id': 5, 'schedule_start_time': datetime(2026, 3, 25, 7, 0, 0)},
        {'emp_id': 5, 'schedule_start_time': datetime(2026, 3, 26, 7, 0, 0)}
    ]

    time_stamps_data = [
        {'emp_id': 1, 'time_stamp': datetime(2026, 3, 25, 6, 50, 0), 'entry_type': 'check-in'},
        {'emp_id': 1, 'time_stamp': datetime(2026, 3, 25, 15, 0, 0), 'entry_type': 'check-out'},
        {'emp_id': 1, 'time_stamp': datetime(2026, 3, 26, 7, 5, 0), 'entry_type': 'check-in'},
        {'emp_id': 1, 'time_stamp': datetime(2026, 3, 26, 15, 2, 0), 'entry_type': 'check-out'},
        {'emp_id': 2, 'time_stamp': datetime(2026, 3, 25, 7, 50, 0), 'entry_type': 'check-in'},
        {'emp_id': 2, 'time_stamp': datetime(2026, 3, 25, 16, 0, 0), 'entry_type': 'check-out'},
        {'emp_id': 2, 'time_stamp': datetime(2026, 3, 26, 8, 10, 0), 'entry_type': 'check-in'},
        {'emp_id': 3, 'time_stamp': datetime(2026, 3, 25, 9, 14, 0), 'entry_type': 'check-in'},
        {'emp_id': 3, 'time_stamp': datetime(2026, 3, 25, 17, 0, 0), 'entry_type': 'check-out'},
        {'emp_id': 4, 'time_stamp': datetime(2026, 3, 25, 6, 55, 0), 'entry_type': 'check-in'},
        {'emp_id': 4, 'time_stamp': datetime(2026, 3, 25, 15, 5, 0), 'entry_type': 'check-out'},
        {'emp_id': 5, 'time_stamp': datetime(2026, 3, 25, 7, 8, 0), 'entry_type': 'check-in'},
        {'emp_id': 5, 'time_stamp': datetime(2026, 3, 25, 15, 0, 0), 'entry_type': 'check-out'},
        {'emp_id': 5, 'time_stamp': datetime(2026, 3, 26, 6, 58, 0), 'entry_type': 'check-in'},
        {'emp_id': 5, 'time_stamp': datetime(2026, 3, 26, 15, 3, 0), 'entry_type': 'check-out'}
    ]

    payrolls_data = [
        {'start_date': date(2026, 3, 1), 'end_date': date(2026, 3, 31), 'emp_id': 1, 'total_hours_worked': 15.95, 'total_compensation': 239.25},
        {'start_date': date(2026, 3, 1), 'end_date': date(2026, 3, 31), 'emp_id': 2, 'total_hours_worked': 8.0, 'total_compensation': 140.00},
        {'start_date': date(2026, 3, 1), 'end_date': date(2026, 3, 31), 'emp_id': 3, 'total_hours_worked': 7.77, 'total_compensation': 153.45},
        {'start_date': date(2026, 3, 1), 'end_date': date(2026, 3, 31), 'emp_id': 4, 'total_hours_worked': 8.0, 'total_compensation': 120.00},
        {'start_date': date(2026, 3, 1), 'end_date': date(2026, 3, 31), 'emp_id': 5, 'total_hours_worked': 15.87, 'total_compensation': 238.05}
    ]

    op.bulk_insert(Position.__table__, positions_data)
    op.bulk_insert(Employee.__table__, employees_data)
    op.bulk_insert(Shift.__table__, shifts_data)
    op.bulk_insert(Timestamp.__table__, time_stamps_data)
    op.bulk_insert(Payroll.__table__, payrolls_data)


def downgrade() -> None:
    op.execute("DELETE FROM payrolls")
    op.execute("DELETE FROM timestamps")
    op.execute("DELETE FROM shifts")
    op.execute("DELETE FROM employees")
    op.execute("DELETE FROM positions")