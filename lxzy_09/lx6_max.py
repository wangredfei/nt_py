def mymax(*args):
    if not args :
        return "error"
    
    max_num = 0
    for i in args:
        if type(i) is list or type(i) is tuple :
            for k in i:
                if k >max_num:
                    max_num = k
        
        elif i > max_num:
            max_num = i
    return max_num
print(mymax([6, 8, 3, 5]))
print(mymax(100,200))
print(mymax(1,3,5,9,7))
print(mymax())
