from random import randint
import pygal
class Die():
    '''表示一个筛子'''
    def __init__(self,num=6):
        self.num = num
    def roll(self):
        return randint(1, self.num)


die = Die()
resules = []
for roii_num in range(1000):
    resule = die.roll()
    resules.append(resule)

# print(resules)
frequencies = []
for value in range(1,die.num+1):
    frequency = resules.count(value)
    frequencies.append(frequency)
print(frequencies)

# 对结果可视化
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels=['1','2','3','4','5','6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")

