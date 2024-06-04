# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Ticket machinery to represent destination tickets."""
import typing as tp

from attrs import field, frozen, validators

from .city import City


@frozen
class Ticket:
    """Ticket machinery to represent destination tickets.

    Args:
        origin: Origin city as defined in the ticket.
        destination: Destination city as defined in the ticket.
        face_value: Points value specified on the ticket.
    """
    origin: City
    destination: City
    face_value: int = field(validator=validators.ge(1))

    @property
    def objective_cities(self: tp.Self) -> tp.FrozenSet[City]:
        """Get an unordered pair of cities which a ticket prescribes to connect."""
        return frozenset((self.origin, self.destination))
