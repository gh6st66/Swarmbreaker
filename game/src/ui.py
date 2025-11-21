import pygame

def draw_ui(screen, player, game_time):
    """
    Draws the user interface elements (HUD) onto the screen.

    Displays health, experience, level, and game time.

    Args:
        screen (pygame.Surface): The main game screen surface.
        player (Player): The player instance to read stats from.
        game_time (float): The current game time in seconds.
    """
    font = pygame.font.Font(None, 36)

    # Health
    health_text = font.render(f"Health: {player.health}/{player.max_health}", True, (255, 255, 255))
    screen.blit(health_text, (10, 10))

    # Experience
    xp_text = font.render(f"XP: {player.experience}/{player.level * 100}", True, (255, 255, 255))
    screen.blit(xp_text, (10, 50))

    # Level
    level_text = font.render(f"Level: {player.level}", True, (255, 255, 255))
    screen.blit(level_text, (10, 90))

    # Timer
    timer_text = font.render(f"Time: {int(game_time)}s", True, (255, 255, 255))
    screen.blit(timer_text, (650, 10))
