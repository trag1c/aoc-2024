g=0;s=lambda r:-~-any(a==b or(a<b)^(r[0]<r[1])or~-(0<abs(a-b)<4)for a,b in zip(r,r[1:]))
for r in open(0):*r,=map(int,r.split());g+=[any(s(r[:j]+r[j+1:])for j in range(len(r))),1][s(r)]
print(g)