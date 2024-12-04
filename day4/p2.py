*L,=open(p:=0);D=(1,1),(1,0),(1,O:=-1),(0,1),(0,O),(O,1),(O,0),(O,O);X=range;Z=X(140)
def f(X,x,y,s="MAS"):
 if max(z:=not s,0>x,0>y):return z
 try:return(0,f(X,x+X,y+1,s[1:]))[L[y][x]==s[0]]
 except:return 0
for _ in X(4):
 for y in Z:
  for x in Z:p+=f(1,x,y)&f(O,x+2,y)
 L=[[*i][::O]for i in zip(*L)]
print(p)