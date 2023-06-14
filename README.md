# Azure Maps Route Optimization with Python

This repository contains a Python script that utilizes the Azure Maps Route Directions API to optimize a multi-stop route based on the traveling salesman problem. It calculates the minimum distance route for a given list of waypoints and returns the optimized path for the user to follow.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.8 installed on your machine
- An Azure Maps subscription key (obtainable from the Azure portal)

## Usage

1. Open the main file (`__init__.py`) in a text editor.
2. Assign to the placeholder value `AZURE_SUBSCRIPTION_KEY` variable your actual Azure Maps subscription key.
3. Define your list of waypoints in the `waypoints` variable. Each waypoint should be specified as a string in the format "latitude,longitude".
4. Save the changes to the file.
5. Run the file to obtain the optimized route.

The file will make an HTTP request to the Azure Maps Route Directions API, optimize the route, and return the optimized path with waypoint indices. The optimized path will be printed in the console.

## References

- [Azure Maps Documentation](https://docs.microsoft.com/en-us/azure/azure-maps/)
- [Azure Maps Route Directions API](https://docs.microsoft.com/en-us/azure/azure-maps/route/)
- [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)


