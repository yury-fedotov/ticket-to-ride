# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Tests for map machinery."""
import pytest

from ticket_to_ride import City, Map, Route
from ticket_to_ride.default_components.north_america import default_routes


def test_cannot_initialize_with_bridges() -> None:
    """Test that a map cannot be initialized if routes imply bridges."""
    routes_with_implicit_bridge = (
        Route(cities=(City(name="a"), City(name="c"))),
        Route(cities=(City(name="b"), City(name="c"))),
        Route(cities=(City(name="c"), City(name="x"))),
        Route(cities=(City(name="x"), City(name="y"))),
        Route(cities=(City(name="x"), City(name="z"))),
    )
    with pytest.raises(ValueError, match="bridges"):
        Map(routes_with_implicit_bridge)


def test_visualize() -> None:
    """Test that the map visualization API does not fail."""
    game_map = Map(routes=default_routes)
    game_map.visualize()
