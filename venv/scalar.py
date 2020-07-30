n = int(input())
A = [[1]*(n+1) for i in range(n+1)]
for i in range(0,n+1):
    for j in range(0,i+1):
        if i>=2 and j<i and j>0:
            A[i][j]=A[i-1][j]+A[i-1][j-1]
        print(A[i][j],end=' ')
    print()