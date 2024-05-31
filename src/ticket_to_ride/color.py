# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Color machinery to represent key property of routes and cars."""
from enum import Enum


class Color(Enum):
    """Collection of colors used in the game."""
    # Those are specific colors to distinguish cars and routes
    PINK = "#FFC0CB"
    WHITE = "#F9F6EE"
    BLUE = "#0000FF"
    YELLOW = "#FFFF00"
    ORANGE = "#FFA500"
    BLACK = "#000000"
    RED = "#FF0000"
    GREEN = "#008000"
    # Those are system colors to define neutral route and locomotive car
    NEUTRAL = "#808080"
    LOCOMOTIVE = "#CF9FFF"
