from enum import Enum

class GameState(Enum):
    """
    Enum representing the possible states of the game.

    Attributes:
        START_MENU (int): Represents the start menu state.
        GAMEPLAY (int): Represents the active gameplay state.
        GAME_OVER (int): Represents the game over state.
    """
    START_MENU = 1
    GAMEPLAY = 2
    GAME_OVER = 3
