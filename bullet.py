import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Bullet by ship"""
    
    def __init__(self, ai_settings, screen, ship) -> None:
        super().__init__()
        self.screen = screen
        
        # Create a bullet in (0,0) position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        """Update bullet position to top"""
        # 更新表示子弹位置
        self.y -= self.speed_factor
        # 更新子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet in screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
