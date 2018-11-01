# turtle 小乌龟绘图库
1. 画布(canvas)
- 画布就是turtle为我们展开用于绘图区域，我们可以设置它的大小和初始位置。
- 设置画布大小
    - `turtle.screensize(canvwidth=None, canvheight=None, bg=None)`
    - 参数分别为画布的宽(单位像素), 高, 背景颜色。
    - turtle.setup(width=0.5, height=0.75, startx=None, starty=None)，参数：width, height: 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例，(startx, starty): 这一坐标表示矩形窗口左上角顶点的位置, 如果为空,则窗口位于屏幕中心。
```py
turtle.screensize(800,600, "green")

turtle.screensize() #返回默认大小(400, 300)


turtle.setup(width=0.6,height=0.6)
turtle.setup(width=800,height=800, startx=100, starty=100)
```
2. 画笔

- 画笔的状态
    - 在画布上，默认有一个坐标原点为画布中心的坐标轴，坐标原点上有一只面朝x轴正方向小乌龟。这里我们描述小乌龟时使用了两个词语：坐标原点(位置)，面朝x轴正方向(方向)， turtle绘图中，就是使用位置方向描述小乌龟(画笔)的状态。

- 画笔的属性(画笔的属性，颜色、画线的宽度等)

    1. turtle.pensize()：设置画笔的宽度；

    2. turtle.pencolor()：没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。

    3. turtle.speed(speed)：设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。


