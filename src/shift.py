# Applying CRUD operations for Shift

from data.create import Shift, engine
from sqlalchemy.orm import Session


def get_session():
    return Session(engine)

# Create function to add a new shift to the database
def create_shift(emp_id, schedule_start_time):
    try:
        with get_session() as session:
            exisiting_shift = session.query(Shift).filter_by(emp_id=emp_id, schedule_start_time=schedule_start_time).first() # Checking if a shift with the same emp_id and schedule_start_time already exists in the database to avoid duplicate shift records for the same employee at the same time
            if exisiting_shift:
                print("A shift with the same employee ID and schedule start time already exists.")
                return
                
            shift = Shift(emp_id=emp_id, schedule_start_time=schedule_start_time)
            session.add(shift)
            session.commit()
            print("Shift created successfully.")
    except Exception as e:
        print(f"Error occurred while creating shift: {e}")

# Read function to retrieve shift details from the database
def read_shifts(shift_id=None, emp_id=None):
    try:
        with get_session() as session:
            if shift_id:
                shift = session.get(Shift, shift_id)
                if shift:
                    print(f"ID: {shift.id}, Employee ID: {shift.emp_id}, Schedule Start Time: {shift.schedule_start_time}")
                else:
                    print(f"Shift with ID {shift_id} not found.")

            elif emp_id:
                shifts = session.query(Shift).filter(Shift.emp_id == emp_id).all()
                if not shifts:
                    print(f"No shifts found for Employee ID {emp_id}.")
                    return
                for shift in shifts:
                    print(f"ID: {shift.id}, Employee ID: {shift.emp_id}, Schedule Start Time: {shift.schedule_start_time}")

            else:
                shifts = session.query(Shift).all()
                if not shifts:
                    print("No shifts found.")
                    return
                for shift in shifts:
                    print(f"ID: {shift.id}, Employee ID: {shift.emp_id}, Schedule Start Time: {shift.schedule_start_time}")

    except Exception as e:
        print(f"Error occurred while reading shifts: {e}")

        
# Update function to modify existing shift details in the database
def update_shift(shift_id, emp_id=None, schedule_start_time=None):
    try:
        with get_session() as session:
            shift = session.get(Shift, shift_id)
            if shift: # Checking if the shift with the provided shift_id exists in the database
                if emp_id is not None:
                    shift.emp_id = emp_id
                if schedule_start_time is not None:
                    shift.schedule_start_time = schedule_start_time
                session.commit()
                print("Shift updated successfully.")
            else:
                print("Shift not found.")
    except Exception as e:
        print(f"Error occurred while updating shift: {e}")

# Delete function to remove a shift from the database
def delete_shift(shift_id):
    try:
        with get_session() as session:
            shift = session.get(Shift, shift_id)
            if shift: # Checking if the shift with the provided shift_id exists in the database
                session.delete(shift)
                session.commit()
                print("Shift deleted successfully.")
            else:
                print("Shift not found.")
    except Exception as e:
        print(f"Error occurred while deleting shift: {e}")
