M,i=map,[];X=Y=0;a,b=M(str.split,open(0).read().split("\n\n"))
def I():
 for V in(eval(x.replace(*"|,"))for x in a):
  try:
   i,j=M(P.index,V)
   if i>j:return i,j
  except:0
for P in M(eval,b):
 if I():i+=[P]
 else:X+=P[len(P)//2]
for P in M(list,i):
 while I():i,j=I();P[i],P[j]=P[j],P[i]
 Y+=P[len(P)//2]
print(X,Y)