x=input().split()
x=sorted(x)
x.sort(key=len)
print(*x)