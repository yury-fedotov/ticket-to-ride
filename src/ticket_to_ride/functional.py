# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Functional APIs to work with various machinery across the project."""
import typing as tp

import networkx as nx
import pandas as pd

from ticket_to_ride import Map, Ticket


def evaluate_tickets(tickets: tp.Iterable[Ticket], board_map: Map) -> pd.DataFrame:
    """Evaluate tickets against a board map and get a summary table.

    Args:
        tickets: Tickets to evaluate.
        board_map: A board map to evaluate tickets against.

    Returns:
        A pandas DataFrame with one row representing one ticket and columns storing various statistics.
    """
    tickets = tuple(tickets)
    origins = tuple(ticket.origin.name for ticket in tickets)
    destinations = tuple(ticket.destination.name for ticket in tickets)
    face_value = tuple(ticket.face_value for ticket in tickets)
    shortest_path_length = tuple(
        nx.shortest_path_length(
            G=board_map.graph,
            source=ticket.origin,
            target=ticket.destination,
            weight="length",
        )
        for ticket in tickets
    )
    return pd.DataFrame({
        "origin": origins,
        "destination": destinations,
        "face_value": face_value,
        "shortest_path_length": shortest_path_length,
    })
