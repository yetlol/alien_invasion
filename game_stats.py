class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """Init game stats settings"""
        self.ai_settings = ai_settings
        # 游戏刚启动时候处于活动
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit

        