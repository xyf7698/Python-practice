class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (230,230,200)
        self.ship_speed_factor = 1.5

        """子弹设置"""
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5