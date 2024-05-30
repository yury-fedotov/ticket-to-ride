# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default destination tickets for the North America game version."""
from .cities import default_cities
from ticket_to_ride import Ticket

default_tickets = frozenset((
    Ticket(cities=(default_cities["Los Angeles"], default_cities["New York"]), value=21),
    Ticket(cities=(default_cities["Duluth"], default_cities["Houston"]), value=8),
    Ticket(cities=(default_cities["Sault Ste. Marie"], default_cities["Nashville"]), value=8),
    Ticket(cities=(default_cities["New York"], default_cities["Atlanta"]), value=6),
    Ticket(cities=(default_cities["Portland"], default_cities["Nashville"]), value=17),
    Ticket(cities=(default_cities["Vancouver"], default_cities["Montreal"]), value=20),
    Ticket(cities=(default_cities["Duluth"], default_cities["El Paso"]), value=10),
    Ticket(cities=(default_cities["Toronto"], default_cities["Miami"]), value=10),
    Ticket(cities=(default_cities["Portland"], default_cities["Phoenix"]), value=11),
    Ticket(cities=(default_cities["Dallas"], default_cities["New York"]), value=11),
    Ticket(cities=(default_cities["Calgary"], default_cities["Salt Lake City"]), value=7),
    Ticket(cities=(default_cities["Calgary"], default_cities["Phoenix"]), value=13),
    Ticket(cities=(default_cities["Los Angeles"], default_cities["Miami"]), value=20),
    Ticket(cities=(default_cities["Winnipeg"], default_cities["Little Rock"]), value=11),
    Ticket(cities=(default_cities["San Francisco"], default_cities["Atlanta"]), value=17),
    Ticket(cities=(default_cities["Kansas City"], default_cities["Houston"]), value=5),
    Ticket(cities=(default_cities["Los Angeles"], default_cities["Chicago"]), value=16),
    Ticket(cities=(default_cities["Denver"], default_cities["Pittsburgh"]), value=11),
    Ticket(cities=(default_cities["Chicago"], default_cities["Santa Fe"]), value=9),
    Ticket(cities=(default_cities["Vancouver"], default_cities["Santa Fe"]), value=13),
    Ticket(cities=(default_cities["Boston"], default_cities["Miami"]), value=12),
    Ticket(cities=(default_cities["Chicago"], default_cities["New Orleans"]), value=7),
    Ticket(cities=(default_cities["Montreal"], default_cities["Atlanta"]), value=9),
    Ticket(cities=(default_cities["Seattle"], default_cities["New York"]), value=22),
    Ticket(cities=(default_cities["Denver"], default_cities["El Paso"]), value=4),
    Ticket(cities=(default_cities["Helena"], default_cities["Los Angeles"]), value=8),
    Ticket(cities=(default_cities["Winnipeg"], default_cities["Houston"]), value=12),
    Ticket(cities=(default_cities["Montreal"], default_cities["New Orleans"]), value=13),
    Ticket(cities=(default_cities["Sault Ste. Marie"], default_cities["Oklahoma City"]), value=9),
    Ticket(cities=(default_cities["Seattle"], default_cities["Los Angeles"]), value=9),
))
