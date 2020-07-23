n = int(input())
A = [int(a) for a in input().split()]
l = int(input())
B = [int(q) for q in input().split()]
F=[[0]*(len(B)+1) for i in range(len(A)+1)]
for i in range(1,n+1):
    for j in range(1,l+1):
        if A[i-1]==B[j-1]:
            F[i][j]=F[i-1][j-1]+1
        else:
            F[i][j]=max(F[i-1][j],F[i][j-1])
C = []
i = n
j = l
while F[i][j]>0:
    if F[i][j]==F[i-1][j]:
        i -= 1
    elif F[i][j]==F[i][j-1]:
        j -= 1
    else:
        C.append(A[i-1])
        i -= 1
        j -= 1
C.reverse()
for i in range(0,F[-1][-1]):
    print(C[i])
