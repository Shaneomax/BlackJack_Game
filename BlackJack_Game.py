import random
import sys
import argparse

# Define the card values.
CARD_VALUES = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

# Define the suits.
SUITS = ["Hearts", "Spades", "Clubs", "Diamonds"]

# Create a deck of cards.
deck = []
for suit in SUITS:
    for rank in CARD_VALUES:
        deck.append((rank, suit))

# Shuffle the deck.
random.shuffle(deck)

# Deal two cards to the player and dealer.
player_hand = []
dealer_hand = []
for _ in range(2):
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

# Display the player's hand.
print("Your hand:")
for card in player_hand:
    print(card[0] + " of " + card[1])

# Display the dealer's hand, but hide the second card.
print("Dealer's hand:")
print("* of *")
print(dealer_hand[1][0] + " of " + dealer_hand[1][1])

# Let the player play their hand.
while True:
    hit_or_stand = input("Hit (h) or stand (s)? ")
    if hit_or_stand == "h":
        player_hand.append(deck.pop())
    elif hit_or_stand == "s":
        break
    else:
        print("Invalid input.")

# Calculate the player's hand value.
player_hand_value = 0
for card in player_hand:
    player_hand_value += CARD_VALUES[card[0]]

# Check if the player has busted.
if player_hand_value > 21:
    print("You busted!")
    sys.exit()

# Let the dealer play their hand.
while dealer_hand_value < 17:
    dealer_hand.append(deck.pop())

# Calculate the dealer's hand value.
dealer_hand_value = 0
for card in dealer_hand:
    dealer_hand_value += CARD_VALUES[card[0]]

# Determine the winner.
if player_hand_value > dealer_hand_value:
    print("You win!")
elif player_hand_value < dealer_hand_value:
    print("You lose!")
else:
    print("Tie!")
