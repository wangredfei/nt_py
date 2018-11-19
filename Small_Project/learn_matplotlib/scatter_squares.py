import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
x_values = list(range(1,1000))
y_values = [x**2 for x in x_values]

plt.scatter(
    x_values,
    y_values,
    edgecolor='none',
    cmap=plt.cm.Blues,
    c=y_values,# 将参数c设置成一个y值列表,并使用参数cmap告诉pyplot使用哪个颜色映射
    s=40
    )
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value",fontsize=24)
plt.ylabel("Square of Value ", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis="both",which="major",labelsize=14)
plt.axis([0,1100,0,1100000])

# plt.show()

plt.savefig("squares_plot2.png",bbox_inches="tight")
# 第一个实参file  第二个剪切空白区域  默认保留