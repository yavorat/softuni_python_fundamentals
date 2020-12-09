def calc_factorial(n):
    result = 1
    for num in range(2, n+1):
        result *= num
    return result

a = int(input())
b = int(input())

a_factorial = calc_factorial(a)
b_factorial = calc_factorial(b)

result = a_factorial / b_factorial

print(f"{result:.2f}")