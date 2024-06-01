# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Tests for route machinery."""
import pytest

from ticket_to_ride import City, Route


@pytest.mark.parametrize(("one", "another", "should_be_equal"), (
    (
        Route(cities=(City(name="a"), City(name="b"))),
        Route(cities=(City(name="a"), City(name="b"))),
        True,
    ),
    (
        Route(cities=(City(name="a"), City(name="b"))),
        Route(cities=(City(name="b"), City(name="a"))),
        True,
    ),
    (
        Route(cities=(City(name="a"), City(name="b"))),
        Route(cities=(City(name="a"), City(name="c"))),
        False,
    ),
    (
        Route(cities=(City(name="a"), City(name="b"))),
        Route(cities=(City(name="c"), City(name="d"))),
        False,
    ),
))
def test_equals(one: Route, another: Route, should_be_equal: bool) -> None:
    """Test that routes equality is inferred as expected."""
    evaluated_as_equal = (one == another)
    assert evaluated_as_equal == should_be_equal
