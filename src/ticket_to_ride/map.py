# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Map machinery to represent game board."""
import typing as tp
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

from .color import Color
from .route import Route


class Map:
    """Representation of a game board."""

    def __init__(self: tp.Self, routes: tp.Iterable[Route]) -> None:
        """Constructor.

        Args:
            routes: Routes to form a map.
        """
        self.graph: nx.Graph = nx.MultiGraph()
        for route in routes:
            route.add_as_edge(self.graph)
        self._check_has_no_bridges()

    def visualize(self: tp.Self) -> None:
        """Visualize self as a graph figure similar to actual game board."""
        plt.figure(figsize=(12, 12))

        # Resolve positions.
        pos = nx.spring_layout(self.graph, seed=42)

        # Draw nodes.
        nx.draw_networkx_nodes(self.graph, pos, node_size=1200, node_color="#FFF", edgecolors="black")
        nx.draw_networkx_labels(
            self.graph,
            pos,
            labels={n: n.name for n in self.graph},
            font_size=7,
            font_family="sans-serif",
            font_weight="bold",
        )

        # Draw edges.
        edges_by_color = self._get_edges_by_color()
        for color, edges in edges_by_color.items():
            nx.draw_networkx_edges(
                self.graph,
                pos,
                edgelist=edges,
                width=2,
                alpha=0.7,
                edge_color=color.value,
                style="dashed",
            )
        edge_labels = nx.get_edge_attributes(self.graph, name="length")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def _get_edges_by_color(self: tp.Self) -> tp.Dict[Color, tp.List[tp.Any]]:
        edges_by_color: tp.Dict[Color, tp.List[tp.Any]] = defaultdict(list)
        for (u, v, ddict) in self.graph.edges(data=True):
            color: Color = ddict["color"]
            edges_by_color[color].append((u, v))  # TODO: persist all edge info?
        return edges_by_color  # TODO: make values tuples for safety?

    def _check_has_no_bridges(self: tp.Self) -> None:
        bridges = frozenset(nx.bridges(self.graph))
        if bridges:
            raise ValueError(f"Cannot initialize a {self.__class__.__name__} with bridges: {bridges}.")
