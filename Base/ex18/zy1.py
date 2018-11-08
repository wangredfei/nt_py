# 练习:
#   1. 写一个类Bicycle自行车类,有run方法,调用时
#   显示骑行的里程km
#     class Bicycle:
#         def run(self, km):
#             print("自行车骑行了", km, '公里')
#     再写一个EBicycle电动自行车类,在Bicycle的基础
#     上添加了电池电量volume属性,有两个方法:
#       fill_charge(vol)  用来充电 vol为电量
#       run(km)  方法,每骑行10km消耗电量1度,同时显
#       示当前电量,当电量耗尽时则调用Bicycle的run方法
#       (用脚蹬骑行)
    
#     class EBicycle:
#         ....
#     b = EBicycle(5)  新买的电动车内有5度电
#     b.run(10) 电动骑行了10km里,还剩4度电
#     b.run(100) 电动骑行了40km里,还剩0度电,用脚蹬
#             骑行了60km
#     b.fill_charge(10)  电动自行车充电10度
#     b.run(50)  电动骑行了50km里,还剩5度电

class Bicycle():
    def run(self, km):
        print("自行车骑行了",km , '公里')

class EBicycle(Bicycle):
    def __init__(self, volume = 0):
        self.volume = volume
        print("新买的电动车内有{}度电".format(self.volume))
    def fill_charge(self,vol):
        self.volume += vol
        print("电动自行车充电{}度,还有{}度".format(vol,self.volume))
    def run(self,km):
        e_km = min(km, self.volume*10)
        if e_km > 0 :
            self.volume -= e_km/10
            print("电动车骑行了%d公里,还剩余%d度电"%(e_km,self.volume))
        if km - e_km:
            super().run(km-e_km)
        # if  km/10 >= self.volume :
        #     # 电动车骑行了drun公里
        #     drun = self.volume*10
        #     self.volume = 0 
        #     print("电动骑行了{}公里, 还剩{}度电".format(drun,self.volume))
        #     super().run(km-drun)
        # else :
        #     self.volume = self.volume - km/10
        #     print("电车骑行了{}公里,还剩{}度电".format(km,self.volume))
b = EBicycle(5)  #新买的电动车内有5度电
b.run(10) #电动骑行了10km里,还剩4度电
b.run(100) #电动骑行了40km里,还剩0度电,用脚蹬骑行了60km
b.fill_charge(10)  #电动自行车充电10度
b.run(50)  #电动骑行了50km里,还剩5度电
