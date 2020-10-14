n,m = map(int,input().split())
A=[[] for i in range(n)]
while m>0:
    i,j=map(int,input().split())
    A[i].append(j)
    m-=1
Color = [0]*n
Cycle=False

def DFS(start,Cycle):
    if Color[start-1] == 1:
        Cycle=True
    Color[start] = 1
    for u in A[start]:
        if Color[u]==0:
            DFS(u,Cycle)
        elif Color[u]==1:
            Cycle=True
    Color[start]=2
for i in range(n):
    if Color[i]==0:
        DFS(i,Cycle)
print(Cycle)