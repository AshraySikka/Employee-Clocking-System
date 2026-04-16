from src.employee import create_employee, read_employees, update_employee, delete_employee
from src.position import create_position, read_positions, update_position, delete_position
from src.shift import create_shift, read_shifts, update_shift, delete_shift
from src.timestamp import create_timestamp, read_timestamp, update_timestamp, delete_timestamp
from src.payroll import create_payroll, read_payroll, update_payroll, delete_payroll
from datetime import datetime

def main_menu():
    while True:
        try:
            print("\n===== Employee Clocking System =====")
            print("1. Employee Management")
            print("2. Position Management")
            print("3. Shift Management")
            print("4. Timestamp Management")
            print("5. Payroll Management")
            print("6. Exit")

            try:
                choice = int(input("Select your choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    employee_menu()
                case 2:
                    position_menu()
                case 3:
                    shift_menu()
                case 4:
                    timestamp_menu()
                case 5:
                    payroll_menu()
                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()
                case _:
                    print("Error: Invalid option. Please try again.")
        
        except Exception as e:
            print(f"Error: An unexpected error occured: {e}")


def employee_menu():
    while True:
        try:
            print("\n===== Employee Management =====")
            print("1. Add Employee")
            print("2. View Employee")
            print("3. Update Employee")
            print("4. Delete Employee")
            print("5. Back to Main Menu")
            print("6. Exit the Program")

            try:
                choice = int(input("Select your choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    first_name = input("Enter the employee first name: ").strip()
                    last_name = input("Enter the employee last name: ").strip()
                    
                    print("Available positions:\n") 
                    positions = read_positions(flag=1)
                    
                    for position in positions: # this will give a list of all the available postions
                        print(f"ID: {position.id}, Position Name: {position.position_name}")
                    
                    try:
                        position_id = int(input("Enter position ID:"))
                    except ValueError:
                        raise ValueError("Error: Position ID must be a number.")
                    
                    ssn = input("Enter the employee SSN: ").strip()
                    address = input("Enter the employee address: ").strip()
                    
                    email = input("Enter employee email (press Enter to skip): ").strip()
                    if not email:
                        email = None
                    
                    phone_number = input("Enter the employee's phone number: ").strip()
                    emergency_contact = input("Enter the employee's emergency contact (Format: FULL NAME - PHONE NUMBER): ")

                    create_employee(first_name, last_name, ssn, address, email, phone_number, position_id, emergency_contact)

                case 2:
                    emp_id = input("Enter the employee ID (or press ENTER to view all employees):\n ").strip()
                    if emp_id == '':
                        read_employees()
                    else:
                        try:
                            read_employees(int(emp_id))
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")
                        
                case 3:
                    emp_id = input("Enter the employee ID to update: ").strip()
                    try:
                        emp_id = int(emp_id)
                    except ValueError:
                        raise ValueError("Employee ID must be a valid integer.")
                    
                    print("Press Enter to skip any field you do not wish to update.")
                    
                    first_name = input("Enter new first name: ").strip() or None
                    last_name = input("Enter new last name: ").strip() or None
                    ssn = input("Enter new SSN: ").strip() or None
                    address = input("Enter new address: ").strip() or None
                    email = input("Enter new email: ").strip() or None
                    phone_number = input("Enter new phone number: ").strip() or None
                    position_id = input("Enter new position id: ").strip() or None
                    emergency_contact = input("Enter new emergency contact: ").strip() or None

                    if position_id:
                        try:
                            position_id = int(position_id)
                        except ValueError:
                            raise ValueError("Position ID must be a valid integer.")
                        
                    else:
                        position_id = None

                    update_employee(emp_id, first_name, last_name, ssn, address, email, phone_number, position_id, emergency_contact)

                case 4:
                    emp_id = input("Enter the employee ID to delete: ").strip()
                    try:
                        delete_employee(int(emp_id))
                    except ValueError:
                        raise ValueError("Employee ID must be a valid integer.") 
                    
                case 5:
                    break

                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()

                case _:
                    print("Error: Invalid option. Please enter a valid choice between 1 and 6.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occured in Employee Management: {e}")


def position_menu():
    while True:
        try:
            print("\n===== Position Management =====")
            print("1. Add Position")
            print("2. View Position")
            print("3. Update Position")
            print("4. Delete Position")
            print("5. Back to Main Menu")
            print("6. Exit the Program")

            try:
                choice = int(input("Select you choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    position_name = input("Enter the position name: ").strip().lower()
                    compensation = input("Enter the compensation (per hour): ").strip()
                    
                    try:
                        compensation = float(compensation)
                    except ValueError:
                        raise ValueError("Error: Compensation must be a valid number (e.g. 18.50).")
                    
                    create_position(position_name, compensation)

                case 2:
                    read_positions()
                        
                case 3:
                    position_id = input("Enter position ID to update: ").strip()

                    try:
                        position_id = int(position_id)
                    except ValueError:
                        raise ValueError("Position ID must be a valid integer.")
                    
                    print("Press Enter to skip any field you do not wish to update.")
                    position_name = input("Enter the new Postion name: ").strip() or None
                    compensation = input("Enter the new compensation (per hour): ").strip()

                    if compensation:
                        try:
                            compensation = float(compensation)
                        except ValueError:
                            raise ValueError("Compensation must be a valid number (e.g. 18.50).")
                    else:
                        compensation = None
                        
                    update_position(position_id, position_name, compensation)

                case 4:
                    position_id = input("Enter the position ID to delete: ").strip()
                    try:
                        delete_position(int(position_id))
                    except ValueError:
                        raise ValueError("Position ID must be a valid integer.") 
                    
                case 5:
                    break

                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()

                case _:
                    print("Error: Invalid option. Please enter a valid choice between 1 and 6.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occured in Position Management: {e}")


def shift_menu():
    while True:
        try:
            print("\n===== Shift Management =====")
            print("1. Assign Shift")
            print("2. View Shifts")
            print("3. Update Shift")
            print("4. Delete Shift")
            print("5. Back to Main Menu")
            print("6. Exit the Program")

            try:
                choice = int(input("Select you choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    emp_id = input("Enter employee ID: ").strip()
                    start_time = input("Enter shift start time (YYYY-MM-DD HH:MM): ").strip()
                    
                    try:
                        emp_id = int(emp_id)
                    except ValueError:
                        raise ValueError("Error: Employee ID must be a valid integer.")
                    
                    try:
                        start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
                    except ValueError:
                        raise ValueError("Invalid date. Please use YYYY-MM-DD HH:MM.")
                    
                    create_shift(emp_id, start_time)

                case 2:
                    print("\n1. View all shifts")
                    print("2. Search by shift ID")
                    print("3. Search by employee ID\n")

                    search_choice = input("Select an option: ").strip()

                    if not search_choice.isdigit():
                        raise ValueError("Please enter a valid integer.")

                    match search_choice:
                        case '1':
                            read_shifts()
                        case '2':
                            shift_id = input("Enter shift ID: ").strip()
                            try:
                                read_shifts(shift_id=int(shift_id))
                            except ValueError:
                                raise ValueError("Shift ID must be a valid integer.")
                        case '3':
                            emp_id = input("Enter employee ID: ").strip()
                            try:
                                read_shifts(emp_id=int(emp_id))
                            except ValueError:
                                raise ValueError("Employee ID must be a valid integer.")
                        case _:
                            print("Error: Invalid option.")
                                        
                case 3:
                    shift_id = input("Enter shift ID to update: ").strip()

                    try:
                        shift_id = int(shift_id)
                    except ValueError:
                        raise ValueError("Shift ID must be a valid integer.")
                    
                    print("Press Enter to skip any field you do not wish to update.")
                    emp_id = input("Enter the new Employee ID: ").strip()
                    start_time = input("Enter shift start time (YYYY-MM-DD HH:MM): ").strip()

                    if emp_id:
                        try:
                            emp_id = int(emp_id)
                        except ValueError:
                            raise ValueError("Error: Employee ID must be a valid integer.")
                    else:
                        emp_id = None

                    if start_time:
                        try:
                            start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
                        except ValueError:
                            raise ValueError("Invalid date. Please use YYYY-MM-DD HH:MM.")
                    else:
                        start_time = None
                        
                    update_shift(shift_id, emp_id, start_time)

                case 4:
                    shift_id = input("Enter the shift ID to delete: ").strip()
                    try:
                        delete_shift(int(shift_id))
                    except ValueError:
                        raise ValueError("Shift ID must be a valid integer.") 
                    
                case 5:
                    break

                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()

                case _:
                    print("Error: Invalid option. Please enter a valid choice between 1 and 6.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occured in Shift Management: {e}")



def timestamp_menu():
    while True:
        try:
            print("\n===== Timestamp Management =====")
            print("1. Clock In / Clock Out")
            print("2. View Timestamps")
            print("3. Update Timestamps")
            print("4. Delete Timestamps")
            print("5. Back to Main Menu")
            print("6. Exit the Program")

            try:
                choice = int(input("Select you choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    emp_id = input("Enter employee ID: ").strip()
          
                    try:
                        emp_id = int(emp_id)
                    except ValueError:
                        raise ValueError("Error: Employee ID must be a valid integer.")
                    
                    current_stamp = datetime.now() #taking the current system timestamp
                    create_timestamp(emp_id, current_stamp)

                case 2:
                    emp_id = input("Enter employee ID (press ENTER to view all): ").strip()
                    if emp_id == '':
                        read_timestamp()
                    else:
                        try:
                            read_timestamp(int(emp_id))
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")
                                        
                case 3:
                    stamp_id = input("Enter timestamp ID to update: ").strip()
                    try:
                        stamp_id = int(stamp_id)
                    except ValueError:
                        raise ValueError("Timestamp ID must be a valid integer.")
                    
                    print("Press Enter to skip any field you do not wish to update.")
                    emp_id = input("Enter the new Employee ID: ").strip()
                    new_stamp = input("Enter new timestamp (YYYY-MM-DD HH:MM): ").strip()
                    new_entry_type = input("Enter new entry type (check-in/check-out): ").strip().lower()

                    if emp_id:
                        try:
                            emp_id = int(emp_id)
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")
                    else:
                        emp_id = None

                    if new_stamp:
                        try:
                            new_stamp = datetime.strptime(new_stamp, "%Y-%m-%d %H:%M")
                        except ValueError:
                            raise ValueError("Invalid date. Please use YYYY-MM-DD HH:MM.")
                    else:
                        new_stamp = None

                    if new_entry_type:
                        if new_entry_type not in ['check-in', 'check-out']:
                            raise ValueError("Entry type must be 'check-in' or 'check-out'.")
                    else:
                        new_entry_type = None
                        
                    update_timestamp(stamp_id, emp_id, new_stamp, new_entry_type)

                case 4:
                    stamp_id = input("Enter the Timestamp ID to delete: ").strip()
                    try:
                        delete_timestamp(int(stamp_id))
                    except ValueError:
                        raise ValueError("Timestamp ID must be a valid integer.") 
                    
                case 5:
                    break

                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()

                case _:
                    print("Error: Invalid option. Please enter a valid choice between 1 and 6.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occured in Timestamp Management: {e}")


def payroll_menu():
    while True:
        try:
            print("\n===== Payroll Management =====")
            print("1. Generate Payroll")
            print("2. View Payroll")
            print("3. Update Payroll")
            print("4. Delete Payroll")
            print("5. Back to Main Menu")
            print("6. Exit the Program")

            try:
                choice = int(input("Select you choice: "))
            except ValueError:
                print("Error: Choice must be a number")
                continue

            match choice:
                case 1:
                    try:
                        start_date = input("Enter pay period start date (YYYY-MM-DD): ").strip()
                        end_date = input("Enter pay period end date (YYYY-MM-DD): ").strip()

                        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                    
                    except ValueError:
                        raise ValueError("Invalid date. Please use YYYY-MM-DD.")
                    
                    if start_date >= end_date:
                        raise ValueError("Start date must be before end date.")
                    
                    emp_id = input("Enter employee ID (press ENTER to generate for all employees): ").strip()
                    if emp_id == '':
                        create_payroll(start_date, end_date) # calling it to generate the payroll for all the employees

                    else:
                        try:
                            create_payroll(start_date, end_date, int(emp_id))
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")

                case 2:
                    emp_id = input("Enter employee ID (press ENTER to view all): ").strip()
                    if emp_id == '':
                        read_payroll()
                    else:
                        try:
                            read_payroll(int(emp_id))
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")
                                        
                case 3:
                    payroll_id = input("Enter Payroll ID to update: ").strip()
                    try:
                        payroll_id = int(payroll_id)
                    except ValueError:
                        raise ValueError("Payroll ID must be a valid integer.")
                    
                    print("Press Enter to skip any field you do not wish to update.")
                    start_date = input("Enter the new start date (YYYY-MM-DD): ").strip() or None
                    end_date = input("Enter the new end date (YYYY-MM-DD): ").strip() or None
                    emp_id = input("Enter the new Employee ID: ").strip() or None
                    total_hours = input("Enter new total hours worked: ").strip() or None
                    total_comp = input("Enter new total compensation: ").strip() or None

                    if start_date:
                        try:
                            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Invalid start date. Please use YYYY-MM-DD.")

                    if end_date:
                        try:
                            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
                        except ValueError:
                            raise ValueError("Invalid end date. Please use YYYY-MM-DD.")

                    if emp_id:
                        try:
                            emp_id = int(emp_id)
                        except ValueError:
                            raise ValueError("Employee ID must be a valid integer.")

                    if total_hours:
                        try:
                            total_hours = float(total_hours)
                        except ValueError:
                            raise ValueError("Total hours must be a valid number")

                    if total_comp:
                        try:
                            total_comp = float(total_comp)
                        except ValueError:
                            raise ValueError("Total Compenstaion must be a valid number")
                        
                    update_payroll(payroll_id, start_date, end_date, emp_id, total_hours, total_comp)

                case 4:
                    payroll_id = input("Enter the Payroll ID to delete: ").strip()
                    try:
                        delete_payroll(int(payroll_id))
                    except ValueError:
                        raise ValueError("Payroll ID must be a valid integer.") 
                    
                case 5:
                    break

                case 6:
                    print("Exiting the system. Goodbye!")
                    exit()

                case _:
                    print("Error: Invalid option. Please enter a valid choice between 1 and 6.")

        except ValueError as e:
            print(f"ValueError: {e}")
        except Exception as e:
            print(f"Error: An unexpected error occured in Payroll Management: {e}")   


if __name__ == '__main__':
    main_menu() 