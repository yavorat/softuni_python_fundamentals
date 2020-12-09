import math

budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_apron = float(input())

total_flour = price_flour * (students - students // 5)
total_eggs = students * 10 * price_egg
total_aprons = price_apron * math.ceil(students * 1.2)

total_price = total_eggs + total_flour + total_aprons

if total_price <= budget:
    print(f"Items purchased for {total_price:.2f}$.")
else:
    print(f"{total_price - budget:.2f}$ more needed.")