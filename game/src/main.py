import pygame
from game.src.constants import SCREEN_WIDTH, SCREEN_HEIGHT
from game.src.player import Player
from game.src.enemy import Enemy
from game.src.experience_orb import ExperienceOrb
from game.src.ui import draw_ui
from game.src.game_state import GameState
from game.src.boss import Boss

def reset_game():
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    experience_orbs = pygame.sprite.Group()

    player = Player(all_sprites, bullets)
    all_sprites.add(player)

    return all_sprites, enemies, bullets, experience_orbs, player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Multiplayer Survivor Game")

    clock = pygame.time.Clock()

    while True:
        all_sprites, enemies, bullets, experience_orbs, player = reset_game()
        game_time = 0

        WAVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(WAVE_EVENT, 5000)
        wave_number = 1

        running = True
        current_state = GameState.START_MENU
        boss_spawned = False
        last_time = pygame.time.get_ticks()

        while running:
            now = pygame.time.get_ticks()
            dt = (now - last_time) / 1000.0
            last_time = now

            if current_state == GameState.GAMEPLAY:
                game_time += dt

            if current_state == GameState.START_MENU:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        current_state = GameState.GAMEPLAY

                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 72)
                text = font.render("Press Enter to Start", True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text, text_rect)
                pygame.display.flip()

            elif current_state == GameState.GAMEPLAY:
                if game_time >= 1200 and not boss_spawned: # 20 minutes
                    pygame.time.set_timer(WAVE_EVENT, 0) # Stop waves
                    boss = Boss(player)
                    all_sprites.add(boss)
                    enemies.add(boss)
                    boss_spawned = True

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == WAVE_EVENT and not boss_spawned:
                        for _ in range(wave_number * 2):
                            enemy = Enemy(player)
                            all_sprites.add(enemy)
                            enemies.add(enemy)
                        wave_number += 1

                all_sprites.update()

                hits = pygame.sprite.spritecollide(player, enemies, False)
                for hit in hits:
                    player.health -= 10
                    if player.health <= 0:
                        current_state = GameState.GAME_OVER
                    if not isinstance(hit, Boss):
                        hit.kill()

                hits = pygame.sprite.groupcollide(enemies, bullets, False, True)
                for hit in hits:
                    if isinstance(hit, Boss):
                        hit.health -= 10
                        if hit.health <= 0:
                            hit.kill()
                            running = False
                    else:
                        hit.kill()
                        orb = ExperienceOrb(hit.rect.centerx, hit.rect.centery)
                        all_sprites.add(orb)
                        experience_orbs.add(orb)

                hits = pygame.sprite.spritecollide(player, experience_orbs, True)
                for hit in hits:
                    player.gain_experience(25)

                screen.fill((0, 0, 0))
                all_sprites.draw(screen)
                draw_ui(screen, player, game_time)
                pygame.display.flip()

            elif current_state == GameState.GAME_OVER:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        running = False

                screen.fill((0, 0, 0))
                font = pygame.font.Font(None, 72)
                text = font.render("Game Over", True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                screen.blit(text, text_rect)

                font = pygame.font.Font(None, 36)
                text = font.render("Press Enter to Restart", True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
                screen.blit(text, text_rect)
                pygame.display.flip()

            clock.tick(60)

if __name__ == "__main__":
    main()
