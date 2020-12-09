import copy

cards = input().split()
n_shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]

shuffled_cards = []

half = len(cards) // 2

for n_shuffle in range(n_shuffles):
    left_cards = []
    right_cards = []

    for card in range(1, half):
        left_cards.append(cards[card])
    for card in range(half, len(cards) - 1):
        right_cards.append(cards[card])

    for index in range(len(left_cards)):
        shuffled_cards.append(right_cards[index])
        shuffled_cards.append(left_cards[index])

    cards = shuffled_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffled_cards = []

print(cards)