from .color import Color
from dataclasses import dataclass
import typing as tp


@dataclass
class Route:
    cities: tp.Collection[str, str]
    length: int
    color: Color
