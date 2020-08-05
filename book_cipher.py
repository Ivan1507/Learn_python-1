n = int(input())
w = int(input())
M =[]*n
V = []*n
for i in range(0,n):
    k = int(input())
    M.append(k)
    v = int(input())
    V.append(v)
F = [[0]*(n+1) for i in range(w+1)]
for i in range(1, n+1):
    for k in range(1, w+1):
        if M[i-1] <= k:
            F[k][i] = max(F[k][i-1],V[i-1]+F[k-M[i-1]][i-1])
        else:
            F[k][i] = F[k][i-1]
for i in range(1,n+1):
    for j in range(1,w+1):
        print(F[j][i],end=' ')
    print()
print(F[w][n])

