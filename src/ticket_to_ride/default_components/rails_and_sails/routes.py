# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Default routes for the worldwide Rails & Sails game version."""
from ticket_to_ride import Color, Route, TransportationType

from .cities import default_cities

default_routes = (
    Route(
        cities=(default_cities["Murmansk"], default_cities["Tiksi"]),
        length=7, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Murmansk"], default_cities["Moskva"]),
        length=2, color=Color.PINK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Moskva"], default_cities["Novosibirsk"]),
        length=4, color=Color.BLUE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Moskva"], default_cities["Novosibirsk"]),
        length=4, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Novosibirsk"], default_cities["Tiksi"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Yakutsk"], default_cities["Tiksi"]),
        length=1, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Yakutsk"], default_cities["Novosibirsk"]),
        length=3, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Novosibirsk"]),
        length=3, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Novosibirsk"]),
        length=3, color=Color.BLACK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Yakutsk"]),
        length=3, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Petropavlovsk"], default_cities["Yakutsk"]),
        length=3, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Petropavlovsk"], default_cities["Tiksi"]),
        length=7, color=Color.BLACK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Petropavlovsk"], default_cities["Tokyo"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Tokyo"], default_cities["Hong Kong"]),
        length=3, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Hong Kong"]),
        length=2, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Hong Kong"]),
        length=2, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Manila"], default_cities["Hong Kong"]),
        length=1, color=Color.PINK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Manila"], default_cities["Tokyo"]),
        length=2, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
)
