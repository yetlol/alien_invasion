from pydoc import classname


class Settings():
    """ Save alien invasion all settings variable"""

    def __init__(self):
        """Init game settings"""
        # Scree Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed_factor = 2.5
        # Max ship limit
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed_factor = 1
        # 下落的速度
        self.fleet_drop_speed = 10
        # 移动的方向, 1为右移，-1 为左移
        self.fleet_direction = 1