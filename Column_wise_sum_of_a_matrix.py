n,m=map(int,input().split())
s=[0]*m
for i in range(n):
    m=list(map(int,input().split()))
    for j in range(len(m)):
        s[j]=s[j]+m[j]
for k in s:
    print(k,end=' ')
    