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

    global player_earnings
    
    player_earnings = 0

    if deck == None:
        deck = build_deck()

    else:
        testing = True
        
    # burn card
    deck.pop(0)

    while keep_playing:
        print(f"\nPlayer Earnings: ${player_earnings}\n")

        play_hand(deck)

        if testing:
            keep_playing = False

        else:
            another_round = input("\nAnother Round? ").lower()
    
            if another_round[0] != "y":
                break
    
            os.system("clear")
    
        print("\n>>> Goodbye...\n")
        

def play_hand(deck):
    if debug: print("play_hand()")

    player_hand = []
    dealer_hand = []

    initial_bet = 0
    insurance = False
    insurance_bet = 0

    while True:

        try:
            initial_bet = float(input("Enter initial bet: $ ") or 10)

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

    if dealer_hand[1][0] == Ace:
        want_insurance = input("\nDo you want insurance? ").lower()

        if want_insurance == "y":
            if trace: print("player wants insurance")

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

    player_move(player_hand, deck)    

    # game over logic
    if total(player_hand) > 21:
        print("\n>>> Player Bust...You Lose")
        # player_earnings -= initial_bet
        return -initial_bet

    dealer_move(dealer_hand, deck)

    if total(dealer_hand) > 21:
        print("\n>>> Dealer Bust...You Win")
        # player_earnings += initial_bet 
        return initial_bet

    return settle_bets(dealer_hand, player_hand, initial_bet, insurance_bet)
     

def settle_bets(dealer_hand, player_hand, player_wager, player_insurance):

    result = 0

    if is_blackjack(dealer_hand):

        if player_insurance > 0:
            print("\n>>> You win insurance bet")

        if is_blackjack(player_hand):
            print("\n>>> Both have blackjack...Its a Draw")
            result = player_insurance * 2

        print("\n>>> Dealer has blackjack...You lose")
        result = -player_wager + player_insurance * 2
    
    if is_blackjack(player_hand):
        result = player_wager * 1.5 - player_insurance
            
    if total(dealer_hand) > total(player_hand):
        print("\n>>> Dealer is closer to 21...You Lose")
        result = -player_wager - player_insurance

    if total(player_hand) > total(dealer_hand):
        print("\n>>> Player is closer to 21...You Win")
        result = player_wager - player_insurance

    result = -player_insurance

    print(f">>> Updated Player Earnings: ${result}")
    return result
    

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

        rank = card[0]
    
        if rank == Ace:
            ace_count += 1
            
    if ace_count > 0 and total > 21:
            total -= 10
    
    # if trace: print(f"hand total: {total}")
    
    return total


def is_blackjack(hand):
    if debug: print("is_blackjack()")

    return len(hand) == 2 and total(hand) == 21


def dealer_move(hand, deck):
    if debug: print("dealer_move()")

    print("\ndealer hand revealed:")
    print_hand(hand)
    
    dealer_hand_total = total(hand)

    if trace: print(f"dealer hand total: {dealer_hand_total}")
         
    while dealer_hand_total < 17:
        
        if len(deck) == 0:
            raise Exception("Handle later...need at least 4 cards")
            
        dealer_card = deck.pop(0)
        hand.append(dealer_card)
        dealer_hand_total += value(dealer_card)
        
        if value(dealer_card) == 11 and dealer_hand_total >= 21:
            dealer_hand_total -= 10
            break

    if len(hand) > 2:
        print("\nupdated dealer hand:")
        print_hand(hand)
    
    print(f"\nupdated dealer hand total: {dealer_hand_total}")

    return dealer_hand_total


def player_move(hand, deck):

    while True:
        first_option = input("\nEnter first move (s-stand, h-hit, d-double): ").lower()
    
        if first_option == "s":
            if trace: print("player elected to stand")
            break

        if first_option == "h":
            if trace: print("player elected to hit")

            while True:

                if len(deck) == 0:
                    raise Exception("Handle later...need at least 4 cards")
            
                hit_card = deck.pop(0)
                hit_card_rank = hit_card[0]
                hand.append(hit_card)
                
                player_hand_total = total(hand)
            
                if hit_card_rank == Ace and player_hand_total > 21:
                    if trace: print("soft hand")
                    player_hand_total -= 10
        
                print("\nupdated player hand:")
                print_hand(hand)
                print(f"\nupdated player hand total: {player_hand_total}") 
        
                if player_hand_total == 21: 
                    break
        
                if player_hand_total > 21: 
                    break
        
                next_option = input("\nEnter next move (s-stand, h-hit): ").lower()
        
                if next_option == "h":
                    continue
        
                if trace: print("player elected to stand")
        
                break

        break

        if first_option == "d":
            if trace: print("player elected to double down")

            player_hand_total = total(hand)

            if len(player_hand) == 2:
                if player_hand_total == 9 or player_hand_total == 10 or player_hand_total == 11:
                    initial_bet += initial_bet
                    player_earnings -= (initial_bet/2)

                    print(f"Updated Player Bank: ${player_bank}")

                    if len(deck) == 0:
                        raise Exception("Handle later...need at least 4 cards")
            
                    hit_card = deck.pop(0)
                    hand.append(hit_card)
                        
                    player_hand_total += value(hit_card)
                
                    print("\nupdated player hand:")
                    print_hand(player_hand)
                    print(f"updated player hand total: {player_hand_total}") 
                    break

                print("> cards total NOT 9, 10, or 11...unable double")
                continue

            print("> unable double after initial move")
            continue


if __name__ == "__main__":
    play()
    
