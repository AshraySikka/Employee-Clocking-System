# Applying CRUD operations for Position 

from data.create import Position, engine
from sqlalchemy.orm import Session

def get_session():
    return Session(engine)

# Create function to add a new position to the database
def create_position(position_name, compensation): # parameters for creating a new position record in the database
    try:
        position_name = position_name.lower()

        with get_session() as session:
            position = Position(position_name=position_name,compensation=compensation)
            session.add(position)
            session.commit()

            print("Position created successfully.")

    except Exception as e:
        print(f"Error occurred while creating position: {e}")

# Read function to retrieve position details from the database
def read_positions(flag=0):
    try:
        with get_session() as session:
            positions = session.query(Position).all()
            
            if(flag == 1): # will be using this to give the user 'options' of all the positions availabel to choose from
                return positions
            
            for position in positions:
                print(f"ID: {position.id}, Position Name: {position.position_name}, Compensation: {position.compensation}")
    
    except Exception as e:
        print(f"Error occurred while reading positions: {e}")

# Update function to modify existing position details in the database
def update_position(position_id, position_name = None, compensation = None):
    try:
        with get_session() as session:
            position = session.get(Position, position_id)
            if position: # Checking if the position with the provided position_id exists in the database
                if position_name:
                    position.position_name = position_name
                if compensation is not None:
                    position.compensation = compensation
                session.commit()
                print(f"Position with ID {position_id} updated successfully.")
            else:
                print(f"Position with ID {position_id} not found.")
    except Exception as e:
        print(f"Error occurred while updating position: {e}")

# Delete function to remove a position from the database
def delete_position(position_id):
    try:
        with get_session() as session:
            position = session.get(Position, position_id)
            if position:
                if position.employees: # checking if any employees are assigned to this position before deleting
                    print(f"Error: Cannot delete position '{position.position_name}'. There are {len(position.employees)} employee(s) assigned to it.")
                    return
                session.delete(position)
                session.commit()
                print(f"Position with ID {position_id} deleted successfully.")
            else:
                print(f"Position with ID {position_id} not found.")
    except Exception as e:
        print(f"Error occurred while deleting position: {e}")