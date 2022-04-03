#! /usr/bin/env python3

import random
import os

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

Suit_Index = 0
Rank_Index = 1

Suits = [Spades, Clubs, Hearts, Diamonds]        
Ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

Suit_Map = {Spades: "Spades", Clubs: "Clubs", Hearts: "Hearts", Diamonds: "Diamonds"}
Suit_Symbols = ['♠', '♣', '♥', '♦']

Rank_Map = {1: "Ace", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Jack", 12: "Queen", 13: "King"}


def build_deck(shuffle=True):
    if debug: print(f"build_deck({shuffle})")

    deck = []
    
    for suit in Suits:

        for rank in Ranks:
            card = (suit, rank)
            if trace: print (card)
            deck.append (card)

    if shuffle: 
        random.shuffle(deck)

    return deck


def is_ace (card): return card[Rank_Index] == Ace
def is_face_card (card): return card[Rank_Index] >= Jack and card[Rank_Index] <= King

def card_value (card):
    if debug: print (f"card_value({card})")

    if is_ace (card): return 11

    if is_face_card (card): return 10

    return card[Rank_Index]

def value_of(hand):
    if debug: print (f"value_of ({hand})")

    value = 0
    ace_count = 0

    for card in hand:
        if trace: print (f"    card_value: {card}")
        value += card_value(card)

        if is_ace (card): ace_count += 1

    while value > 21 and ace_count > 0:
        value -= 10
        ace_count -= 1

    return value


def is_blackjack (hand): return len(hand) == 2 and value_of(hand) == 21


def soft(hand, value):
    if debug: print (f"soft ({hand}, {value}")

    if len(hand) != 2 and value_of(hand) != value: return False
    
    return is_Ace(hand[0]) or is_Ace(hand[1])


def print_card(card, indent=4):
    
    print (" "*indent, end="")
    print (f"{Rank_Map[card[Rank_Index]]} of {Suit_Map[card[Suit_Index]]}")


def print_hand(player, hand):

    print (f"{player}'s cards")

    for card in hand:
        print_card (card)

    print(f"total: {value_of(hand)}\n")


def display_hand (player, hand, hide_first=False):

    if not hide_first:
        lines = [ [] for i in range(9) ]
    
    else:
        hand = hand.copy()
        hand.pop (0)

        lines = [['┌─────────┐'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['│░░░░░░░░░│'],
                 ['└─────────┘']]

    for card in hand:
        space = " "
        suit = Suit_Symbols[card[Suit_Index]-1]

        if is_face_card (card) or is_ace(card):
            rank = Rank_Map[card[Rank_Index]][0]
        else:
            rank = str(card[Rank_Index])

            if len(rank) == 2:
                space = ""

        lines[0].append('┌─────────┐')
        lines[1].append('│{}{}       │'.format(rank, space))
        lines[2].append('│         │')
        lines[3].append('│         │')
        lines[4].append('│    {}    │'.format(suit))
        lines[5].append('│         │')
        lines[6].append('│         │')
        lines[7].append('│       {}{}│'.format(space, rank))
        lines[8].append('└─────────┘')

    result = []

    for index, line in enumerate(lines):
        result.append(''.join(lines[index]))

    print ('\n'.join(result), "\n")


def play():
    if debug: print(f"play()")

    player_bet = 0
    player_bank = 0

    deck = build_deck(shuffle=True)

    deck.pop() # burn a card

    playing_game = True

    while playing_game:
        os.system("clear")

        playing_hand = True

        while playing_hand:
            player_hand = []
            dealer_hand = []
    
            player_hand_total = 0
            dealer_hand_total = 0
    
            print(f"\nPlayer Bank: ${player_bank}\n")

            while True:

                try:
                    player_bet = int(input("Enter your bet: $ ") or 10)
        
                except ValueError:
                    print("> Error: Enter a valid number\n")
                    continue

                break

            print(f"\nPlayer Bet: ${player_bet}\n")

            for i in range(2):
                if len(deck) > 0:
                    player_hand.append(deck.pop())
                    dealer_hand.append(deck.pop())
    
            # print_hand("Player", player_hand)

            display_hand ("Player", player_hand)

            # print ("Dealer's cards")
            # print ("    face down card")
            # print_card (dealer_hand[1])
            # print ()

            display_hand ("Dealer", dealer_hand, hide_first=True)

            if is_ace (dealer_hand[1]):
                insurance = input("Do you want insurance? ").lower()
    
                if insurance == "y":
                    if trace: print("player wants insurance")
                    
                    while True:
                        print(f"initial bet: ${player_bet}")
                        insurance_bet = int(input("How much insurance amount: "))
                
                        if insurance_bet > (player_bet/2):
                            print("you may only bet up to 1/2 of your initial bet")
                            continue
                        
                        break
    
                if is_blackjack (dealer_hand):
                    player_bank -= player_bet
                    player_bank += 2*insurance_bet

                    playing_hand = False
                    continue

                print ("Dealer does not have Blackjack; Player loses insurance bet\n")
                player_bank -= insurance_bet
    
            if is_blackjack(dealer_hand):
                player_bank -= player_bet

                playing_hand = False
                continue
    
            if value_of(player_hand) == 21:
                player_bank += 1.5 * player_bet

                playing_hand = False
                continue
    
            player_can_hit = True
    
            double_down = input("Do you want double down? ").lower()
    
            if double_down == "y":
                player_bet *= 2.0
                player_hand.append(deck.pop())
                display_hand("Player", player_hand)
    
                player_can_hit = False
    
            while player_can_hit:
                player_choice = input("\nPlease choose to (S)tand, (H)it, or s(P)lit: ").lower()
                
                if player_choice == "s":
                    player_can_hit = False
                    continue
    
                if player_choice == "h":
                    card = deck.pop()
                    print ("Players hits and gets the", end=" ")
                    print_card (card, 0)

                    player_hand.append(card)
                    display_hand("Player", player_hand)
    
                    if value_of(player_hand) > 21:
                        player_can_hit = False
                        continue
    
                if player_choice == "p":
                    pass

            if value_of(player_hand) > 21:
                print ("Player busts")
                player_bank -= player_bet

                playing_hand = False
                continue
    
            display_hand("Dealer", dealer_hand)

            while value_of(dealer_hand) < 17:
                card = deck.pop()
                print (f"Dealer hits and gets the", end=" ")
                print_card (card, 0)
                print ()

                dealer_hand.append(card)
                display_hand("Dealer", dealer_hand)
    
            if value_of(dealer_hand) > 21:
                print ("Dealer busts")
                player_bank += player_bet

                playing_hand = False
                continue
    
            if value_of(dealer_hand) > value_of(player_hand):
                print ("Dealer has better hand, so player loses")
                player_bank -= player_bet

                playing_hand = False
                continue
    
            if value_of(dealer_hand) == value_of(player_hand):
                print ("Dealer pushes, so player loses")
                player_bank -= player_bet

                playing_hand = False
                continue
    
            print ("Player wins")
            player_bank += player_bet

        print(f"\nPlayer Bank: ${player_bank}\n")

        playing_game = not input("Another Round? ").lower()[0] != "y"

    print("\n>>> Goodbye...\n")


if __name__ == "__main__":
    play()
