import pygame 
import os
import sys, random, time
from pygame.locals import *


class BasePlane():
    '''飞机的基类'''
    def __init__(self, screen_temp, x, y, image_name,image_list):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image_name = image_name
        self.list = image_list
        self.image = pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji",self.image_name))
        # 定义一个列表用于存储子弹
        self.bullet_list = []
        self.hit = False
        self.image_num = 0
        self.image_index = 0
    def display(self ):
        if self.hit == True:
            self.screen.blit(self.list[self.image_index],(self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                time.sleep(1)
                sys.exit()
        else:
            self.screen.blit(self.image, (self.x, self.y))
        # 判断字段越界的问题
        b = []
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.y < 0:
                b.append(bullet)
        for i in b:
            self.bullet_list.remove(i)
    def plane_over(self):
        self.hit = True

class HeroPlane(BasePlane):
    '''这是一个自己飞机的类'''
    def __init__(self, screen_temp):
        image_list_hero = [
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","hero_blowup_n1.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","hero_blowup_n2.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","hero_blowup_n3.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","hero_blowup_n4.png")),
                            ]
        BasePlane.__init__(self, screen_temp, 190, 700,"hero1.png" ,image_list_hero)
        
 
    def move_left(self):
        self.x -= 10
        # if self.x < 0:
    def move_right(self):
        self.x += 10

    def move_up(self): 
        self.y -= 10

    def move_down(self):
        self.y += 10
    # 将子弹存入列表
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x, self.y))


class Enemy1(BasePlane):
    '''这是敌机的类'''
    def __init__(self, screen_temp):
        self.x = random.randrange(1,480,30)
        self.y = 0
        image_list_enemy = [
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","enemy0_down1.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","enemy0_down2.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","enemy0_down3.png")),
                            pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","enemy0_down4.png")),
        ]
        BasePlane.__init__(self, screen_temp,self.x , self.y,"enemy-1.gif",image_list_enemy )
        self.direction = "right"


    # 用于敌机移动
    def move(self):

        if self.direction == "right":
            self.x += 1
        elif self.direction == "left": 
            self.x -= 1
        if self.x >= 200:
            self.direction = "left"
        elif self.x < 0 :
            self.direction = "right"
        # 控制敌机下降的速度
        self.y += 0.8

    def fire(self):
        random_num = random.randrange(100)
        if  random_num == 8 or random_num == 20:

            self.bullet_list.append(Bullet2(self.screen,self.x, self.y))
    

class Base_Bullet():
    def __init__(self, screen_temp, x, y, image_name):
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji",image_name))
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))


class Bullet(Base_Bullet):  
    '''这是母机子弹的类'''
    def __init__(self,screen_temp, x, y):
       Base_Bullet.__init__(self, screen_temp, x+40, y-20, "bullet-3.gif")
    
    def move(self):
        self.y -= 10


class Bullet2(Base_Bullet): 

    def __init__(self,screen_temp, x, y):
        Base_Bullet.__init__(self, screen_temp, x+20, y+40, "bullet-1.gif")

    def move(self):
        self.y += 3

        
def key_control(plane_temp):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                plane_temp.move_left()

            elif event.key == K_d or event.key == K_RIGHT:
                plane_temp.move_right()

            elif event.key == K_w or event.key == K_UP:
                plane_temp.move_up()

            elif event.key == K_s or event.key == K_DOWN:
                plane_temp.move_down()

            elif event.key == K_b :
                plane_temp.hit = True

            elif event.key == K_SPACE:
                plane_temp.fire()


def main():
    screen = pygame.display.set_mode((480,852), 0, 32)
    # 创建背景
    background = pygame.image.load(os.path.join(r"D:\nt_py\plane game\feiji","background.png"))
    # 一个飞机对象
    plane = HeroPlane(screen)
    # 实例化一个敌机
    enemy1 = Enemy1(screen)
    while 1:
        key_control(plane)
        # 放背景
        screen.blit(background,(0,0)) 
        for bullet in  plane.bullet_list:
            # 判断是否击中
            if enemy1.x <= bullet.x <= enemy1.x+50 and enemy1.y <= bullet.y <= enemy1.y+40:
                enemy1.plane_over() 
        for bullet in  enemy1.bullet_list:
            # 判断是否被击中
            if plane.x <= bullet.x <= plane.x+100 and plane.y <= bullet.y <= plane.y+100:
                plane.plane_over() 
        # 打印飞机
        plane.display() 
        # # 打印敌机
        enemy1.display()
        enemy1.move()
        enemy1.fire()
        pygame.display.update()
if __name__ == "__main__":
    main()