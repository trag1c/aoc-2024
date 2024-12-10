E=enumerate;G={x+y*1j:int(c)for y,l in E(open(0))for x,c in E(l[:-1])}
for P in 1,0:
 R=0
 for C in G:
  if h:=G[C]:continue
  r=[(C,h)];S=set()
  while r:
   *r,(X,h)=r
   for i in-1j,1,1j,-1:
    if~-((N:=X+i)in G)or(H:=G[N])!=h+1:continue
    if P:
     if{N}<S:continue
     S|={N}
    R+=H==9;r+=[(N,H)]*(H!=9)
 print(R)