# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default cities for the worldwide Rails & Sails game version."""
from ticket_to_ride import City

_CITY_NAMES = frozenset((
    "Reykjavik",
    "Murmansk",
    "Tiksi",
    "Yakustsk",
    "Petropavlovsk",
    "Tokyo",
    "Beijing",
    "Hong Kong",
    "Manila",
    "Honolulu",
    "Bangkok",
    "Mumbai",
    "Labore",
    "Novosibirsk",
    "Moskva",
    "Hamburg",
    "Marseille",
    "Casablanca",
    "Edinburgh",
    "Athina",
    "Al-Zabira",
    "Djubouti",
    "Dar Es Salaam",
    "Toamasina",
    "Cape Town",
    "Luanda",
    "Lagos",
    "North Pole",
    "Tehran",
    "Jakarta",
    "Darwin",
    "Perth",
    "Sydney",
    "Post Moresby",
    "Rio de Janeiro",
    "Buenos Aires",
    "Lima",
    "Valparaiso",
    "Caracas",
    "Miami",
    "Mexico",
    "Los Angeles",
    "New York",
    "Winnipeg",
    "Cambridge Bay",
    "Anchorage",
    "Christchurch",
    "Vancouver",
))

default_cities = {
    name: City(name=name)
    for name in _CITY_NAMES
}
