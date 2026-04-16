# Employee Clocking System (using SQLAlchemy and Alembic)

A Python-based employee clocking system that manages employee records, shift scheduling, time tracking, and payroll generation. Built using `SQLAlchemy` for Object Relational Mapping and `Alembic` for database migrations, the system provides a menu-driven console interface for performing CRUD operations across five relational database tables.

#### Features
The main features of this program are:
1. Employee Management: Full CRUD operations for managing employee records including personal details, contact information, and position assignments.
2. Position Management: Ability to create, read, update, and delete company positions with associated hourly compensation rates. Positions cannot be deleted while employees are assigned to them.
3. Shift Scheduling: Assign, view, update, and delete employee shifts. Shifts can be looked up by shift ID or by employee ID.
4. Time Clock System: Employees clock in and out using their employee ID. The system automatically determines whether a punch is a check-in or check-out based on the employee's last timestamp for the day. Clock-ins are restricted to a 15-minute window before or after the scheduled shift start time.
5. Payroll Generation: Calculates total hours worked and compensation for each employee within a specified pay period. Supports generating payroll for a single employee or all employees at once. Daily hours are capped at 8 as overtime is not a factor.
6. Database Migrations: Leverages `Alembic` to track schema changes and maintain version control of the database state.
7. Seed Data: Includes a migration script that populates all tables with initial test data for development and testing purposes.
8. Error Handling: Comprehensive try-except blocks and input validation across all operations with clear, user-friendly error messages.

#### How It Works
This program works in the following steps:
1. Database Initialization: Alembic runs the initial migration to create the five database tables (positions, employees, shifts, timestamps, payrolls) with all necessary columns, constraints, and foreign key relationships.
2. Seed Data Population: A subsequent Alembic migration populates the tables with sample data including 3 positions, 5 employees, 8 shifts, 15 timestamp records, and 5 payroll records.
3. Menu-Driven Interface: The user runs `model.py` which presents a main menu with options for Employee, Position, Shift, Timestamp, and Payroll management. Each submenu provides Create, Read, Update, and Delete operations.
4. Clock In/Out Logic: When an employee punches in, the system checks if a shift exists for today, verifies the punch falls within the 15-minute window, and determines the entry type (check-in or check-out) based on the last recorded timestamp for that day.
5. Payroll Calculation: When a pay period is provided, the system pairs check-in and check-out timestamps, calculates the hours worked per day (capped at 8), and multiplies the total hours by the employee's hourly rate from their assigned position.

#### Database Schema
The program uses five tables:
1. `positions` - Stores position names and hourly compensation rates.
2. `employees` - Stores employee personal details with a foreign key to positions.
3. `shifts` - Stores scheduled shift start times with a foreign key to employees.
4. `timestamps` - Stores clock-in and clock-out records with a foreign key to employees.
5. `payrolls` - Stores pay period records with calculated hours and compensation, with a foreign key to employees.

#### How to Run
To run this program, complete the following steps:
1. Ensure you have Python 3.10+ installed on your system (required for match-case syntax).
2. Install the required libraries by running: `pip install sqlalchemy alembic`
3. Ensure your terminal is opened to the root directory containing the `alembic.ini` file.
4. Update the database connection string in `data/create.py` and `alembic.ini` to match your local file path.
5. Run the database migrations to build the schema and populate seed data: `alembic upgrade head`
6. Run the program: `python -m src.model`

#### Notes
A few assumptions were made for this program:
1. The program uses a SQLite database for local development. The database connection string in `data/create.py` and `alembic.ini` must be updated to match the user's local file path.
2. The 15-minute clock-in window is enforced strictly. An employee cannot clock in more than 15 minutes before or after their scheduled shift start time.
3. Overtime is not a factor at the company. Daily hours worked are capped at 8 hours per check-in/check-out pair.
4. The shift end time is always 8 hours after the shift start time and is not stored in the database. It is computed when needed.
5. An employee can only clock in once and clock out once per day. After clocking out, the system rejects further punch attempts for that day.
6. Deleting an employee cascades the deletion to all their associated shifts, timestamps, and payroll records.
7. A position cannot be deleted if employees are currently assigned to it.
