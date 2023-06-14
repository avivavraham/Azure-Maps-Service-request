import requests
# Put the relevant subscription key below from your AzureMap Service.
AZURE_SUBSCRIPTION_KEY = "z3m2QmnGOqCnBPODEjxdCoiI2XzC-TaRgenvLd6AkzE"


def optimize_route_waypoints(waypoints):
    # Azure Maps Route Directions API endpoint
    global response
    endpoint = "https://atlas.microsoft.com/route/directions/json"

    # Azure Maps API key
    api_key = AZURE_SUBSCRIPTION_KEY

    # Format the query string with waypoints
    query = ":".join(waypoints)

    # Query parameters
    params = {
        "api-version": "1.0",
        "subscription-key": api_key,
        "computeBestOrder": "true",
        "query": query
    }

    try:
        # Make the GET request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()

        # Parse the response JSON
        data = response.json()

        # Check if the response contains routes
        if "routes" in data and len(data["routes"]) > 0:
            route = data["routes"][0]
            points = route["legs"][0]["points"]
            coordinates = [(point["latitude"], point["longitude"]) for point in points]
            # The optimized waypoint order information from the Routing service provides a set of indices.
            # These exclude the origin and the destination indices.
            # so we need to increment these values by 1 to account for the origin.
            optimized_route = [node["optimizedIndex"] + 1 for node in data["optimizedWaypoints"]]
            # here I returned Indices, and ignored the route field in data.
            # If needed, you can return route information from the route field.
            # look for https://learn.microsoft.com/en-us/azure/azure-maps/how-to-use-best-practices-for-routing for
            # additional information.
            return optimized_route
        else:
            print("No routes found.")
            return None

    except requests.exceptions.HTTPError as error:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Error message: {error}")
        return None


# Example usage, Here the first and last are equal to perform a cyclic route.
waypoints = [
    "47.606544,-122.336502",
    "47.759892,-122.204821",
    "47.670682,-122.120415",
    "47.480133,-122.213369",
    "47.615556,-122.193689",
    "47.676508,-122.206054",
    "47.495472,-122.360861",
    "47.606544,-122.336502"
]

# The optimized waypoint order information from the Routing service provides a set of indices.
# These exclude the origin and the destination indices.
# so we need to increment these values by 1 to account for the origin.
path = [0] + optimize_route_waypoints(waypoints) + [0]
print(path)
if path:
    print("Optimized Path:")
    for index in path:
        print(f"Node: {index}, Latitude: {waypoints[index].split(',')[0]}, Longitude: {waypoints[index].split(',')[1]}")
else:
    print("Failed to calculate the path.")
