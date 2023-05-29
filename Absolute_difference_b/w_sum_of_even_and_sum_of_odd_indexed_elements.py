n=int(input())
c=0
a=list(map(int,input().split()))
d=0
for i in range(n):
    if i%2!=0:
        c=c+a[i]
    else:
        d=d+a[i]
print(d-c)        
    