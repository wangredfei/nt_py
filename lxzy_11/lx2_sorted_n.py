def sorted_name(name):
    
    return name[::-1]
names = ['Tom','Jerry','Spike','Tyke']
# sorted(names,key=sorted_name)
print(sorted(names,key=sorted_name))
