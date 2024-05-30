import typing as tp

import networkx
from pydantic import BaseModel, Field

from .city import City
from .color import Color


class Route(BaseModel):
    cities: tp.Tuple[City, City]
    length: int = Field(ge=1)
    color: Color

    def add_as_edge(self, graph: networkx.Graph) -> None:
        graph.add_edge(
            self.cities[0],
            self.cities[1],
            length=self.length,
            color=self.color,
        )
