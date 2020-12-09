team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

was_terminated = False
card_team = ""
card_player = ""

cards = input().split()

for card in range(0, len(cards)):
    card_team, card_player = cards[card].split("-")
    card_player = int(card_player)
    if card_team == "A":
        if card_player not in team_a:
            continue
        team_a.remove(card_player)
        if len(team_a) < 7:
            was_terminated = True
            break
    if card_team == "B":
        if card_player not in team_b:
            continue
        team_b.remove(card_player)
        if len(team_b) < 7:
            was_terminated = True
            break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if was_terminated:
    print("Game was terminated")


