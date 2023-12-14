<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Booking</title>
</head>
<body>
    <h1>Add Booking</h1>
    <form action="/bookings/add" method="post">
        Flight Code: <input type="text" name="flight_code" required>
        <input type="hidden" name="user_id" value="{{ user_id }}">
        <input type="submit" value="Add Booking">
    </form>
    <p><a href="/bookings/{{ user_id }}">Back to Bookings</a></p>
</body>
</html>