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