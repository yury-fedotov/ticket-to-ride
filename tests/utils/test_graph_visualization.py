# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Tests for graph visualization utilities."""
import typing as tp

import pytest

from ticket_to_ride.utils.graph_visualization import generate_connectionstyle_iterable


@pytest.mark.parametrize(("n_edges", "expected"), (
    (0, frozenset()),
    (1, frozenset(("arc3,rad=0.0",))),
    (2, frozenset(("arc3,rad=0.2", "arc3,rad=-0.2"))),
))
def test_generate_connectionstyle_iterable(n_edges: int, expected: tp.FrozenSet[str]) -> None:
    """Test that connectionstyle iterable is generated correctly."""
    assert generate_connectionstyle_iterable(n_edges) == expected
