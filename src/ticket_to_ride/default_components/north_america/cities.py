# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default cities for the North America game version."""
from ticket_to_ride import City

_CITY_NAMES = frozenset((
    "Los Angeles",
    "San Francisco",
    "Portland",
    "Seattle",
    "Vancouver",
    "Calgary",
    "Winnipeg",
    "Sault Ste. Marie",
    "Montreal",
    "Boston",
    "New York",
    "Washington",
    "Raleigh",
    "Charleston",
    "Miami",
    "New Orleans",
    "Houston",
    "El Paso",
    "Phoenix",
    "Las Vegas",
    "Salt Lake City",
    "Helena",
    "Duluth",
    "Toronto",
    "Pittsburgh",
    "Nashville",
    "Atlanta",
    "Little Rock",
    "Dallas",
    "Oklahoma City",
    "Santa Fe",
    "Denver",
    "Kansas City",
    "Saint Louis",
    "Omaha",
))

default_cities = {
    name: City(name=name)
    for name in _CITY_NAMES
}
