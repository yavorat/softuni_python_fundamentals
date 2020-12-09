friends = input().split(", ")
command = input()

blacklisted_names = 0
lost_names = 0

while not command == "Report":
    command_type = command.split()[0]
    command_name = command.split()[1]
    if command_type == "Blacklist":
        for friend_index in range(len(friends)):
            if friends[friend_index] == command_name:
                friends[friend_index] = "Blacklisted"
                print(f"{command_name} was blacklisted.")
                blacklisted_names += 1
                break
            else:
                continue
        else:
            print(f"{command_name} was not found.")
    elif command_type == "Change":
        if int(command_name) < len(friends) and int(command_name) > 0:
            friend_name_changed = friends[int(command_name)]
            friends[int(command_name)] = command.split()[2]
            print(f"{friend_name_changed} changed his username to {command.split()[2]}.")
    elif command_type == "Error":
        if not (friends[int(command_name)] == "Blacklisted" or friends[int(command_name)] == "Lost"):
            friend_name_lost = friends[int(command_name)]
            friends[int(command_name)] = "Lost"
            print(f"{friend_name_lost} was lost due to an error.")
            lost_names += 1


    command = input()
print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(' '.join(friends))
