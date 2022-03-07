import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """Init ship and set it position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image and set rect size
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Set ship in screen bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

        # Keep move sign
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置，根据飞船速度"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # 根据 center 对象来更新 rect 的 centerx 的值
        self.rect.centerx = self.center

        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor

        self.rect.bottom = self.bottom


    def blitme(self):
        """Draw ship in right position"""
        self.screen.blit(self.image, self.rect)
