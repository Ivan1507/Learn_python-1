from collections import deque
def main():
     G=read_graph()
     start=input()
     while start not in G:
         start = input()
     finish = input()
     while finish not in G:
         finish= input()
     path=djk(G,start,finish)
     path[:]=path[::-1]
     print(path)
def add_egde(G,a,b,w):
    if a not in G:
        G[a]= {b:w}
    else:
        G[a][b]=w

def read_graph():
    M=int(input())
    G ={}
    for i in range(M):
        a,b,w=input().split()
        w=float(w)
        add_egde(G,a,b,w)
        add_egde(G,b,a,w)
    return G
def djk(G,start,finish):
    Q=deque()
    s = {}
    s[start]=0
    parents = {v:None for v in G}
    Q.append(start)
    while Q:
        v=Q.pop()
        for u in G[v]:
            if u not in s or s[v]+G[v][u]<s[u]:
                s[u]=s[v]+G[v][u]
                Q.append(u)
                parents[u]=v
    path=[finish]
    parent=parents[finish]
    while not parent is None:
        path.append(parent)
        parent=parents[parent]
    return path
main()