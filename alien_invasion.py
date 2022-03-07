import pygame
from pygame.sprite import Group

from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    # Init game and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Create a ship
    ship = Ship(ai_settings, screen)

    # Create a group save bullets
    bullets = Group()

    # Start game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()