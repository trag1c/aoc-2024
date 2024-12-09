from itertools import*;*L,=open(0);l=len;W,H=l(L[0])-1,l(L);N={};S=set;s=S.add;P=S();p=S()
for i in range(H*W):
 c=L[i//W][i%W]
 if'.'<c:s(N.setdefault(c,S()),(i//W,i%W))
for n in N:
 for A,B in combinations(N[n],2):
  p|={A,B};A,a=A;B,b=B
  for Z,z,D,d in(A,a,-B+A,-b+a),(B,b,B-A,b-a):
   Z+=D;z+=d
   if H>z>=0<=Z<W:s(P,(Z,z))
   while H>z>=0<=Z<W:s(p,(Z,z));Z+=D;z+=d
print(l(P),l(p))