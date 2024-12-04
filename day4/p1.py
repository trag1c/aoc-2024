*L,=open(p:=0);D=(1,1),(1,0),(1,O:=-1),(0,1),(0,O),(O,1),(O,0),(O,O)
def f(s,X,Y,x,y):
 if max(z:=not s,0>x,0>y):return z
 try:return(0,f(s[1:],X,Y,x+X,y+Y))[L[y][x]==s[0]]
 except:return 0
print(sum(f("XMAS",*d,i//140,i%140)for i in range(19600)for d in D))