gifts_list = input().split()
command = input()

command_list = []
command_gift = []
command_index = []



while command != "No Money":
    command_list = command.split()
    command_gift = command_list[1]
    if "OutOfStock" in command_list:
        if command_gift in gifts_list:
            gift = 0
            while gift <= len(gifts_list)-1:
                if gifts_list[gift] == command_gift:
                    gifts_list.pop(gift)
                gift += 1

    elif "Required" in command_list:
        command_index = int(command_list[2])
        if command_index < len(gifts_list):
            gifts_list[command_index] = command_gift
    elif "JustInCase" in command_list:
        gifts_list[-1] = command_gift

    command = input()

for el in range(len(gifts_list)):
    print(f"{gifts_list[el]} ", end="")