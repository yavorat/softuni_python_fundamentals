data = input().split()

bakery = {}

for index in range(0, len(data), 2):
    key = data[index]
    value = data[index + 1]
    bakery[key] = int(value)

print(bakery)