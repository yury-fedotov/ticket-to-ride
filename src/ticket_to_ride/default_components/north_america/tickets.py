# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default destination tickets for the North America game version."""
from ticket_to_ride import Ticket

from .cities import default_cities

default_tickets = frozenset((
    Ticket(origin=default_cities["Los Angeles"], destination=default_cities["New York"], face_value=21),
    Ticket(origin=default_cities["Duluth"], destination=default_cities["Houston"], face_value=8),
    Ticket(origin=default_cities["Sault Ste. Marie"], destination=default_cities["Nashville"], face_value=8),
    Ticket(origin=default_cities["New York"], destination=default_cities["Atlanta"], face_value=6),
    Ticket(origin=default_cities["Portland"], destination=default_cities["Nashville"], face_value=17),
    Ticket(origin=default_cities["Vancouver"], destination=default_cities["Montreal"], face_value=20),
    Ticket(origin=default_cities["Duluth"], destination=default_cities["El Paso"], face_value=10),
    Ticket(origin=default_cities["Toronto"], destination=default_cities["Miami"], face_value=10),
    Ticket(origin=default_cities["Portland"], destination=default_cities["Phoenix"], face_value=11),
    Ticket(origin=default_cities["Dallas"], destination=default_cities["New York"], face_value=11),
    Ticket(origin=default_cities["Calgary"], destination=default_cities["Salt Lake City"], face_value=7),
    Ticket(origin=default_cities["Calgary"], destination=default_cities["Phoenix"], face_value=13),
    Ticket(origin=default_cities["Los Angeles"], destination=default_cities["Miami"], face_value=20),
    Ticket(origin=default_cities["Winnipeg"], destination=default_cities["Little Rock"], face_value=11),
    Ticket(origin=default_cities["San Francisco"], destination=default_cities["Atlanta"], face_value=17),
    Ticket(origin=default_cities["Kansas City"], destination=default_cities["Houston"], face_value=5),
    Ticket(origin=default_cities["Los Angeles"], destination=default_cities["Chicago"], face_value=16),
    Ticket(origin=default_cities["Denver"], destination=default_cities["Pittsburgh"], face_value=11),
    Ticket(origin=default_cities["Chicago"], destination=default_cities["Santa Fe"], face_value=9),
    Ticket(origin=default_cities["Vancouver"], destination=default_cities["Santa Fe"], face_value=13),
    Ticket(origin=default_cities["Boston"], destination=default_cities["Miami"], face_value=12),
    Ticket(origin=default_cities["Chicago"], destination=default_cities["New Orleans"], face_value=7),
    Ticket(origin=default_cities["Montreal"], destination=default_cities["Atlanta"], face_value=9),
    Ticket(origin=default_cities["Seattle"], destination=default_cities["New York"], face_value=22),
    Ticket(origin=default_cities["Denver"], destination=default_cities["El Paso"], face_value=4),
    Ticket(origin=default_cities["Helena"], destination=default_cities["Los Angeles"], face_value=8),
    Ticket(origin=default_cities["Winnipeg"], destination=default_cities["Houston"], face_value=12),
    Ticket(origin=default_cities["Montreal"], destination=default_cities["New Orleans"], face_value=13),
    Ticket(origin=default_cities["Sault Ste. Marie"], destination=default_cities["Oklahoma City"], face_value=9),
    Ticket(origin=default_cities["Seattle"], destination=default_cities["Los Angeles"], face_value=9),
))
