*L,=open(0);l=len;W=l(L[0])-1;D=-1,1j,1,-1j;S=set;E=enumerate
G={x+y*1j:c for y,l in E(L)for x,c in E(l)}
def I(x):
 i,s,c=S(),S(),G[x];a=x,
 while a:
  *a,p=a;i|={p}
  for d in D:
   if{n:=p+d}<s:continue
   s|={n}
   if(l(L)>n.imag>=0<=n.real<W)and G[n]==c:a+=n,
 return i
o=S();A=B=0
for p in range(W*l(L)):
 if{p:=p//W+p%W*1j}<o:continue
 t=S();P=s=0
 for u in sorted(i:=I(p),key=lambda x:(x.imag,x.real)):
  for d in D:
   if~-({n:=u+d}<i):P+=1;t|={(n,d)};s+=not{(n+D[(p:=D.index(d)+1)%4],d),(n+D[p-2],d)}&t
 A+=l(i)*P;B+=l(i)*s;o|=i
print(A,B)