# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default routes for the Europe game version."""
from ticket_to_ride import Color, Route

from .cities import default_cities

default_routes = (
    Route(cities=(default_cities["Edinburgh"], default_cities["London"]), length=4, color=Color.BLACK),
    Route(cities=(default_cities["Edinburgh"], default_cities["London"]), length=4, color=Color.ORANGE),
    Route(cities=(default_cities["London"], default_cities["Dieppe"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["London"], default_cities["Dieppe"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Dieppe"], default_cities["Brest"]), length=2, color=Color.ORANGE),
    Route(cities=(default_cities["Dieppe"], default_cities["Paris"]), length=1, color=Color.PINK),
    Route(cities=(default_cities["Brest"], default_cities["Pamplona"]), length=4, color=Color.PINK),
    Route(cities=(default_cities["Pamplona"], default_cities["Madrid"]), length=3, color=Color.BLACK),
    Route(cities=(default_cities["Pamplona"], default_cities["Madrid"]), length=3, color=Color.WHITE),
    Route(cities=(default_cities["Madrid"], default_cities["Lisboa"]), length=3, color=Color.PINK),
    Route(cities=(default_cities["Lisboa"], default_cities["Cadiz"]), length=2, color=Color.BLUE),
    Route(cities=(default_cities["Cadiz"], default_cities["Madrid"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Madrid"], default_cities["Barcelona"]), length=2, color=Color.YELLOW),
    Route(cities=(default_cities["Barcelona"], default_cities["Pamplona"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Barcelona"], default_cities["Marseille"]), length=4, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pamplona"], default_cities["Marseille"]), length=4, color=Color.RED),
    Route(cities=(default_cities["Marseille"], default_cities["Paris"]), length=4, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pamplona"], default_cities["Paris"]), length=4, color=Color.BLUE),
    Route(cities=(default_cities["Pamplona"], default_cities["Paris"]), length=4, color=Color.GREEN),
    Route(cities=(default_cities["Brest"], default_cities["Paris"]), length=3, color=Color.BLACK),
    # TODO: complete this list, items above are correct but the list is not finished.
)
