numbers = input().split()

opposite_numbers = []

for n in range(len(numbers)):
    number = int(numbers[n]) * -1
    opposite_numbers.append(number)

print(opposite_numbers)