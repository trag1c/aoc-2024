def I(A=2):
 P,p=S;D,d=-1,0;V=set();c=A!=2
 while 1:
  if~-(W>P>=0<=p<H):return[len(V),0][c]
  if O[P][p]or(A==(P,p)):P-=D;p-=d;D,d=d,-D
  elif(m:=(P,p,D,d))in V and c:return 1
  else:V.add([(P,p),m][c]);P+=D;p+=d
*D,=open(0);H,W,R=len(D),len(D[0])-1,range
h,w=R(H),R(W);O=[[D[x][y]<'.'for y in h]for x in w]
S=[(x,y)for x in h for y in w if D[x][y]>'.'][0]
print(I(),sum(I((x,y))for x in h for y in w if~-(O[x][y]or(x,y)==S)))