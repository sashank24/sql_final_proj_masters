<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Flight</title>
</head>
<body>
    <h1>Add Flight</h1>
    <form action="/flights/add" method="post">
        Flight Code: <input type="text" name="flight_code" required>
        Destination: <input type="text" name="destination" required>
        <input type="submit" value="Add Flight">
    </form>
    <p><a href="/flights">Back to Flights</a></p>
</body>
</html>