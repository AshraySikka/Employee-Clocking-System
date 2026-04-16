from sqlalchemy.orm import Session
from data.create import Timestamp, Payroll, Employee, engine
from datetime import datetime

def get_session():
    return Session(engine)

# Helper function to calculate total hours worked for an employee within a pay period
def calculate_hours(session, emp_id, start_date, end_date):
    stamps = session.query(Timestamp).filter(
        Timestamp.emp_id == emp_id,
        Timestamp.time_stamp >= datetime.combine(start_date, datetime.min.time()), # from the start of the pay period
        Timestamp.time_stamp <= datetime.combine(end_date, datetime.max.time()) # to the end of the pay period
    ).order_by(Timestamp.time_stamp.asc()).all()

    total_hours = 0.0
    check_in_time = None

    for stamp in stamps:
        if stamp.entry_type == 'check-in':
            check_in_time = stamp.time_stamp
        elif stamp.entry_type == 'check-out' and check_in_time is not None: # only calculate if a check-in exists before this check-out
            time_diff = stamp.time_stamp - check_in_time # difference between check-out and check-in
            daily_hours = time_diff.total_seconds() / 3600 # converting seconds to hours

            if daily_hours > 8: # capping at 8 hours as overtime is not a factor
                print(f"  Note: Employee ID {emp_id} checked in at {check_in_time} and checked out at {stamp.time_stamp} ({round(daily_hours, 2)} hrs). No overtime criteria, capping at 8 hours.")
                daily_hours = 8

            total_hours += daily_hours
            check_in_time = None # resetting for the next pair

    return round(total_hours, 2)


def create_payroll(start_date, end_date, emp_id=None):
    try:
        with get_session() as session:
            if emp_id: # if a specific employee id is provided
                employee = session.get(Employee, emp_id)
                if not employee:
                    print(f"Error: Employee ID {emp_id} does not exist!")
                    return

                # Check if a payroll record already exists for this employee in this pay period
                existing_payroll = session.query(Payroll).filter(
                    Payroll.emp_id == emp_id,
                    Payroll.start_date == start_date,
                    Payroll.end_date == end_date
                ).first()

                if existing_payroll:
                    print(f"Error: Payroll record already exists for Employee ID {emp_id} for this pay period!")
                    return

                total_hours = calculate_hours(session, emp_id, start_date, end_date)
                hourly_rate = employee.position.compensation # getting the hourly rate from the position table
                total_compensation = round(total_hours * hourly_rate, 2)

                new_record = Payroll(
                    start_date = start_date,
                    end_date = end_date,
                    emp_id = emp_id,
                    total_hours_worked = total_hours,
                    total_compensation = total_compensation
                )
                session.add(new_record)
                session.commit()
                session.refresh(new_record)
                print(f"[PAYROLL CREATED] Employee ID: {emp_id} | Hours: {total_hours} | Rate: ${hourly_rate}/hr | Total Pay: ${total_compensation}")

            else: # if no employee id is provided, calculate for all employees
                employees = session.query(Employee).all()
                if not employees:
                    print("Error: No employees found!")
                    return

                for employee in employees:
                    # Check if a payroll record already exists for this employee in this pay period
                    existing_payroll = session.query(Payroll).filter(
                        Payroll.emp_id == employee.id,
                        Payroll.start_date == start_date,
                        Payroll.end_date == end_date
                    ).first()

                    if existing_payroll:
                        print(f"Skipping Employee ID {employee.id}: Payroll record already exists for this pay period.")
                        continue

                    total_hours = calculate_hours(session, employee.id, start_date, end_date)
                    hourly_rate = employee.position.compensation
                    total_compensation = round(total_hours * hourly_rate, 2)

                    new_record = Payroll(
                        start_date = start_date,
                        end_date = end_date,
                        emp_id = employee.id,
                        total_hours_worked = total_hours,
                        total_compensation = total_compensation
                    )
                    session.add(new_record)
                    print(f"[PAYROLL CREATED] Employee ID: {employee.id} | Hours: {total_hours} | Rate: ${hourly_rate}/hr | Total Pay: ${total_compensation}")

                session.commit() # committing all records at once after the loop
    except Exception as e:
        print(f"Error occurred while creating payroll: {e}")


def read_payroll(emp_id=None):
    try:
        with get_session() as session:
            if not emp_id:
                records = session.query(Payroll).all()
                if not records:
                    print("No payroll records found.")
                    return
                print("===All Payroll Records===")

                for record in records:
                    print(f"Payroll ID: {record.id} | Employee ID: {record.emp_id} | Period: {record.start_date} to {record.end_date} | Hours: {record.total_hours_worked} | Pay: ${record.total_compensation}")

            else:
                records = session.query(Payroll).filter(Payroll.emp_id == emp_id).all()
                if not records:
                    print(f"No payroll records found for Employee ID {emp_id}.")
                    return
                print(f"===Payroll Records for Employee ID {emp_id}===")

                for record in records:
                    print(f"Payroll ID: {record.id} | Employee ID: {record.emp_id} | Period: {record.start_date} to {record.end_date} | Hours: {record.total_hours_worked} | Pay: ${record.total_compensation}")
    except Exception as e:
        print(f"Error occurred while reading payroll: {e}")


def update_payroll(payroll_id, start_date=None, end_date=None, emp_id=None, total_hours_worked=None, total_compensation=None):
    try:
        with get_session() as session:
            current_entry = session.get(Payroll, payroll_id)

            if not current_entry:
                print(f"Error: Payroll ID {payroll_id} does not exist!")
                return

            if start_date:
                current_entry.start_date = start_date
            if end_date:
                current_entry.end_date = end_date
            if emp_id:
                current_entry.emp_id = emp_id
            if total_hours_worked:
                current_entry.total_hours_worked = total_hours_worked
            if total_compensation:
                current_entry.total_compensation = total_compensation

            session.commit()
            print(f"[UPDATED RECORD] Payroll ID: {current_entry.id} | Employee ID: {current_entry.emp_id} | Period: {current_entry.start_date} to {current_entry.end_date} | Hours: {current_entry.total_hours_worked} | Pay: ${current_entry.total_compensation}")
    except Exception as e:
        print(f"Error occurred while updating payroll: {e}")


def delete_payroll(payroll_id):
    try:
        with get_session() as session:
            current_entry = session.get(Payroll, payroll_id)

            if not current_entry:
                print(f"Error: Payroll ID {payroll_id} does not exist!")
                return

            session.delete(current_entry)
            session.commit()
            print(f"[DELETED RECORD] Payroll ID: {current_entry.id} | Employee ID: {current_entry.emp_id} | Period: {current_entry.start_date} to {current_entry.end_date} | Hours: {current_entry.total_hours_worked} | Pay: ${current_entry.total_compensation}")
    except Exception as e:
        print(f"Error occurred while deleting payroll: {e}")