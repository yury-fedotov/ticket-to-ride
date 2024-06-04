from ticket_to_ride.functional import evaluate_tickets
from ticket_to_ride.default_components.north_america.tickets import default_tickets
from ticket_to_ride.default_components import north_america_map


def test_evaluate_tickets():
    tickets = default_tickets
    board_map = north_america_map
    output = evaluate_tickets(tickets, board_map)
    assert len(output) == len(tickets)
