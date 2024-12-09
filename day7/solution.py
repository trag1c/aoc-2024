I=int
def E(l):r,v=l.split(":");return[*map(I,v.split())],I(r)
def V(e):
 o=[I.__add__,I.__mul__]+[lambda x,y:I(f"{x}{y}")]*c;(a,*b),r=e;s={a}
 for v in b:s=set.union(*({f(x,v)for x in s}for f in o))
 return({r}<s)*r
*l,=open(0)
for c in 0,1:print(sum(map(V,map(E,l))))