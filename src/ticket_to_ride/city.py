# This project is implemented exclusively for learning purposes and assumes no commercial use.
# Neither Yury Fedotov nor organizations he is affiliated with claim any rights to the "Ticket to Ride" trademark,
# game rules or other game-related artifacts. "Ticket to Ride" was designed by Alan R. Moon and released
# by Days of Wonder. To the best of author's knowledge, the trademark is owned by Days of Wonder, Inc.
# All rights to the original game and its elements are owned by their respective holders.
# For more information about the game, please visit
# the official Days of Wonder website: https://www.daysofwonder.com/ticket-to-ride/.
"""City machinery to represent nodes of the board."""
from pydantic import BaseModel, ConfigDict, Field


class City(BaseModel):
    """City machinery to represent nodes of the board."""
    model_config = ConfigDict(frozen=True)

    name: str = Field(min_length=1)
