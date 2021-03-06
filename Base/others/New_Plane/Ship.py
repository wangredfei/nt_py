import pygame
import os
class Ship():
    def __init__(self, ai_settings, screen):
        '''初始化飞船并设置起始位置'''
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载飞船图像并获取其外接图形
        self.image = pygame.image.load(os.path.join(r"D:\nt_py\New_Plane\images",'ship.bmp'))
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 设置在中下部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)
        # 添加移动标志
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def updata(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor   
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor   
        self.rect.centerx = self.center