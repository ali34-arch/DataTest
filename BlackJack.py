import random
deck = ['1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS',
        '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD',
        '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH',
        '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC']
card_values = {
    '1': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10
}
def shuffle(deck):
    random.shuffle(deck)
    return deck

deck = shuffle(deck)



def del_hand(deck, total):
    hand = []
    for i in range (total):
        hand.append(deck.pop()) #faster and there's no change if the first item is picked instead
#    print(hand)
    return hand
player = del_hand(deck, 2)
dealer = del_hand(deck, 2)
print(f"Player hand: {player}")
print(f"Dealer hand: {dealer}")
print(f"Total remaining: {len(deck)}")