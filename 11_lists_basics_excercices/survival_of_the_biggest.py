numbers = input().split()
numbers = list(map(int, numbers))
n = int(input())

n_to_remove = None

for iteration in range(n):
    n_to_remove = min(numbers)
    numbers.remove(n_to_remove)

print(numbers)