class settings():
    ''' 这是一个用于设置参数的类'''
    def __init__(self):
        self.width = 1200
        self.height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
