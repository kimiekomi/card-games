#! /usr/bin/env python3

debug = False
trace = False

Ace = 1
Jack = 11
Queen = 12
King = 13

Spades = 1
Clubs = 2
Hearts = 3
Diamonds = 4

def print_card(card):
    if debug: print("print_card()")

    rank = card[0]
    suit = card[1]

    if rank == Ace:
        rank = "Ace"

    elif rank == Jack:
        rank = "Jack"

    elif rank == Queen:
        rank = "Queen"

    elif rank == King:
        rank = "King" 

    else:
        rank = str(rank)

    if suit == Spades:
        suit = "Spades"

    elif suit == Clubs:
        suit = "Clubs"

    elif suit == Hearts:
        suit = "Hearts"

    elif suit == Diamonds:
        suit = "Diamonds"

    if trace: print(f"{rank} of {suit}")
        
    return f"{rank}_of_{suit}"

def build_deck():
    if debug: print("deck() called")

    suits = [Spades, Clubs, Hearts, Diamonds]        
    ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

    deck = []
    card_deck = []

    file = open("cards.py", "a")
    
    for suit in suits:
        for rank in ranks:
            card = (rank, suit)
            
            deck.append(card)
            card_deck.append(print_card(card))

            file.write(f"{print_card(card)} = {card}\n")

    file.write(f"\ncard_deck = {card_deck}")
    file.close()

    if trace: print(f"\ngame deck({len(deck)}): {deck}")

    return deck


if __name__ == "__main__":
    build_deck()

