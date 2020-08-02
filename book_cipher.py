def erotosfen(N):
    A = []
    for i in range(0, N+1):
        A.append(True)
    for i in range(2, N+1):
        if A[i]:
            for j in range(i+i,N+1,i):
                A[j] = False
    for i in range(2, N+1):
        if A[i]:
            print(i)
erotosfen(int(input()))