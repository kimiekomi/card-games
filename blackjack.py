#! /usr/bin/env python3

import random
import os

from cards import *

debug = False
trace = False

def play(deck=None):
    if debug: print(f"\nplay()")

    testing = False
    keep_playing = True 

    player_earnings = 0
    player_bank = 100

    if deck == None:
        deck = build_deck()

    else:
        testing = True
        
    # burn card
    deck.pop(0)

    while keep_playing:
        print("\n*** Let's Play Blackjack ***\n")

        player_bank += player_earnings

        print(f"Player Bank: ${player_bank}")

        player_earnings = play_hand(deck)
        
        print(f">>> Player Earnings: ${player_earnings}")

        if testing:
            keep_playing = False

        else:
            another_round = input("\nAnother Round? ").lower()
    
            if another_round[0] != "y":
                print("\n>>> Goodbye...\n")
                break
    
            os.system("clear")
    

def play_hand(deck):
    if debug: print("play_hand()")

    player_hand = []
    dealer_hand = []

    initial_bet = 0
    insurance = False
    insurance_bet = 0

    while True:

        try:
            initial_bet = float(input("\nEnter initial bet: $ ") or 10)

        except ValueError:
            print("> Error: Enter a valid number\n")
            continue

        break

    print(f"initial bet: ${initial_bet}")
    
    for i in range(2):

        if len(deck) == 0:
            raise Exception("Handle later...need at least 4 cards")
            
        player_hand.append(deck.pop(0))
        
        if len(deck) == 0:
            raise Exception("Handle later...need at least 4 cards")
            
        dealer_hand.append(deck.pop(0))

    print("\nplayer hand:")
    print_hand(player_hand)
    print("\ndealer hand:")
    print("___ of ___")
    print_card(dealer_hand[1])
    
    print(f"\nplayer hand total: {total(player_hand)}")

    if trace: print(f"dealer hand total: {total(dealer_hand)}")
    
    print(f"dealer card2 value: {value(dealer_hand[1])}") 

    if is_ace(dealer_hand[1]):
        want_insurance = input("\nDo you want insurance? ").lower()

        if want_insurance == "y":
            print("player wants insurance")

            insurance = True
            
            while True:
                print(f"initial bet: ${initial_bet}")

                try:
                    insurance_bet = float(input("\nEnter insurance amount: $ ") or (initial_bet/2))
            
                    if insurance_bet > (initial_bet/2):
                        print("> may only bet up to HALF the initial bet")
                        continue

                except:
                    print("Enter a valid number")
                    continue

                break

            print(f"insurance bet: ${insurance_bet}")

    if is_blackjack(dealer_hand) or is_blackjack(player_hand):
        return settle_bets(dealer_hand, player_hand, initial_bet, insurance_bet)

    if total(player_hand) == 9 or total(player_hand) == 10 or total(player_hand) == 11:
        want_double = input("\nDo you want to double down? ").lower()

        if want_double == "y":
            print("player wants to double down")

            initial_bet = initial_bet*2

            print(f"\nUpdated Initial Bet: ${initial_bet}")

            if len(deck) == 0:
                raise Exception("Handle later...need at least 4 cards")
    
            hit_card = deck.pop(0)
            hand.append(hit_card)
                
            print("\nupdated player hand:")
            print_hand(hand)
            print(f"\nupdated player hand total: {total(hand)}") 

            return settle_bets(dealer_hand, player_hand, initial_bet, insurance_bet)
            
    player_move(player_hand, deck, initial_bet)

    # game over logic
    if total(player_hand) > 21:
        print("\n>>> Player Bust...You Lose")
        return -initial_bet

    dealer_move(dealer_hand, deck)

    if total(dealer_hand) > 21:
        print("\n>>> Dealer Bust...You Win")
        return initial_bet

    return settle_bets(dealer_hand, player_hand, initial_bet, insurance_bet)
     

def build_deck(shuffle=True):
    if debug: print("build_deck()")

    suits = [Spades, Clubs, Hearts, Diamonds]        
    ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    # if trace: print(f"\ngame deck({len(deck)}): {deck}")

    if shuffle:
        random.shuffle(deck)

    return deck


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

    # if trace: print(f"{rank} of {suit}")
        
    print(f"{rank} of {suit}")


def print_hand(hand):
    if debug: print("print_hand()")
        
    for card in hand:
        print_card(card)


def display_card(card):
    if debug: print("display_card()")

    suits_symbols = ['♠', '♣', '♥', '♦']

    rank = card[0]
    suit = card[1]

    if rank == 1: rank = "A"
    if rank == 11: rank = "J"
    if rank == 12: rank = "Q"
    if rank == 13: rank = "K"
    
    suit = suits_symbols[card[1]-1]

    print("┌───────┐")
    print(f"│{rank}      │")
    print("│       │")
    print(f"│   {suit}   │")
    print("│       │")
    print(f"│      {rank}│")
    print("└───────┘")
    

def display_hand(hand):
    if debug: print("display_hand()")

    for card in hand:
        display_card(card)
        

def value(card):
    if debug: print("value()")

    rank = card[0]
    
    if rank == Ace:
        return 11

    if rank == Jack or rank == Queen or rank == King:
        return 10

    # if trace: print(f"rank: {rank}")
        
    return rank


def total(hand):
    if debug: print("total()")

    total = 0
    ace_count = 0

    for card in hand:
        total += value(card)

        if card[Rank] == Ace:
            ace_count += 1
            
    while ace_count > 0 and total > 21:
        ace_count -= 1
        total -= 10
    
    # if trace: print(f"hand total: {total}")
    
    return total


def is_blackjack(hand):
    if debug: print("is_blackjack()")

    return len(hand) == 2 and total(hand) == 21


def is_ace(card):
    if debug: print("is_ace()")
        
    return card[Rank] == Ace


def dealer_move(hand, deck):
    if debug: print("dealer_move()")

    print("\ndealer hand revealed:")
    print_hand(hand)
    
    if trace: print(f"dealer hand total: {total(hand)}")
         
    while total(hand) < 17:
        
        if len(deck) == 0:
            raise Exception("Handle later...need at least 4 cards")
            
        dealer_card = deck.pop(0)
        hand.append(dealer_card)
        
        if total(hand) >= 21:
            break

    if len(hand) > 2:
        print("\nupdated dealer hand:")
        print_hand(hand)
    
    print(f"\nupdated dealer hand total: {total(hand)}")

    return total(hand)


def player_move(hand, deck, player_wager):
    if debug: print("player_move()")

    while True:
        first_option = input("\nEnter your move (s-stand, h-hit): ")[0].lower()
    
        if first_option == "s":
            print("player elected to stand")
            return

        if first_option == "h":
            print("player elected to hit")

            if len(deck) == 0:
                raise Exception("Handle later...need at least 4 cards")
        
            hit_card = deck.pop(0)
            hit_card_rank = hit_card[0]
            hand.append(hit_card)
            
            print("\nupdated player hand:")
            print_hand(hand)
            print(f"\nupdated player hand total: {total(hand)}") 
    
            if total(hand) >= 21: 
                return


def settle_bets(dealer_hand, player_hand, player_wager, player_insurance):

    if is_blackjack(dealer_hand):

        if player_insurance > 0:
            print("\n>>> You win insurance bet")

        if is_blackjack(player_hand):
            print("\n>>> Both have blackjack...Its a Draw")
            return player_insurance * 2

        print("\n>>> Dealer has blackjack...You lose")
        return -player_wager + player_insurance * 2
    
    if is_blackjack(player_hand):
        print("\n>>> Player has blackjack...You win")
        return player_wager * 1.5 - player_insurance
            
    if total(dealer_hand) > total(player_hand):
        print("\n>>> Dealer is closer to 21...You Lose")
        return -player_wager - player_insurance

    if total(player_hand) > total(dealer_hand):
        print("\n>>> Player is closer to 21...You Win")
        return player_wager - player_insurance

    return -player_insurance


if __name__ == "__main__":
    play()
    
    # sample_display = [Ace_of_Spades, Two_of_Hearts, Jack_of_Clubs, Queen_of_Spades, King_of_Diamonds]
    # hand_hit = [Ace_of_Spades, Four_of_Hearts]
    # hand_hit_bust = [Ace_of_Spades, Nine_of_Hearts]
    # hand_double = [Two_of_Spades, Seven_of_Hearts]
    
    # deck = [Two_of_Spades, Four_of_Spades, Six_of_Spades, Eight_of_Spades, Ten_of_Spades]
    
    # player_move(hand_double, deck, 10)

    # display_card(Ace_of_Spades)
    # display_card(Two_of_Hearts)
    # display_card(Jack_of_Clubs)
    # display_card(Queen_of_Spades)
    # display_card(King_of_Diamonds)
    
    # display_hand(sample_display)

    # print(total([Ace_of_Spades, Ace_of_Hearts, Ace_of_Clubs]))
