companions = int(input())
days = int(input())

coins = 0

for n_day in range(1, days+1):
    if n_day % 10 == 0:
        companions -= 2
    if n_day % 15 == 0:
        companions += 5
    coins += 50
    coins -= companions * 2
    if n_day % 3 == 0:
        coins -= companions * 3
    if n_day % 5 == 0:
        coins += companions * 20
        if n_day % 3 == 0:
            coins -= companions * 2

print(f"{companions} companions received {int(coins / companions)} coins each.")
