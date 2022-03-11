from sys import flags
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """An class about alien"""

    def __init__(self, ai_settings, screen):
        """Init alien and set it position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load alien image and set rect
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each alien start position is 0,0
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Save float position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw alien in right postion"""
        self.screen.blit(self.image, self.rect)


    def check_edges(self):
        """如果处于屏幕的边缘，则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    
    def update(self):
        """Move alien position to right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x