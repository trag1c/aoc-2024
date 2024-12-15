import re;from fractions import*;F=Fraction;N=10**13;f=lambda x:map(int,re.findall(R,x)[0]);R=r"(\d+)\D+(\d+)";S=open(0).read().split("\n\n");O=o=0
def C(P,p,A,a,B,b):c=F(A*p-a*P,A*b-a*B);C=F(P-B*c,A);return(3*C+c)*(C.denominator==c.denominator<2)
for s in S:a,b,p=s.split("\n");A,a=f(a);B,b=f(b);P,p=f(p);a=A,a,B,b;O+=C(P,p,*a);o+=C(P+N,p+N,*a)
print(O,o)