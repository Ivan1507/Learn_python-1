price ,delta ,week = map(int,input().split())
money = 0
week *= 7
t = price
while week >0:
    if week == 1:
        price = t
    else:
        price += delta
    money += price
    week -= 1
print(money)

