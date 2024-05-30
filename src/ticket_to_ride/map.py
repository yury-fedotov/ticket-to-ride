# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Map machinery to represent game board."""
import typing as tp

import networkx as nx

from .route import Route


class Map:
    """Representation of a game board."""

    def __init__(self: tp.Self, routes: tp.Iterable[Route]) -> None:
        """Constructor.

        Args:
            routes: Routes to form a map.
        """
        self.graph: nx.Graph = nx.Graph()
        for route in routes:
            route.add_as_edge(self.graph)
        self._check_has_no_bridges()

    def _check_has_no_bridges(self: tp.Self) -> None:
        bridges = frozenset(nx.bridges(self.graph))
        if bridges:
            raise ValueError(f"Cannot initialize a {self.__class__.__name__} with bridges: {bridges}.")
