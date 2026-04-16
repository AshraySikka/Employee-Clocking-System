from sqlalchemy import create_engine, Column, Integer, ForeignKey, String, DateTime, Float, Date #noqa - added to stop checking for quality assurance
from sqlalchemy.orm import declarative_base, relationship

# Will be changing the database connection based on MariaDB or SQLite3
engine = create_engine(
    'sqlite:////Users/ashraysikka/Desktop/Python/Python Backend/EXSM 3950 - Python II/Assignments/Assignment-6/data/database.db',
    echo = False
    )

Base = declarative_base()

class Position(Base):
    __tablename__ = 'positions'

    id = Column(Integer, primary_key=True)
    position_name = Column(String(200), nullable=False, unique=True) # Nullable: false as the position cannot be empty, unique: true to avoid duplicate positions
    compensation = Column(Float, nullable=False) # Using float as we will be storing decimal values for compensation

    employees = relationship('Employee', back_populates='position')


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    ssn = Column(String(12), nullable=False, unique=True)
    address = Column(String(250), nullable=False)
    email = Column(String, nullable=True)
    phone_number = Column(String(12), nullable=False, unique=True)
    position_id = Column(Integer, ForeignKey('positions.id'), nullable=False)
    emergency_contact = Column(String(255), nullable=False)

    position = relationship('Position', back_populates='employees')
    shifts = relationship('Shift', back_populates='employee')
    timestamps = relationship('Timestamp', back_populates='employee')
    payrolls = relationship('Payroll', back_populates='employee')


class Shift(Base):
    __tablename__ = "shifts"

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    schedule_start_time = Column(DateTime, nullable=False)

    employee = relationship('Employee', back_populates='shifts')

class Timestamp(Base):
    __tablename__ = 'timestamps'

    id = Column(Integer, primary_key=True)
    emp_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    time_stamp = Column(DateTime, nullable=False)
    entry_type = Column(String, nullable=False) # Adding in this column to track if it is a 'check-in' or 'check-out' timestamp

    employee = relationship('Employee', back_populates='timestamps')

class Payroll(Base):
    __tablename__ = 'payrolls'

    id = Column(Integer, primary_key=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    emp_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    total_hours_worked = Column(Float)
    total_compensation = Column(Float)

    employee = relationship('Employee', back_populates='payrolls')



