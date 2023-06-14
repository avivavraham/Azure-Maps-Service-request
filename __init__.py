import os
import requests
from azure.core.credentials import AzureKeyCredential
from azure.maps.route import MapsRouteClient
# TODO: Put the relevant subscription key below from AzureMap Portal.
AZURE_SUBSCRIPTION_KEY = "z3m2QmnGOqCnBPODEjxdCoiI2XzC-TaRgenvLd6AkzE"

"""
FILE: sample_get_route_range.py
DESCRIPTION:
    This sample demonstrates how to perform get route range with given lat/lon.
USAGE:
    python sample_get_route_range.py

    Set the environment variables with your own values before running the sample:
    - AZURE_SUBSCRIPTION_KEY - your subscription key
"""

subscription_key = os.getenv("AZURE_SUBSCRIPTION_KEY")


def get_route_range():
    # [START get_route_range]
    from azure.core.credentials import AzureKeyCredential
    from azure.maps.route import MapsRouteClient

    # Set the Azure Subscription Key
    os.environ["AZURE_SUBSCRIPTION_KEY"] = AZURE_SUBSCRIPTION_KEY

    # Create the AzureKeyCredential object
    credential = AzureKeyCredential(os.environ["AZURE_SUBSCRIPTION_KEY"])

    # Create an instance of the MapsRouteClient
    maps_route_client = MapsRouteClient(credential=credential)

    result = maps_route_client.get_route_range(coordinates=(52.50931,13.42936), time_budget_in_sec=6000)

    print("Get Route Range with coordinates and time budget:")
    print(result.reachable_range.center)
    print(result.reachable_range.boundary[0])
    # [END get_route_range]

"""
def calculate_shortest_path(addresses):
    # Set the Azure Subscription Key
    os.environ["AZURE_SUBSCRIPTION_KEY"] = AZURE_SUBSCRIPTION_KEY

    # Create the AzureKeyCredential object
    credential = AzureKeyCredential(os.environ["AZURE_SUBSCRIPTION_KEY"])

    # Create an instance of the MapsRouteClient
    route_client = MapsRouteClient(credential=credential)

    # Create a list of waypoints from the addresses
    waypoints = [{"address": address} for address in addresses]

    # Set the route calculation options
    route_request = RouteDirectionsRequest(
        waypoints=waypoints,
        route_mode=RouteMode.fastest,
        optimize=RouteDirectionsRequest.OptimizeOptions.distance,
    )
    # Call the route directions API to get the optimized route
    response = route_client.calculate_directions(route_request)

    if response.error:
        print("Error:", response.error.message)
        return None

    # Extract the route information
    route = response.routes[0]
    optimized_route = route.legs[0].points

    # Extract the coordinates of the optimized route
    coordinates = [(point.latitude, point.longitude) for point in optimized_route]

    return coordinates


# Example usage
addresses_of_dustbins = [
    "Address 1",
    "Address 2",
    "Address 3",
    # Add more addresses here...
]

path = calculate_shortest_path(addresses_of_dustbins)
if path:
    print("Optimized Path:")
    for lat, lon in path:
        print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Failed to calculate the path.")
"""





def calculate_route_directions(origin, destination):
    # Azure Maps Route Directions API endpoint
    endpoint = "https://atlas.microsoft.com/route/directions/json"

    # Azure Maps API key
    api_key = AZURE_SUBSCRIPTION_KEY

    # Query parameters
    params = {
        "api-version": "1.0",
        "query": f"{origin}:{destination}",
        "report": "effectiveSettings",
        "subscription-key": api_key
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

            return coordinates
        else:
            print("No routes found.")
            return None

    except requests.exceptions.HTTPError as error:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Error message: {error}")
        return None

# Example usage
origin = "52.50931,13.42936"
destination = "52.50274,13.43872"

path = calculate_route_directions(origin, destination)
if path:
    print("Optimized Path:")
    for lat, lon in path:
        print(f"Latitude: {lat}, Longitude: {lon}")
else:
    print("Failed to calculate the path.")
