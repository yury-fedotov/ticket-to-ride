# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Map machinery to represent game board."""
import typing as tp
from collections import Counter, defaultdict

import matplotlib.pyplot as plt
import networkx as nx

from .city import City
from .color import Color
from .route import Route
from .utils import generate_connectionstyle_iterable

_TEdgeTupleWithData = tp.Tuple[City, City, tp.Dict[str, tp.Any]]


class Map:
    """Representation of a game board."""

    def __init__(
        self: tp.Self,
        routes: tp.Iterable[Route],
        name: str = "Anonymous",
    ) -> None:
        """Constructor.

        Args:
            name: The name of the map, e.g. "North America".
            routes: Routes to form a map.
        """
        self.name = name
        self.graph: nx.Graph = nx.MultiGraph()
        for route in routes:
            route.add_as_edge(self.graph)
        self._check_is_suitable()

    def __str__(self: tp.Self) -> str:
        """Return readable string representation of self."""
        number_of_cities = self.graph.number_of_nodes()
        number_of_routes = self.graph.number_of_edges()
        return f"{self.name} map with {number_of_cities} cities and {number_of_routes} routes."

    def visualize(self: tp.Self, node_size: int = 1400) -> None:
        """Visualize self as a graph figure similar to actual game board.

        Args:
            node_size: Size of nodes to display.

        Returns:
            None, just plt.show()s the map.
        """
        plt.figure(figsize=(12, 12))

        # Resolve positions.
        pos = nx.spring_layout(self.graph, seed=42)

        # Draw nodes.
        centralities = self.calculate_centrality()
        node_colors = tuple(
            centralities.get(city, 0)
            for city in self.graph
        )
        nx.draw_networkx_nodes(
            self.graph,
            pos,
            node_size=node_size,
            node_color=node_colors,  # type: ignore[arg-type]
            cmap="Reds",
            edgecolors="black",
        )
        nx.draw_networkx_labels(
            self.graph,
            pos,
            labels={n: n.name for n in self.graph},
            font_size=6,
            font_family="sans-serif",
            font_weight="bold",
        )

        # Draw edges.
        for edges_between_pair in self._get_edges_by_neighbor_pair().values():
            nx.draw_networkx_edges(
                self.graph,
                pos,
                edgelist=edges_between_pair,
                width=4,
                alpha=0.7,
                # edge_color, if a sequence, should be a list rather than a tuple due to a bug in nx or plt package
                edge_color=[edge[2]["color"].value for edge in edges_between_pair],  # type: ignore[arg-type]
                # For the style parameter below, note that the sequence of strings should be specifically a list
                # because matplotlib style resolvers treat tuples as numeric parameters for styles.
                style=[edge[2]["transportation_type"].value for edge in edges_between_pair],  # type: ignore[arg-type]
                connectionstyle=generate_connectionstyle_iterable(len(edges_between_pair)),  # type: ignore[arg-type]
                node_size=node_size,
            )

        edge_labels = nx.get_edge_attributes(self.graph, name="length")
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels)

        plt.axis("off")
        plt.tight_layout()
        plt.show()

    def calculate_centrality(self: tp.Self) -> tp.Dict[City, float]:
        """Calculate centrality measure of all involved cities.

        Returns:
            A mapping from cities to their centrality measure, sorted from high to low centrality.
        """
        centrality = nx.betweenness_centrality(self.graph, weight="length")
        return dict(Counter(centrality).most_common())

    def calculate_routes_by_color(self: tp.Self) -> tp.Dict[Color, int]:
        """Calculate the number of routes by color and return as a mapping from color to number of routes."""
        routes_by_color = {color: len(edges) for color, edges in self._get_edges_by_color().items()}
        return dict(Counter(routes_by_color).most_common())

    def calculate_contrast_ratio(self: tp.Self) -> float:
        """Calculate the contrast ratio of a map which is a fraction of neutral-colored routes."""
        neutral_routes = self.calculate_routes_by_color()[Color.NEUTRAL]
        total_routes = self.graph.number_of_edges()
        return 1 - neutral_routes / total_routes

    def _get_edges_by_neighbor_pair(self: tp.Self) -> tp.Dict[tp.FrozenSet[City], tp.List[_TEdgeTupleWithData]]:
        """Get a mapping from neighbor pair to a collection of edges connecting it."""
        edges_by_pair = defaultdict(list)
        for (u, v, ddict) in self.graph.edges(data=True):
            pair = ddict["route_object"].involved_cities
            edges_by_pair[pair].append((u, v, ddict))
        return edges_by_pair

    def _get_routes_count_by_neighbor_pair(self: tp.Self) -> tp.Dict[tp.FrozenSet[City], int]:
        """Get a mapping from neighbor pair to the number of routes connecting them."""
        return {
            pair: len(edges)
            for pair, edges in self._get_edges_by_neighbor_pair().items()
        }

    def _get_edges_by_color(self: tp.Self) -> tp.Dict[Color, tp.List[_TEdgeTupleWithData]]:
        edges_by_color: tp.Dict[Color, tp.List[tp.Any]] = defaultdict(list)
        for (u, v, ddict) in self.graph.edges(data=True):
            color: Color = ddict["color"]
            edges_by_color[color].append((u, v, ddict))
        return edges_by_color  # TODO: make values tuples for safety?

    def _check_is_suitable(self: tp.Self) -> None:
        """Check that self is suitable for the Ticket to Ride game."""
        self._check_has_no_bridges()
        self._check_is_planar()

    def _check_has_no_bridges(self: tp.Self) -> None:
        """Check that the underlying graph has no bridges."""
        bridges = frozenset(nx.bridges(self.graph))
        if bridges:
            raise ValueError(f"Cannot initialize a {self.__class__.__name__} with bridges: {bridges}.")

    def _check_is_planar(self: tp.Self) -> None:
        """Check that the underlying graph is planar."""
        is_planar = nx.is_planar(self.graph)
        if not is_planar:
            raise ValueError(f"Cannot initialize a {self.__class__.__name__} with non-planar graph.")
