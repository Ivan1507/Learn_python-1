n = int(input())
A = [0] * n
for i in range(n):
    A[i] = int(input())
mx = 0
mr = 0
c = 0
for i in range(n):
    for j in range(i+1,n):
        if A[i] == A[j]:
            c += 1
    if c > mx:
        mx = c
        mr = A[i]
    c = 0
if n == 1:
    print(A[0])
else:
    print(mr)

