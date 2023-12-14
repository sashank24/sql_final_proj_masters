<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Flight</title>
</head>
<body>
    <h1>Update Flight</h1>
    <form action="/flights/update/{{ flight_id }}" method="post">
        <input type="hidden" name="flight_id" value="{{ flight_id }}">
        Flight Code: <input type="text" name="flight_code" value="{{ flight['flight_code'] }}" required>
        Destination: <input type="text" name="destination" value="{{ flight['destination'] }}" required>
        <input type="submit" value="Update Flight">
    </form>
    <p><a href="/flights">Back to Flights</a></p>
</body>
</html>
