import pygame 
import sys
# 这行代码用来导入python使用的常量
from pygame.locals import *
import random

#1.定义颜色
red = pygame.Color(255,0,0)
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)

# 定义游戏结束函数
def gameover():
    pygame.quit()
    sys.exit()

#定义主函数
def main():
    # 初始化里面的模块
    pygame.init()
    # 控制游戏的速度
    fpsClock = pygame.time.Clock()
    #创建显示层
    playsuiface = pygame.display.set_mode((640,480))
    pygame.display.set_caption("贪吃蛇")
    #初始化变量
    # 初始贪吃蛇的起始坐标位置（100,100）
    snakepos = [100,100]
    snakebod = [[100,100],[80,100],[60,100]]
    # 初始化目标方块的位置
    targetpos = [300,300]
    
    #初始化方向－－》　往右
    direction = "right"
    #定义一个方向变量
    changeDirecftion = direction
   
    #　
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirecftion = "right"
                elif event.key == K_LEFT:
                    changeDirecftion = "left"
                elif event.key == K_UP:
                    changeDirecftion = "up"
                elif event.key == K_DOWN:
                    changeDirecftion = "down"
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        if changeDirecftion == "left" and not direction == "right":
            direction = changeDirecftion
        elif changeDirecftion == "right" and not direction == "left":
            direction = changeDirecftion
        elif changeDirecftion == "down" and not direction == "up":
            direction = changeDirecftion
        elif changeDirecftion == "up" and not direction == "down":
            direction = changeDirecftion
        
        if direction == "right":
            snakepos[0] += 20
        elif direction == "left":
            snakepos[0] -= 20
        elif direction == "up":
            snakepos[1] -= 20
        elif direction == "down":
            snakepos[1] += 20
        if snakepos in snakebod:
            gameover()
        
        snakebod.insert(0, list(snakepos))
        foodpos = [[x*20,y*20] for x in range(1,32) for y in range(1,24) if [x,y] not in snakebod]
        print(foodpos)
                 
        if snakepos == targetpos:
            targetpos = random.choice(foodpos)
        else:
            snakebod.pop()
        
        playsuiface.fill(black)
        # 画图
        for position in snakebod:
            pygame.draw.rect(playsuiface,white,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playsuiface,red,Rect(targetpos[0],targetpos[1],20,20))
        
        pygame.display.flip()
        # 判断出界
        if snakepos[0]>620 or snakepos[0]<0 :
            gameover()
        elif snakepos[1]>460 or snakepos[1] < 0:
            gameover()
        
        fpsClock.tick(5)

if __name__=="__main__":
    main()




