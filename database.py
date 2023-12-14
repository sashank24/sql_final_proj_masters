import sqlite3
from bottle import route, request, post

connection = sqlite3.connect("flight_management.db")

# Function to retrieve flights
@route('/flights')
def get_flights():
    cursor = connection.cursor()
    search_term = request.query.get('search', '').strip()
    if search_term:
        rows = cursor.execute("SELECT * FROM flights WHERE flight_code LIKE ?", (f"%{search_term}%",))
    else:
        rows = cursor.execute(f"SELECT * FROM flights")
    rows = rows.fetchall()
    rows = [{'flight_id': row[0], 'flight_code': row[1], 'destination': row[2]} for row in rows]
    return rows

# Function to retrieve bookings for a user
@route('/bookings/<user_id:int>')
def get_bookings(user_id):
    cursor = connection.cursor()
    cursor.execute("SELECT flights.flight_id, flights.flight_code FROM flights JOIN bookings ON flights.flight_id = bookings.flight_id WHERE bookings.user_id = ?", (user_id,))
    rows = cursor.fetchall()
    rows = [{'flight_id': row[0], 'flight_code': row[1]} for row in rows]
    return rows

# Function to retrieve flight details by flight ID
@route('/flights/<flight_id:int>')
def get_flight(flight_id):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM flights WHERE flight_id = ?", (flight_id,))
    row = cursor.fetchone()
    flight = {'flight_id': row[0], 'flight_code': row[1], 'destination': row[2]}
    return flight

# Function to add a new flight
@post('/flights/add')
def add_flight(flight_code, destination):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO flights (flight_code, destination) VALUES (?, ?)", (flight_code, destination))
    connection.commit()

# Function to update flight details
@post('/flights/update/<flight_id:int>')
def update_flight(flight_id, flight_code, destination):
    cursor = connection.cursor()
    cursor.execute("UPDATE flights SET flight_code = ?, destination = ? WHERE flight_id = ?", (flight_code, destination, flight_id))
    connection.commit()

# Function to delete a flight
@route('/flights/delete/<flight_id:int>')
def delete_flight(flight_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM flights WHERE flight_id = ?", (flight_id,))
    connection.commit()

# Function to add a booking for a user
@post('/bookings/add')
def add_booking(user_id, flight_code):
    cursor = connection.cursor()
    cursor.execute("SELECT flight_id FROM flights WHERE flight_code = ?", (flight_code,))
    flight_id = cursor.fetchone()[0]
    cursor.execute("INSERT INTO bookings (user_id, flight_id) VALUES (?, ?)", (user_id, flight_id))
    connection.commit()

# Database setup function
def set_up_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS flights")
        cursor.execute("DROP TABLE IF EXISTS bookings")
    except:
        pass

    cursor.execute('''CREATE TABLE flights (flight_id INTEGER PRIMARY KEY AUTOINCREMENT, flight_code TEXT NOT NULL, destination TEXT NOT NULL)''')
    cursor.execute('''CREATE TABLE bookings (booking_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, flight_id INTEGER, 
                      FOREIGN KEY (user_id) REFERENCES users(user_id), FOREIGN KEY (flight_id) REFERENCES flights(flight_id))''')
    connection.commit()

if __name__ == "__main__":
    set_up_database()
