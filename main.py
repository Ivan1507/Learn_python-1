def search(number, A):
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    print(flag)
A = [54, 12, 32, 67, 123]
search(12, A)

