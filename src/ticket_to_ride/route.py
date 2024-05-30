import networkx

from .color import Color
from .city import City
from pydantic import BaseModel, Field
import typing as tp


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
