# Applying CRUD operations for Employee 

from data.create import Employee, engine
from sqlalchemy.orm import Session



def get_session():
    return Session(engine)

# Create function to add a new employee to the database
def create_employee(first_name, last_name, ssn, address, email, phone_number, position_id, emergency_contact):
    try:
        with get_session() as session:
            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                ssn=ssn,
                address=address,
                email=email,
                phone_number=phone_number,
                position_id=position_id, # Foreign key to link employee to a position in position table
                emergency_contact=emergency_contact
            )
            session.add(employee)
            session.commit()
            print("Employee created successfully.")
    except Exception as e:
        print(f"Error occurred while creating employee: {e}")

# Read function to retrieve employee details from the database
def read_employees(employee_id=None):
    try:
        with get_session() as session:
            if employee_id is not None:
                employee = session.query(Employee).filter_by(id=employee_id).first() # Using filter_by to retrieve employee based on the provided employee_id
                if employee:
                    print(f"ID: {employee.id}, Name: {employee.first_name} {employee.last_name}:\n - Position ID: {employee.position_id}\n - SSN: {employee.ssn}\n - Address: {employee.address}\n - Email: {employee.email}\n - Phone Number: {employee.phone_number}\n - Emergency Contact: {employee.emergency_contact}\n")
                else:
                    print("Employee not found.")
            else:
                employees = session.query(Employee).all()
                for employee in employees:
                    print(f"ID: {employee.id}, Name: {employee.first_name} {employee.last_name}:\n - Position ID: {employee.position_id}\n - SSN: {employee.ssn}\n - Address: {employee.address}\n - Email: {employee.email}\n - Phone Number: {employee.phone_number}\n - Emergency Contact: {employee.emergency_contact}\n")
    except Exception as e:
        print(f"Error occurred while reading employees: {e}")

# Update function to modify existing employee details in the database
def update_employee(employee_id, first_name=None, last_name=None, ssn=None, address=None, email=None, phone_number=None, position_id=None, emergency_contact=None):
    try:
        with get_session() as session:
            employee = session.get(Employee, employee_id)
            if employee:
                if first_name:
                    employee.first_name = first_name
                if last_name:
                    employee.last_name = last_name
                if ssn:
                    employee.ssn = ssn
                if address:
                    employee.address = address
                if email:
                    employee.email = email
                if phone_number:
                    employee.phone_number = phone_number
                if position_id:
                    employee.position_id = position_id
                if emergency_contact:
                    employee.emergency_contact = emergency_contact

                session.commit()
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
    except Exception as e:
        print(f"Error occurred while updating employee: {e}")

# Delete function to remove an employee from the database
def delete_employee(employee_id):
    try:
        with get_session() as session:
            employee = session.get(Employee, employee_id)
            if employee:
                for payroll in employee.payrolls: # Deleting all payroll records associated with the employee before deleting the employee record 
                    session.delete(payroll)
                for timestamp in employee.timestamps: # Deleting all timestamp records associated with the employee before deleting the employee record
                    session.delete(timestamp)
                for shift in employee.shifts: # Deleting all shift records associated with the employee before deleting the employee record
                    session.delete(shift)

                session.delete(employee)
                session.commit()
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")
    except Exception as e: 
        print(f"Error occurred while deleting employee: {e}")
