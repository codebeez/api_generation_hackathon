from flask import Flask, request, jsonify, make_response
from datetime import datetime
import psycopg2
import json

app = Flask(__name__)

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

# Helper function to convert database results to dictionary
def shift_to_dict(shift):
    return {
        "ShiftID": shift[0],
        "Name": shift[1],
        "StartTime": shift[2].strftime('%H:%M:%S'),
        "EndTime": shift[3].strftime('%H:%M:%S'),
        "ModifiedDate": shift[4].strftime('%Y-%m-%d %H:%M:%S')
    }

# Endpoint to retrieve all shifts
@app.route('/shifts', methods=['GET'])
def get_shifts():
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM Shift;")
                shifts = cursor.fetchall()
                shifts_list = [shift_to_dict(shift) for shift in shifts]
                return jsonify(shifts_list)
        except psycopg2.Error as error:
            print("Error fetching shifts: ", error)
            return make_response(jsonify({"error": "Internal server error"}), 500)
        finally:
            connection.close()
    else:
        return make_response(jsonify({"error": "Internal server error"}), 500)

# Endpoint to create a new shift
@app.route('/shifts', methods=['POST'])
def create_shift():
    try:
        shift_data = request.get_json()
        name = shift_data.get('Name')
        start_time = datetime.strptime(shift_data.get('StartTime'), '%H:%M:%S').time()
        end_time = datetime.strptime(shift_data.get('EndTime'), '%H:%M:%S').time()

        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("INSERT INTO Shift (Name, StartTime, EndTime) VALUES (%s, %s, %s) RETURNING *;",
                                   (name, start_time, end_time))
                    shift = cursor.fetchone()
                    connection.commit()
                    return jsonify(shift_to_dict(shift))
            except psycopg2.Error as error:
                print("Error creating shift: ", error)
                connection.rollback()
                return make_response(jsonify({"error": "Internal server error"}), 500)
            finally:
                connection.close()
        else:
            return make_response(jsonify({"error": "Internal server error"}), 500)
    except ValueError:
        return make_response(jsonify({"error": "Invalid time format. Use HH:MM:SS"}), 400)

# Endpoint to update an existing shift
@app.route('/shifts/<int:shift_id>', methods=['PUT'])
def update_shift(shift_id):
    try:
        shift_data = request.get_json()
        name = shift_data.get('Name')
        start_time = datetime.strptime(shift_data.get('StartTime'), '%H:%M:%S').time()
        end_time = datetime.strptime(shift_data.get('EndTime'), '%H:%M:%S').time()

        connection = create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("UPDATE Shift SET Name=%s, StartTime=%s, EndTime=%s WHERE ShiftID=%s RETURNING *;",
                                   (name, start_time, end_time, shift_id))
                    shift = cursor.fetchone()
                    connection.commit()
                    return jsonify(shift_to_dict(shift))
            except psycopg2.Error as error:
                print("Error updating shift: ", error)
                connection.rollback()
                return make_response(jsonify({"error": "Internal server error"}), 500)
            finally:
                connection.close()
        else:
            return make_response(jsonify({"error": "Internal server error"}), 500)
    except ValueError:
        return make_response(jsonify({"error": "Invalid time format. Use HH:MM:SS"}), 400)

# Endpoint to delete an existing shift
@app.route('/shifts/<int:shift_id>', methods=['DELETE'])
def delete_shift(shift_id):
    connection = create_connection()
    if connection:
        try:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM Shift WHERE ShiftID=%s;", (shift_id,))
                connection.commit()
                return jsonify({"message": "Shift deleted successfully"})
        except psycopg2.Error as error:
            print("Error deleting shift: ", error)
            connection.rollback()
            return make_response(jsonify({"error": "Internal server error"}), 500)
        finally:
            connection.close()
    else:
        return make_response(jsonify({"error": "Internal server error"}), 500)

if __name__ == '__main__':
    app.run(debug=True)
