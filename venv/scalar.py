from collections import deque
letters='abcdfegh'
numbers='12345678'
G=dict()
for l in letters:
    for n in numbers:
        G[l+n]=set()
def add_egde(v1,v2):
    G[v1].add(v2)
    G[v2].add(v1)


print(G)
start_vertex=input()
end_vertex=input()
distances= {v:None for v in G}
parents={v:None for v in G}
distances[start_vertex]=0
queue=deque([start_vertex])
while queue:
    cur_v=queue.popleft()
    for v in G[cur_v]:
        if distances[v] is None:
            distances[v]=distances[cur_v]+1
            parents[v]=cur_v
            queue.append(v)
path= [end_vertex]
parent=parents[end_vertex]
k = 0
while not parent is None:
    path.append(parent)
    parent=parents[parent]
    k+=1
path[:]=path[::-1]
i=0
while i<=k:
    print(path[i])
    i+=1
