# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default routes for the North America game version."""
from .cities import default_cities
from ticket_to_ride import Route, Color

default_routes = (
    Route(cities=(default_cities["Vancouver"], default_cities["Seattle"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Vancouver"], default_cities["Seattle"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Vancouver"], default_cities["Calgary"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Seattle"], default_cities["Portland"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Seattle"], default_cities["Portland"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Seattle"], default_cities["Helena"]), length=6, color=Color.YELLOW),
    Route(cities=(default_cities["Seattle"], default_cities["Calgary"]), length=4, color=Color.NEUTRAL),
    Route(cities=(default_cities["Portland"], default_cities["San Francisco"]), length=5, color=Color.GREEN),
    Route(cities=(default_cities["Portland"], default_cities["San Francisco"]), length=5, color=Color.PINK),
    Route(cities=(default_cities["Portland"], default_cities["Salt Lake City"]), length=6, color=Color.BLUE),
    Route(cities=(default_cities["San Francisco"], default_cities["Salt Lake City"]), length=5, color=Color.ORANGE),
    Route(cities=(default_cities["San Francisco"], default_cities["Salt Lake City"]), length=5, color=Color.WHITE),
    Route(cities=(default_cities["San Francisco"], default_cities["Los Angeles"]), length=3, color=Color.YELLOW),
    Route(cities=(default_cities["San Francisco"], default_cities["Los Angeles"]), length=3, color=Color.PINK),
    Route(cities=(default_cities["Los Angeles"], default_cities["Las Vegas"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Los Angeles"], default_cities["Phoenix"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Los Angeles"], default_cities["El Paso"]), length=6, color=Color.BLACK),
    Route(cities=(default_cities["Las Vegas"], default_cities["Salt Lake City"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Calgary"], default_cities["Winnipeg"]), length=6, color=Color.WHITE),
    Route(cities=(default_cities["Calgary"], default_cities["Helena"]), length=4, color=Color.NEUTRAL),
    Route(cities=(default_cities["Helena"], default_cities["Winnipeg"]), length=4, color=Color.BLUE),
    Route(cities=(default_cities["Helena"], default_cities["Duluth"]), length=6, color=Color.ORANGE),
    Route(cities=(default_cities["Helena"], default_cities["Omaha"]), length=5, color=Color.RED),
    Route(cities=(default_cities["Helena"], default_cities["Denver"]), length=4, color=Color.GREEN),
    Route(cities=(default_cities["Helena"], default_cities["Salt Lake City"]), length=3, color=Color.PINK),
    Route(cities=(default_cities["Salt Lake City"], default_cities["Denver"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Salt Lake City"], default_cities["Denver"]), length=3, color=Color.RED),
    Route(cities=(default_cities["Salt Lake City"], default_cities["Helena"]), length=3, color=Color.PINK),
    Route(cities=(default_cities["Salt Lake City"], default_cities["Las Vegas"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Denver"], default_cities["Helena"]), length=4, color=Color.GREEN),
    Route(cities=(default_cities["Denver"], default_cities["Salt Lake City"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Denver"], default_cities["Salt Lake City"]), length=3, color=Color.RED),
    Route(cities=(default_cities["Denver"], default_cities["Phoenix"]), length=5, color=Color.WHITE),
    Route(cities=(default_cities["Denver"], default_cities["Santa Fe"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Denver"], default_cities["Oklahoma City"]), length=4, color=Color.RED),
    Route(cities=(default_cities["Denver"], default_cities["Kansas City"]), length=4, color=Color.BLACK),
    Route(cities=(default_cities["Denver"], default_cities["Omaha"]), length=4, color=Color.PINK),
    Route(cities=(default_cities["Phoenix"], default_cities["Denver"]), length=5, color=Color.WHITE),
    Route(cities=(default_cities["Phoenix"], default_cities["Santa Fe"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Phoenix"], default_cities["El Paso"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Santa Fe"], default_cities["El Paso"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Santa Fe"], default_cities["Denver"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Omaha"], default_cities["Helena"]), length=5, color=Color.RED),
    Route(cities=(default_cities["Omaha"], default_cities["Denver"]), length=4, color=Color.PINK),
    Route(cities=(default_cities["Omaha"], default_cities["Kansas City"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Omaha"], default_cities["Chicago"]), length=4, color=Color.BLUE),
    Route(cities=(default_cities["Omaha"], default_cities["Duluth"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Oklahoma City"], default_cities["Denver"]), length=4, color=Color.RED),
    Route(cities=(default_cities["Oklahoma City"], default_cities["Kansas City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Oklahoma City"], default_cities["Little Rock"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Oklahoma City"], default_cities["Dallas"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Oklahoma City"], default_cities["El Paso"]), length=5, color=Color.YELLOW),
    Route(cities=(default_cities["Dallas"], default_cities["Oklahoma City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Dallas"], default_cities["Little Rock"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Dallas"], default_cities["Houston"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Dallas"], default_cities["El Paso"]), length=4, color=Color.RED),
    Route(cities=(default_cities["Houston"], default_cities["Dallas"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Houston"], default_cities["New Orleans"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Houston"], default_cities["El Paso"]), length=6, color=Color.GREEN),
    Route(cities=(default_cities["El Paso"], default_cities["Houston"]), length=6, color=Color.GREEN),
    Route(cities=(default_cities["El Paso"], default_cities["Dallas"]), length=4, color=Color.RED),
    Route(cities=(default_cities["El Paso"], default_cities["Santa Fe"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["El Paso"], default_cities["Phoenix"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["El Paso"], default_cities["Oklahoma City"]), length=5, color=Color.YELLOW),
    Route(cities=(default_cities["New Orleans"], default_cities["Houston"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["New Orleans"], default_cities["Little Rock"]), length=3, color=Color.GREEN),
    Route(cities=(default_cities["New Orleans"], default_cities["Atlanta"]), length=4, color=Color.YELLOW),
    Route(cities=(default_cities["Miami"], default_cities["New Orleans"]), length=6, color=Color.RED),
    Route(cities=(default_cities["Miami"], default_cities["Atlanta"]), length=5, color=Color.BLUE),
    Route(cities=(default_cities["Atlanta"], default_cities["New Orleans"]), length=4, color=Color.YELLOW),
    Route(cities=(default_cities["Atlanta"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Atlanta"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Atlanta"], default_cities["Nashville"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Atlanta"], default_cities["Charleston"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Charleston"], default_cities["Atlanta"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Charleston"], default_cities["Miami"]), length=4, color=Color.PINK),
    Route(cities=(default_cities["Charleston"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Atlanta"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Atlanta"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Charleston"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Nashville"]), length=3, color=Color.BLACK),
    Route(cities=(default_cities["Raleigh"], default_cities["Washington"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Washington"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Raleigh"], default_cities["Pittsburgh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Nashville"], default_cities["Atlanta"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Nashville"], default_cities["Raleigh"]), length=3, color=Color.BLACK),
    Route(cities=(default_cities["Nashville"], default_cities["Pittsburgh"]), length=4, color=Color.YELLOW),
    Route(cities=(default_cities["Nashville"], default_cities["Saint Louis"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Nashville"]), length=4, color=Color.YELLOW),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Washington"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pittsburgh"], default_cities["New York"]), length=2, color=Color.GREEN),
    Route(cities=(default_cities["Pittsburgh"], default_cities["New York"]), length=2, color=Color.WHITE),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Toronto"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Chicago"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Pittsburgh"], default_cities["Saint Louis"]), length=5, color=Color.GREEN),
    Route(cities=(default_cities["Washington"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Washington"], default_cities["Raleigh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Washington"], default_cities["Pittsburgh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Washington"], default_cities["New York"]), length=2, color=Color.ORANGE),
    Route(cities=(default_cities["Washington"], default_cities["New York"]), length=2, color=Color.BLACK),
    Route(cities=(default_cities["New York"], default_cities["Washington"]), length=2, color=Color.ORANGE),
    Route(cities=(default_cities["New York"], default_cities["Washington"]), length=2, color=Color.BLACK),
    Route(cities=(default_cities["New York"], default_cities["Boston"]), length=2, color=Color.YELLOW),
    Route(cities=(default_cities["New York"], default_cities["Boston"]), length=2, color=Color.RED),
    Route(cities=(default_cities["New York"], default_cities["Montreal"]), length=3, color=Color.BLUE),
    Route(cities=(default_cities["New York"], default_cities["Pittsburgh"]), length=2, color=Color.GREEN),
    Route(cities=(default_cities["New York"], default_cities["Pittsburgh"]), length=2, color=Color.WHITE),
    Route(cities=(default_cities["Boston"], default_cities["New York"]), length=2, color=Color.YELLOW),
    Route(cities=(default_cities["Boston"], default_cities["New York"]), length=2, color=Color.RED),
    Route(cities=(default_cities["Boston"], default_cities["Montreal"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Montreal"], default_cities["Boston"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Montreal"], default_cities["New York"]), length=3, color=Color.BLUE),
    Route(cities=(default_cities["Montreal"], default_cities["Toronto"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Montreal"], default_cities["Sault Ste. Marie"]), length=5, color=Color.BLACK),
    Route(cities=(default_cities["Montreal"], default_cities["Sault Ste. Marie"]), length=5, color=Color.NEUTRAL),
    Route(cities=(default_cities["Toronto"], default_cities["Pittsburgh"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Toronto"], default_cities["Duluth"]), length=6, color=Color.PINK),
    Route(cities=(default_cities["Toronto"], default_cities["Chicago"]), length=4, color=Color.WHITE),
    Route(cities=(default_cities["Toronto"], default_cities["Sault Ste. Marie"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Sault Ste. Marie"], default_cities["Toronto"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Sault Ste. Marie"], default_cities["Montreal"]), length=5, color=Color.BLACK),
    Route(cities=(default_cities["Sault Ste. Marie"], default_cities["Montreal"]), length=5, color=Color.NEUTRAL),
    Route(cities=(default_cities["Sault Ste. Marie"], default_cities["Duluth"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Duluth"], default_cities["Toronto"]), length=6, color=Color.PINK),
    Route(cities=(default_cities["Duluth"], default_cities["Chicago"]), length=3, color=Color.RED),
    Route(cities=(default_cities["Duluth"], default_cities["Omaha"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Duluth"], default_cities["Omaha"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Duluth"], default_cities["Helena"]), length=6, color=Color.ORANGE),
    Route(cities=(default_cities["Duluth"], default_cities["Sault Ste. Marie"]), length=3, color=Color.NEUTRAL),
    Route(cities=(default_cities["Chicago"], default_cities["Duluth"]), length=3, color=Color.RED),
    Route(cities=(default_cities["Chicago"], default_cities["Toronto"]), length=4, color=Color.WHITE),
    Route(cities=(default_cities["Chicago"], default_cities["Pittsburgh"]), length=3, color=Color.ORANGE),
    Route(cities=(default_cities["Chicago"], default_cities["Omaha"]), length=4, color=Color.BLUE),
    Route(cities=(default_cities["Chicago"], default_cities["Saint Louis"]), length=2, color=Color.GREEN),
    Route(cities=(default_cities["Chicago"], default_cities["Saint Louis"]), length=2, color=Color.WHITE),
    Route(cities=(default_cities["Saint Louis"], default_cities["Chicago"]), length=2, color=Color.GREEN),
    Route(cities=(default_cities["Saint Louis"], default_cities["Chicago"]), length=2, color=Color.WHITE),
    Route(cities=(default_cities["Saint Louis"], default_cities["Kansas City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Saint Louis"], default_cities["Kansas City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Saint Louis"], default_cities["Little Rock"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Saint Louis"], default_cities["Nashville"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Saint Louis"], default_cities["Pittsburgh"]), length=5, color=Color.GREEN),
    Route(cities=(default_cities["Kansas City"], default_cities["Saint Louis"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Kansas City"], default_cities["Saint Louis"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Kansas City"], default_cities["Denver"]), length=4, color=Color.BLACK),
    Route(cities=(default_cities["Kansas City"], default_cities["Oklahoma City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Kansas City"], default_cities["Omaha"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Kansas City"], default_cities["Omaha"]), length=1, color=Color.NEUTRAL),
    Route(cities=(default_cities["Winnipeg"], default_cities["Duluth"]), length=4, color=Color.BLACK),
    Route(cities=(default_cities["Winnipeg"], default_cities["Sault Ste. Marie"]), length=6, color=Color.NEUTRAL),
    Route(cities=(default_cities["Little Rock"], default_cities["Saint Louis"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Little Rock"], default_cities["Nashville"]), length=3, color=Color.WHITE),
    Route(cities=(default_cities["Little Rock"], default_cities["Oklahoma City"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Little Rock"], default_cities["Dallas"]), length=2, color=Color.NEUTRAL),
    Route(cities=(default_cities["Little Rock"], default_cities["New Orleans"]), length=3, color=Color.GREEN),
)
