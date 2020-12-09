numbers = input().split(", ")
beggars = int(input())
beggars_sums = [0] * beggars
result = []
iteration = 0

if beggars > len(numbers):
    result = numbers.copy()
    diff = beggars - len(numbers)
    for n in range(len(result)):
        result[n] = int(result[n])

    for i in range(diff):
        result.append(0)
    beggars_sums = result.copy()
else:
    for n in range(0, len(numbers)):
        if iteration == beggars:
            iteration = 0
        beggars_sums[iteration] += int(numbers[n])
        iteration += 1

print(beggars_sums)


