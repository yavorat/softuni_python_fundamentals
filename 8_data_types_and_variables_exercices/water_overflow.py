n_lines = int(input())

poured_water = 0
for line in range(1, n_lines+1):
    literes = int(input())
    while 255 - poured_water - literes >= 0:
        poured_water += literes
        break
    else:
        print("Insufficient capacity!")

print(poured_water)