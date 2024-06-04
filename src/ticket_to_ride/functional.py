import typing as tp

import pandas as pd
import networkx as nx

from ticket_to_ride import Ticket, Map


def evaluate_tickets(tickets: tp.Iterable[Ticket], board_map: Map) -> pd.DataFrame:
    tickets = tuple(tickets)
    origins = tuple(ticket.cities[0].name for ticket in tickets)
    destinations = tuple(ticket.cities[1].name for ticket in tickets)
    card_points = tuple(ticket.value for ticket in tickets)
    shortest_path_length = tuple(
        nx.shortest_path_length(
            G=board_map.graph,
            source=ticket.cities[0],
            target=ticket.cities[1],
            weight="length",
        )
        for ticket in tickets
    )
    return pd.DataFrame({
        "origin": origins,
        "destination": destinations,
        "card_points": card_points,
        "shortest_path_length": shortest_path_length,
    })
