price_ratings = [int(el) for el in input().split()]
entry_point = int(input())
items_to_break = input()
items_to_look_for = input()
a = 5

left_list = price_ratings[0:entry_point]
right_list = price_ratings[(entry_point+1):len(price_ratings)]

left_damage = []
right_damage = []

if items_to_break == "cheap":
    if items_to_look_for == "negative":
        left_damage = [el for el in left_list if el < price_ratings[entry_point] and el < 0]
        right_damage = [el for el in right_list if el < price_ratings[entry_point] and el < 0]
    elif items_to_look_for == "positive":
        left_damage = [el for el in left_list if el < price_ratings[entry_point] and el > 0]
        right_damage = [el for el in right_list if el < price_ratings[entry_point] and el > 0]
    else:
        left_damage = [el for el in left_list if el < price_ratings[entry_point]]
        right_damage = [el for el in right_list if el < price_ratings[entry_point]]
else:
    if items_to_look_for == "negative":
        left_damage = [el for el in left_list if el >= price_ratings[entry_point] and el < 0]
        right_damage = [el for el in right_list if el >= price_ratings[entry_point] and el < 0]
    elif items_to_look_for == "positive":

        left_damage = [el for el in left_list if (el >= price_ratings[entry_point] and el > 0)]
        right_damage = [el for el in right_list if (el >= price_ratings[entry_point] and el > 0)]
    else:
        left_damage = [el for el in left_list if el >= price_ratings[entry_point]]
        right_damage = [el for el in right_list if el >= price_ratings[entry_point]]

sum_left_damage = sum(left_damage)
sum_right_damage = sum(right_damage)

if sum_left_damage >= sum_right_damage:
    print(f"Left - {sum_left_damage}")
else:
    print(f"Right - {sum_right_damage}")