lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

sum_for_repairs  = 0
counter_shield_brakes = 0

counter_helmet = 0
counter_shield = 0
counter_armor = 0
counter_sword = 0

for n_fight in range(1, lost_fights_count+1):
    if n_fight % 2 == 0:
        sum_for_repairs += helmet_price
        counter_helmet += 1
    if n_fight % 3 == 0:
        sum_for_repairs += sword_price
        counter_sword += 1
    if n_fight % 2 == 0 and n_fight % 3 ==0:
        sum_for_repairs += shield_price
        counter_shield += 1
        counter_shield_brakes += 1
        if counter_shield_brakes != 0 and counter_shield_brakes % 2 == 0:
            sum_for_repairs += armor_price
            counter_armor += 1

print(f'Gladiator expenses: {sum_for_repairs:.2f} aureus')