from sqlalchemy.orm import Session
from data.create import Timestamp, Shift, Employee, engine
from datetime import date, timedelta, datetime

def get_session():
    return Session(engine)

def create_timestamp(emp_id, current_stamp):
    try:
        with get_session() as session:
            # Check if the employee exists
            employee = session.get(Employee, emp_id)
            if not employee:
                print(f"Error: Employee ID {emp_id} does not exist!")
                return

            # Will be getting the last timestamp of the employee for today
            last_stamp_today = session.query(Timestamp).filter(
                Timestamp.emp_id == emp_id,
                Timestamp.time_stamp >= datetime.combine(date.today(), datetime.min.time()) # Basically give me todays date and midnight (00:00:00) for comparison
                ).order_by(Timestamp.time_stamp.desc()).first() # ordering by descending to ensure I get the last entry on top and the selecting it by 'first()'

            if last_stamp_today is not None and last_stamp_today.entry_type == 'check-in': # if a 'check-in' stamp already exists
                new_record = Timestamp(emp_id = emp_id, time_stamp = current_stamp, entry_type = 'check-out')
                session.add(new_record)
                session.commit()
                session.refresh(new_record)
                print(f"Check-out time recorded as: {current_stamp} for Employee {emp_id}")

            elif last_stamp_today is not None and last_stamp_today.entry_type == 'check-out':
                print("Error: You have already checked out for today!")
                return
            
            elif last_stamp_today is None:
                existing_shift_records = session.query(Shift).filter(Shift.emp_id == emp_id).all() # will be used to check if the shift of the employee exists today or not + the login time window

                flag = 0
                for shift_record in existing_shift_records:
                    if(shift_record.schedule_start_time.date() == date.today()): # checking for today's scheduled shift
                        flag = 3
                        accepted_start_time = shift_record.schedule_start_time - timedelta(minutes = 15) #subtracting 15 minsutes from the scheduled time
                        accepted_end_time = shift_record.schedule_start_time + timedelta(minutes = 15) #adding 15 minsutes to the scheduled time
                        break

                if flag == 3:
                    if(current_stamp < accepted_start_time):
                        print(f"Error: Check-in not recorded. The shift start time is {accepted_start_time + timedelta(minutes = 15)}")
                    elif(current_stamp > accepted_end_time):
                        print(f"Error: Check-in not recorded. The shift start time was {accepted_start_time + timedelta(minutes = 15)}")
                    else:
                        new_record = Timestamp(emp_id = emp_id, time_stamp = current_stamp, entry_type = 'check-in')
                        session.add(new_record)
                        session.commit()
                        session.refresh(new_record)
                        print(f"Check-in time recorded as: {current_stamp} for Employee {emp_id}")
                
                else:
                    print("Error: You are not scheduled for today!")
                    return
            
            else:
                print("Error encountered while recording the time, please try again!")
    except Exception as e:
        print(f"Error occurred while creating timestamp: {e}")

def read_timestamp(emp_id=None):
    try:
        with get_session() as session:
            if not emp_id:
                stamps = session.query(Timestamp).all()
                if not stamps:
                    print("No timestamps found.")
                    return
                print("===All the Timestamps===")
                
                for stamp in stamps:
                    print(f"Stamp ID: {stamp.id} | Employee ID: {stamp.emp_id} | Time: {stamp.time_stamp} | Type: {stamp.entry_type}")

            else:
                stamps = session.query(Timestamp).filter(Timestamp.emp_id == emp_id).all()
                if not stamps:
                    print(f"No timestamps found for Employee ID {emp_id}.")
                    return
                print(f"===All the Timestamps for Employee ID {emp_id}===")
                
                for stamp in stamps:
                    print(f"Stamp ID: {stamp.id} | Employee ID: {stamp.emp_id} | Time: {stamp.time_stamp} | Type: {stamp.entry_type}")
    except Exception as e:
        print(f"Error occurred while reading timestamps: {e}")


def update_timestamp(stamp_id, emp_id=None, new_stamp=None, new_entry_type=None):
    try:
        with get_session() as session:
            current_entry = session.get(Timestamp, stamp_id)

            if not current_entry:
                print(f"Error: Timestamp id: {stamp_id} does not exist!")
                return
            
            if emp_id:
                current_entry.emp_id = emp_id
            if new_stamp:
                current_entry.time_stamp = new_stamp
            if new_entry_type:
                current_entry.entry_type = new_entry_type

            session.commit()
            print(f"[UPDATED RECORD] Stamp ID: {current_entry.id} | Employee ID: {current_entry.emp_id} | Time: {current_entry.time_stamp} | Type: {current_entry.entry_type}")
    except Exception as e:
        print(f"Error occurred while updating timestamp: {e}")


def delete_timestamp(stamp_id):
    try:
        with get_session() as session:
            current_entry = session.get(Timestamp, stamp_id)

            if not current_entry:
                print(f"Error: Timestamp id: {stamp_id} does not exist!")
                return

            session.delete(current_entry)
            session.commit()
            print(f"[DELETED RECORD] Stamp ID: {current_entry.id} | Employee ID: {current_entry.emp_id} | Time: {current_entry.time_stamp} | Type: {current_entry.entry_type}")
    except Exception as e:
        print(f"Error occurred while deleting timestamp: {e}")