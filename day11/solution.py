from functools import*;*N,=map(I:=int,input().split());B=cache(lambda e,i:1if i<1else(B(1,i-1)if e<1else(B(e*2024,i-1)if(l:=len(s:=str(e)))%2else B(I(s[:l//2]),i-1)+B(I(s[l//2:]),i-1))))
for i in 25,75:print(sum(B(n,i)for n in N))