a=(2,5,7,9,8)
b=list(a)
b[4]=5
b.extend([6,7,8,9,10])
c=tuple(b)
print(c)