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
    Route(
        cities=(default_cities["Manila"], default_cities["Bangkok"]),
        length=2, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Manila"], default_cities["Jakarta"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Jakarta"], default_cities["Bangkok"]),
        length=2, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Bangkok"], default_cities["Mumbai"]),
        length=3, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Bangkok"], default_cities["Mumbai"]),
        length=3, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mumbai"], default_cities["Labore"]),
        length=1, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mumbai"], default_cities["Labore"]),
        length=1, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Beijing"], default_cities["Labore"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Novosibirsk"], default_cities["Labore"]),
        length=2, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Labore"], default_cities["Tehran"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mumbai"], default_cities["Tehran"]),
        length=3, color=Color.PINK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mumbai"], default_cities["Tehran"]),
        length=3, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Moskva"], default_cities["Tehran"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Tehran"], default_cities["Athina"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Athina"], default_cities["Hamburg"]),
        length=2, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Athina"], default_cities["Marseille"]),
        length=2, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Moskva"]),
        length=2, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Moskva"]),
        length=2, color=Color.BLACK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Marseille"]),
        length=1, color=Color.PINK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Marseille"]),
        length=1, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Edinburgh"]),
        length=1, color=Color.BLACK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Hamburg"], default_cities["Edinburgh"]),
        length=1, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Marseille"], default_cities["Edinburgh"]),
        length=1, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Marseille"], default_cities["Edinburgh"]),
        length=1, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Reykjavik"], default_cities["Edinburgh"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Reykjavik"], default_cities["Murmansk"]),
        length=4, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Marseille"], default_cities["Casablanca"]),
        length=1, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Casablanca"], default_cities["Lagos"]),
        length=4, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Lagos"], default_cities["Luanda"]),
        length=1, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Lagos"], default_cities["Luanda"]),
        length=1, color=Color.PINK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Luanda"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Toamasina"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Dar Es Salaam"]),
        length=3, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Dar Es Salaam"]),
        length=3, color=Color.BLUE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Toamasina"]),
        length=1, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Jakarta"]),
        length=7, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Jakarta"]),
        length=7, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Luanda"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Djubouti"]),
        length=1, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Djubouti"]),
        length=1, color=Color.BLACK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Dar Es Salaam"], default_cities["Mumbai"]),
        length=4, color=Color.WHITE, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Djubouti"], default_cities["Al-Zabira"]),
        length=2, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Djubouti"], default_cities["Al-Zabira"]),
        length=2, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Al-Zabira"], default_cities["Casablanca"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Al-Zabira"], default_cities["Athina"]),
        length=1, color=Color.BLUE, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Al-Zabira"], default_cities["Tehran"]),
        length=1, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Al-Zabira"], default_cities["Tehran"]),
        length=1, color=Color.BLACK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["North Pole"]),
        length=5, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["North Pole"]),
        length=5, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["North Pole"], default_cities["Perth"]),
        length=5, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["North Pole"], default_cities["Perth"]),
        length=5, color=Color.PINK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Perth"], default_cities["Jakarta"]),
        length=3, color=Color.NEUTRAL, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Perth"], default_cities["Darwin"]),
        length=2, color=Color.BLUE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Jakarta"], default_cities["Darwin"]),
        length=2, color=Color.BLACK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Sydney"], default_cities["Darwin"]),
        length=2, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Sydney"], default_cities["Perth"]),
        length=2, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Sydney"], default_cities["Perth"]),
        length=2, color=Color.WHITE, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Sydney"], default_cities["Post Moresby"]),
        length=3, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Darwin"], default_cities["Post Moresby"]),
        length=1, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Buenos Aires"]),
        length=7, color=Color.BLUE, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Buenos Aires"]),
        length=7, color=Color.YELLOW, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Rio de Janeiro"]),
        length=6, color=Color.BLACK, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Cape Town"], default_cities["Rio de Janeiro"]),
        length=6, color=Color.WHITE, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Buenos Aires"], default_cities["Rio de Janeiro"]),
        length=1, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Buenos Aires"], default_cities["Rio de Janeiro"]),
        length=1, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Luanda"], default_cities["Rio de Janeiro"]),
        length=6, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Mexico"], default_cities["Rio de Janeiro"]),
        length=4, color=Color.GREEN, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mexico"], default_cities["Rio de Janeiro"]),
        length=4, color=Color.BLACK, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mexico"], default_cities["Lagos"]),
        length=7, color=Color.RED, transportation_type=TransportationType.SHIP,
    ),
    Route(
        cities=(default_cities["Mexico"], default_cities["Lima"]),
        length=2, color=Color.YELLOW, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Mexico"], default_cities["Lima"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Lima"], default_cities["Valparaiso"]),
        length=2, color=Color.NEUTRAL, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Lima"], default_cities["Valparaiso"]),
        length=2, color=Color.RED, transportation_type=TransportationType.TRAIN,
    ),
    Route(
        cities=(default_cities["Buenos Aires"], default_cities["Valparaiso"]),
        length=3, color=Color.GREEN, transportation_type=TransportationType.SHIP,
    ),
)
