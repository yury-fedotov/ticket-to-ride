import typing as tp

import networkx as nx

from .route import Route


class Map(nx.Graph):

    def __init__(self, routes: tp.Iterable[Route]):
        super().__init__()
        for route in routes:
            route.add_as_edge(self)
