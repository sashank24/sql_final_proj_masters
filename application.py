from bottle import route, post, run, template, redirect, request
import database

@route("/")
def get_index():
    return template("index")

@route("/flights")
def get_list():
    items = database.get_flights()
    search_term = request.query.get('search_term', '').strip()
    return template('flights', flights=items, search_term=search_term)

@route("/bookings/<user_id:int>")
def get_bookings(user_id):
    items = database.get_bookings(user_id)
    return template('bookings', user_id=user_id, bookings=items)

@route("/bookings/add", method=['GET', 'POST'])
def post_bookings():
    if request.method == 'POST':
        flight_code = request.forms.get("flight_code")
        user_id = request.forms.get("user_id")
        database.add_booking(user_id, flight_code)
        redirect(f"/bookings/{user_id}")
    else:
        user_id = request.query.get("user_id")
    return template('add_booking.tpl', user_id=user_id)

@route("/flights/add")
def get_add():
    return template("add_flight.tpl")

@post("/flights/add")
def post_add():
    flight_code = request.forms.get("flight_code")
    destination = request.forms.get("destination")
    database.add_flight(flight_code, destination)
    redirect("/flights")

@route("/flights/update/<flight_id:int>")
def get_update(flight_id):
    item = database.get_flight(flight_id)
    return template("update_flight.tpl", flight=item)

@post("/flights/update/<flight_id:int>")
def post_update(flight_id):
    flight_code = request.forms.get("flight_code")
    destination = request.forms.get("destination")
    database.update_flight(flight_id, flight_code, destination)
    redirect("/flights")

@route("/flights/delete/<flight_id:int>")
def get_delete(flight_id):
    database.delete_flight(flight_id)
    redirect("/flights")

run(host='localhost', port=8080)
