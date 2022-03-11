import pygame
from pygame.sprite import Group
from alien_invasion.game_stats import GameStats

from ship import Ship
from alien import Alien
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

    # Create alien group
    # alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create game stats
    stats = GameStats(ai_settings)

    # Start game loop
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, bullets, aliens)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()