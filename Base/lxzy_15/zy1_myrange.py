# 练习:
# 1. 写一个生成器函数myrange([start,]stop[,step])
#     来生成一系列的整数
#   要求myxrange功能与range函数功能完全相同
#   (不允许调用range函数和列表)
#   用自己写的myxrange,结合生成器表达式求100以内所
#   有的奇数的平方和

def myrange(start, stop = None , step = 1):
	# 判断输入几个数,如果为空则第一个数作为结束,开始为0
	if stop is None  :
		stop = start
		start = 0
	# 判断步长
	if step < 0:
		while  start > stop:
			yield start
			start += step
	elif step > 0:
		while start < stop :
			yield start
			start += step
	else :
		return
# for i in myrange(-3,0):
# 	print(i)

print(sum(i**2 for i in myrange(100)if i%2==1))
# print(sum(i**2 for i in range(100)if i%2==1))