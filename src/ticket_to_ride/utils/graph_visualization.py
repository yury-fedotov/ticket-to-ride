# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""Utilities for visualizing graphs."""
import typing as tp


def generate_connectionstyle_iterable(n_edges: int, rad: float = 0.2) -> tp.Tuple[str, ...]:
    """Generate an iterable of strings compatible with `connectionstyle` arg of `nx.draw_networkx_edges()` function.

    Assumes that edges this iterable is generated for connect a pair of neighbor nodes.

    Args:
        n_edges: Number of edges connecting two nodes.
        rad: Curve radius, where 0 is straight connection and 1 is the extreme curvature.

    Returns:
        A tuple of strings compatible with `connectionstyle` argument of `nx.draw_networkx_edges()` function.
    """
    _sign_defining_substrings = frozenset(("", "-"))

    match n_edges:
        case 0:
            return tuple()
        case 1:
            return tuple("arc3,rad=0.0")
        case 2:
            return tuple(f"arc3,rad={sign}{rad}" for sign in _sign_defining_substrings)
        case _:
            raise NotImplementedError(
                f"This machinery is not yet capable of processing > 2 edges. Got {n_edges} as input.",
            )
