def search(number, A):
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag

def permuts(N:int,M:int=-1, prefix=None):
    M = N if M == -1 else M
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for x in range(1,N+1):
        if search(x,prefix):
            continue
        prefix.append(x)
        permuts(N,M-1,prefix)
        prefix.pop()
permuts(3)
