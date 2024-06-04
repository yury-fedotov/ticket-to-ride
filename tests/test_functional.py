# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Tests for functional APIs in the package."""
from ticket_to_ride.default_components import north_america_map
from ticket_to_ride.default_components.north_america.tickets import default_tickets
from ticket_to_ride.functional import evaluate_tickets


def test_evaluate_tickets() -> None:
    """Test that tickets evaluation works as expected."""
    tickets = default_tickets
    board_map = north_america_map
    output = evaluate_tickets(tickets, board_map)
    assert len(output) == len(tickets)
