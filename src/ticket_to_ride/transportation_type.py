# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Type of route in terms of transportation means."""
from enum import Enum


class TransportationType(Enum):
    """Transportation type such as train, air, ship.

    Values reflect line styles for plotting as graph edges.
    """
    TRAIN = "dashed"
    SHIP = "dashdot"
    AIR = "dotted"
