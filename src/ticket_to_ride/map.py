import typing as tp
from .route import Route
import networkx as nx


class Map(nx.Graph):

    def __init__(self, routes: tp.Iterable[Route]):
        super().__init__()
        for route in routes:
            route.add_as_edge(self)
