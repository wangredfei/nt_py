import sys
import pygame
from Settings import settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    pygame.init()
    # 实例化setting
    ai_setting = settings()
    screen = pygame.display.set_mode((ai_setting.width,ai_setting.height))
    pygame.display.set_caption("Alien Invasion")
    # 实例化飞机
    ship = Ship(ai_setting, screen)

    # 创建一个子弹编组
    bullets = Group()
    # 开始主循环
    while True:

        gf.check_events(ai_setting, screen, ship, bullets)
        ship.updata()
        gf.update_bullets(bullets)
        
        gf.update_screen(screen, ai_setting, ship,bullets)

run_game()