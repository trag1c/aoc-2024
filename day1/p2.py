a,b=[],[]
for l in open(0):x,y=l.split();a+=[x];b+=[y]
print(sum(b.count(i)*int(i)for i in a))