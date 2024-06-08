# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default destination tickets for the Europe game version."""
from ticket_to_ride import Ticket

from .cities import default_cities

default_tickets = frozenset((
    Ticket(origin=default_cities["Athena"], destination=default_cities["Angora"], face_value=5),
    Ticket(origin=default_cities["Budapest"], destination=default_cities["Sofia"], face_value=5),
    Ticket(origin=default_cities["Frankfurt"], destination=default_cities["København"], face_value=5),
    Ticket(origin=default_cities["Rostov"], destination=default_cities["Erzurum"], face_value=5),
    Ticket(origin=default_cities["Sofia"], destination=default_cities["Smyrna"], face_value=5),
    Ticket(origin=default_cities["Kyiv"], destination=default_cities["Petrograd"], face_value=6),
    Ticket(origin=default_cities["Zurich"], destination=default_cities["Brindisi"], face_value=6),
    Ticket(origin=default_cities["Zurich"], destination=default_cities["Budapest"], face_value=6),
    Ticket(origin=default_cities["Warszawa"], destination=default_cities["Smolensk"], face_value=6),
    Ticket(origin=default_cities["Zagreb"], destination=default_cities["Brindisi"], face_value=6),
    Ticket(origin=default_cities["Paris"], destination=default_cities["Zagreb"], face_value=7),
    Ticket(origin=default_cities["Brest"], destination=default_cities["Marseille"], face_value=7),
    Ticket(origin=default_cities["London"], destination=default_cities["Berlin"], face_value=7),
    Ticket(origin=default_cities["Edinburgh"], destination=default_cities["Paris"], face_value=7),
    Ticket(origin=default_cities["Amsterdam"], destination=default_cities["Pamplona"], face_value=7),
    Ticket(origin=default_cities["Roma"], destination=default_cities["Smyrna"], face_value=8),
    Ticket(origin=default_cities["Palermo"], destination=default_cities["Constantinople"], face_value=8),
    Ticket(origin=default_cities["Saraevo"], destination=default_cities["Sevastopol"], face_value=8),
    Ticket(origin=default_cities["Madrid"], destination=default_cities["Dieppe"], face_value=8),
    Ticket(origin=default_cities["Barcelona"], destination=default_cities["Bruxelles"], face_value=8),
    Ticket(origin=default_cities["Paris"], destination=default_cities["Wien"], face_value=8),
    Ticket(origin=default_cities["Barcelona"], destination=default_cities["Munchen"], face_value=8),
    Ticket(origin=default_cities["Brest"], destination=default_cities["Venezia"], face_value=8),
    Ticket(origin=default_cities["Smolensk"], destination=default_cities["Rostov"], face_value=8),
    Ticket(origin=default_cities["Marseille"], destination=default_cities["Essen"], face_value=8),
    Ticket(origin=default_cities["Kyiv"], destination=default_cities["Sochi"], face_value=8),
    Ticket(origin=default_cities["Madrid"], destination=default_cities["Zurich"], face_value=8),
    Ticket(origin=default_cities["Berlin"], destination=default_cities["Bucharest"], face_value=8),
    Ticket(origin=default_cities["Bruxelles"], destination=default_cities["Danzic"], face_value=9),
    Ticket(origin=default_cities["Berlin"], destination=default_cities["Roma"], face_value=9),
    Ticket(origin=default_cities["Angora"], destination=default_cities["Kharkov"], face_value=10),
    Ticket(origin=default_cities["Riga"], destination=default_cities["Bucharest"], face_value=10),
    Ticket(origin=default_cities["Essen"], destination=default_cities["Kyiv"], face_value=10),
    Ticket(origin=default_cities["Venezia"], destination=default_cities["Constantinople"], face_value=10),
    Ticket(origin=default_cities["London"], destination=default_cities["Wien"], face_value=10),
    Ticket(origin=default_cities["Athena"], destination=default_cities["Wilno"], face_value=11),
    Ticket(origin=default_cities["Stockholm"], destination=default_cities["Wien"], face_value=11),
    Ticket(origin=default_cities["Berlin"], destination=default_cities["Moskva"], face_value=12),
    Ticket(origin=default_cities["Amsterdam"], destination=default_cities["Wilno"], face_value=12),
    Ticket(origin=default_cities["Frankfurt"], destination=default_cities["Smolensk"], face_value=13),
    Ticket(origin=default_cities["Lisboa"], destination=default_cities["Danzic"], face_value=20),
    Ticket(origin=default_cities["Brest"], destination=default_cities["Petrograd"], face_value=20),
    Ticket(origin=default_cities["Palermo"], destination=default_cities["Moskva"], face_value=20),
    Ticket(origin=default_cities["København"], destination=default_cities["Erzurum"], face_value=21),
    Ticket(origin=default_cities["Edinburgh"], destination=default_cities["Athena"], face_value=21),
    Ticket(origin=default_cities["Cadiz"], destination=default_cities["Stockholm"], face_value=21),
))
