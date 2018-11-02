# 参考 https://blog.csdn.net/FengF2017/article/details/79300801
import pygame as pg
import sys
import random
import time
pg.init()
# s设置大小
game_window = pg.display.set_mode((600,500))
# 定义框名称
pg.display.set_caption("接球")
# 定义地板颜色 球颜色 板颜色
window_color = (0,0,255)
ball_color = (255,165,0)
rect_color = (255,255,0)
# 设置球从随机位置开始
ball_x = random.randrange(50,400)
ball_y = 20

move_x = 1
move_y = 1
# 分数
score = 0
point = 1
count = 0
font = pg.font.Font(None, 70)
while 1:
    game_window.fill(window_color)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
    # 得到鼠标位置
    mouse_x, mouse_y = pg.mouse.get_pos()
    my_text = font.render(str(score),False,(255,255,255))
    game_window.blit(my_text, (500,30))
    ball_x += move_x
    ball_y += move_y
    # 碰壁返回
    if ball_x <= 20 or ball_x >=580:
        move_x = -move_x
    if ball_y <= 20 :
        move_y = -move_y
    #接到球
    elif mouse_x - 20 < ball_x < mouse_x+120 and ball_y>=470:
        count += 1
        move_y = -move_y
        score += point
        if count  == 3:
            count = 0
            point += point
            if move_x > 0 :
                move_x += 1
            elif move_x < 0:
                move_x -= 1
            move_y -= 1
    # 没接到
    elif ball_y >= 480 and  (ball_x <= mouse_x-20 or ball_x >= mouse_x+100+20 ):
        break 

    time.sleep(0.005)
    # 画球和班子
    pg.draw.circle(game_window,ball_color,(ball_x,ball_y),20)
    pg.draw.rect(game_window, rect_color,(mouse_x, 490,100,10))
    # 更新
    pg.display.update()