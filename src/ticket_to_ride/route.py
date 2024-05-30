# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""
Route machinery to represent routes between cities.
"""
import typing as tp

import networkx
from pydantic import BaseModel, ConfigDict, Field

from .city import City
from .color import Color


class Route(BaseModel):
    model_config = ConfigDict(validate_default=True)

    cities: tp.Tuple[City, City]
    length: int = Field(ge=1, default=1)
    color: Color = Field(default=Color.NEUTRAL)

    def add_as_edge(self: tp.Self, graph: networkx.Graph) -> None:
        graph.add_edge(
            self.cities[0],
            self.cities[1],
            length=self.length,
            color=self.color,
        )
