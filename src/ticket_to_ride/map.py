from dataclasses import dataclass
import typing as tp
from .route import Route


@dataclass
class Map:
    routes: tp.Collection[Route]
