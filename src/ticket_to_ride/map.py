import typing as tp

import networkx as nx

from .route import Route


class Map(nx.Graph):

    def __init__(self: tp.Self, routes: tp.Iterable[Route]) -> None:
        super().__init__()
        for route in routes:
            route.add_as_edge(self)
