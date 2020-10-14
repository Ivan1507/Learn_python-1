from collections import deque
n,m= map(int,input().split())
G = {i:set() for i in range(n)}
q = m
while m>0:
    i, j=map(int,input().split())
    G[i].add(j)
    G[j].add(i)
    m -= 1
ans = 'YES'
if q!=0:
    k = len(G[0])
    for i in range(1, n):
        if len(G[i]) != k:
            ans = "NO"
            break
print(ans)





