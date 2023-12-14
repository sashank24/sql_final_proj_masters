<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flight Management</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Flight Management</h1>
    <form action="/flights" method="get">
        Search: <input type="text" name="search_term" value="{{ search_term }}">
        <input type="submit" value="Search">
    </form>
    <hr>
    <table>
        <tr>
            <th>ID</th>
            <th>Flight Code</th>
            <th>Destination</th>
            <th>Actions</th>
        </tr>
        % for flight in flights:
        <tr>
            <td>{{ flight['flight_id'] }}</td>
            <td>{{ flight['flight_code'] }}</td>
            <td>{{ flight['destination'] }}</td>
            <td>
                <a href="/bookings/{{ flight['flight_id'] }}">View Bookings</a> |
                <a href="/flights/update/{{ flight['flight_id'] }}">Update</a> |
                <a href="/flights/delete/{{ flight['flight_id'] }}">Delete</a>
            </td>
        </tr>
        % end
    </table>
    <hr>
    <a href="/flights/add">Add New Flight</a>
</body>
</html>
