import re;e,s=1,0
for a,b,c in re.findall("(do|'t)\(\)|l\((\d+),(\d+)\)",open(0).read()):
 if b:s+=int(b)*int(c)*e
 else:e=a>"d"
print(s)