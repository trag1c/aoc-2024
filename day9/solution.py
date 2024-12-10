from collections import*
D,R,I,E,Q,N=input(),range,int,enumerate,deque,None;q=Q.append
for p in 0,1:
 A=Q();S=Q();P,F=0,[]
 for i,c in E(map(I,D)):
  if i&1:q(S,(P,c));F+=[N]*c;P+=c;continue
  i>>=1
  if p:q(A,(P,c,i))
  for _ in R(c):
   if~-p:q(A,(P,1,i))
   P+=1;F+=i,
 for P,z,f in[*A][::-1]:
  for a,(b,c)in E(S):
   if b>=P or z>c:continue
   for i in R(z):F[P+i],F[b+i]=N,f
   S[a]=b+z,c-z
   break
 print(sum(i*c for i,c in E(F)if c))