from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import time
import psycopg2

app = FastAPI()

# Database configuration
DB_HOST = 'your_db_host'
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'

# Connect to the database
def create_connection():
    try:
        connection = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        return connection
    except psycopg2.Error as error:
        print("Error connecting to the database: ", error)
        return None

# Pydantic model for Shift
class Shift(BaseModel):
    Name: str
    StartTime: time
    EndTime: time

# Helper function to convert database results to Shift model
def shift_to_model(shift):
    return Shift(**{
        "Name": shift[1],
        "StartTime": shift[2],
        "EndTime": shift[3]
    })

# Endpoint to retrieve all shifts
@app.get('/shifts', response_model=list[Shift])
def get_shifts():
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Shift;")
                shifts = cursor.fetchall()
                return [shift_to_model(shift) for shift in shifts]
        except psycopg2.Error as error:
            print("Error fetching shifts: ", error)
            raise HTTPException(status_code=500, detail="Internal server error")
        finally:
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to create a new shift
@app.post('/shifts', response_model=Shift)
def create_shift(shift: Shift):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO Shift (Name, StartTime, EndTime) VALUES (%s, %s, %s) RETURNING *;",
                               (shift.Name, shift.StartTime, shift.EndTime))
                shift = cursor.fetchone()
                connection.commit()
                return shift_to_model(shift)
        except psycopg2.Error as error:
            print("Error creating shift: ", error)
            connection.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")
        finally:
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to update an existing shift
@app.put('/shifts/{shift_id}', response_model=Shift)
def update_shift(shift_id: int, shift: Shift):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Shift SET Name=%s, StartTime=%s, EndTime=%s WHERE ShiftID=%s RETURNING *;",
                               (shift.Name, shift.StartTime, shift.EndTime, shift_id))
                shift = cursor.fetchone()
                connection.commit()
                if shift:
                    return shift_to_model(shift)
                else:
                    raise HTTPException(status_code=404, detail="Shift not found")
        except psycopg2.Error as error:
            print("Error updating shift: ", error)
            connection.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")
        finally:
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Internal server error")

# Endpoint to delete an existing shift
@app.delete('/shifts/{shift_id}')
def delete_shift(shift_id: int):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Shift WHERE ShiftID=%s;", (shift_id,))
                connection.commit()
                return {"message": "Shift deleted successfully"}
        except psycopg2.Error as error:
            print("Error deleting shift: ", error)
            connection.rollback()
            raise HTTPException(status_code=500, detail="Internal server error")
        finally:
            connection.close()
    else:
        raise HTTPException(status_code=500, detail="Internal server error")
