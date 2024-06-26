# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Route machinery to represent routes between cities."""
import typing as tp

import networkx as nx
from pydantic import BaseModel, ConfigDict, Field

from .city import City
from .color import Color
from .transportation_type import TransportationType

_ROUTE_POINTS_BY_LENGTH = {
    1: 1,
    2: 2,
    3: 4,
    4: 7,
    5: 10,
    6: 15,
    7: 18,
    8: 21,
}


class Route(BaseModel):
    """Representation of a route between cities."""
    model_config = ConfigDict(validate_default=True)

    cities: tp.Tuple[City, City]
    length: int = Field(ge=1, default=1)
    color: Color = Field(default=Color.NEUTRAL)
    transportation_type: TransportationType = Field(default=TransportationType.TRAIN)

    def __eq__(self: tp.Self, other: tp.Any) -> bool:  # noqa: ANN401
        """Check if two routes are equivalent."""
        if isinstance(other, Route):
            conditions = (
                self.involved_cities == other.involved_cities,
                self.length == other.length,
                self.color == other.color,
                self.transportation_type == other.transportation_type,
            )
            return all(conditions)
        return False

    @property
    def involved_cities(self: tp.Self) -> tp.FrozenSet[City]:
        """Get cities involved in a route.

        TODO: Move to __post_init__ since value in not changed along lifecycle?
        """
        return frozenset(self.cities)

    @property
    def points_value(self: tp.Self) -> float:
        """Get points value of a route."""
        return _ROUTE_POINTS_BY_LENGTH[self.length]

    def add_as_edge(self: tp.Self, graph: nx.Graph) -> None:
        """Add self as an edge on a given graph.

        Args:
            graph: A graph to add self as an edge on.

        Returns:
            None: Modifies the graph passed as an argument in place.
        """
        graph.add_edge(
            *self.cities,
            length=self.length,
            color=self.color,
            transportation_type=self.transportation_type,
            route_object=self,
        )
