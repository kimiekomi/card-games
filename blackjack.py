#! /usr/bin/env python3

import random
import os

debug = False
trace = True

Ace = 1
Jack = 11
Queen = 12
King = 13

Spades = 1
Clubs = 2
Hearts = 3
Diamonds = 4


def build_deck():
    if debug: print("called deck()")

    suits = [Spades, Clubs, Hearts, Diamonds]        
    ranks = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]

    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append((rank, suit))

    random.shuffle(deck)

    return deck


def print_card(card):
    if debug: print("called print_card()")

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
        
    return f"{rank} of {suit}"


def print_hand(hand):
    if debug: print("called print_hand()")

    for card in hand:
        print(print_card(card))
        
        
def define_value(card):
    if debug: print("called define_value()")

    if card[0] == Ace:
        return 11

    if card[0] == Jack or card[0] == Queen or card[0] == King:
        return 10

    return card[0]


def calculate_total(cards_list):
    if debug: print("called calculate_total()")

    total = 0

    for card in cards_list:
       total += define_value(card)

    return total


def is_natural(hand):
    if debug: print("called is_natural()")

    hand_total = define_value(hand[0]) + define_value(hand[1])

    return hand_total == 21


def dealers_move(hand, card_deck):
    if debug: print("called dealers_move()")

    print(f"dealer hand revealed:")
    print_hand(hand)
    
    dealer_hand_total = calculate_total(hand)
         
    while dealer_hand_total < 17:
        dealer_card = hand.pop()
        hand.append(dealer_card)
        dealer_hand_total += define_value(dealer_card)
        
        if hand[0] == 1 and dealer_hand_total >= 17:
            break

    if len(hand) > 2:
        print(f"updated dealer hand:")
        print_hand(hand)
    
    print(f"updated dealer hand total: {dealer_hand_total}")

    return dealer_hand_total


def play_game():
    if debug: print(f"\ncalled play_game()")

    initial_bet = 0
    player_bank = 0

    deck = build_deck()

    # burn card
    deck.pop()

    # if trace: print(f"\ngame deck({len(deck)}): {deck}")

    while True:
        player_hand = []
        dealer_hand = []

        player_hand_total = 0
        dealer_hand_total = 0

        if trace: print(f"\nplayer hand({len(player_hand)}), dealer hand({len(dealer_hand)})\nplayer total: {player_hand_total}, dealer total: {dealer_hand_total}")
            
        print(f"\nPlayer Bank: ${player_bank}\n")
        
        try:
            initial_bet = int(input("Enter initial bet: $ ") or 10)

        except ValueError:
            print("> Error: Enter a valid number\n")
            continue

        print(f"Updated Player Bank: ${player_bank}")

        for i in range(2):
            if len(deck) > 0:
                player_hand.append(deck.pop())
                dealer_hand.append(deck.pop())

        print(f"\nplayer hand: {print_card(player_hand[0])}, {print_card(player_hand[1])}")
        print(f"dealer hand: ___ of ___ , {print_card(dealer_hand[1])}")
        
        player_hand_total = 0
        for card in player_hand:
            player_hand_total += define_value(card)
            
        dealer_hand_total = 0
        for card in dealer_hand:
            dealer_hand_total += define_value(card)

        print(f"\nplayer hand total: {player_hand_total}") 
        if trace: print(f"dealer hand total: {dealer_hand_total}")
        print(f"dealer card2 value: {define_value(dealer_hand[1])}") 

        if define_value(dealer_hand[1]) == 11:
            want_insurance = input("\nDo you want insurance? ").lower()

            if want_insurance == "y":
                if trace: print("player wants insurance")
                
                while True:
                    print(f"initial bet: ${initial_bet}")
                    try:
                        insurance_bet = int(input("\nEnter insurance amount: $"))
                
                        if insurance_bet > (initial_bet/2):
                            print("> may only bet up to HALF the initial bet")
                            continue

                    except:
                        print("Enter a valid number")
                        continue

                    break

                print(f"dealer hand revealed: {print_hand(hand)}")
                    
                if is_natural(dealer_hand):
                    player_bank += ((insurance_bet * 2) + insurance_bet)
                    player_bank -= initial_bet
                    print("You win insurance bet")

                else:
                    print("You lose insurance bet")
                    player_bank -= insurance_bet

                print(f"Updated Player Bank: ${player_bank}")
                
        if define_value(dealer_hand[1]) >= 10 and dealer_hand_total == 21:
            print(f"dealer hand revealed: {print_hand(dealer_hand)}")
            
            if not is_natural(player_hand):
                print("\n>>> Dealer has Natural...You Lose")

            print("\n>>> Both have Natural...Its a Draw")
            player_bank += initial_bet

        if player_hand_total == 21:
            if not is_natural(dealer_hand):
                player_bank += initial_bet * 2.5

            else:
                player_bank += initial_bet

        else:
            while True:
                first_option = input("\nEnter first move (s-stand, h-hit, d-double): ").lower()
            
                if first_option == "s":
                    if trace: print("player elected to stand")
                        
                    dealer_hand_total = dealers_move(dealer_hand, deck)
                    break
        
                if first_option == "h":
                    if trace: print("player elected to hit")
    
                    while True:
                
                        hit_card = deck.pop()
                        player_hand.append(hit_card)
                        
                        player_hand_total += define_value(hit_card)
                    
                        if hit_card[0] == 1 and player_hand_total > 21:
                            if trace: print("soft hand")
                            player_hand_total -= 10
                
                        print(f"updated player hand:")
                        print_hand(player_hand)
                        print(f"\nupdated player hand total: {player_hand_total}") 
                        print(f"dealer card1 value: {define_value(dealer_hand[1])}") 
                
                        if player_hand_total == 21: 
                            dealers_move(dealer_hand, deck)
                            break
                
                        if player_hand_total > 21: 
                            break
                
                        next_option = input("\nEnter next move (s-stand, h-hit): ").lower()
                
                        if next_option == "h":
                            continue
                
                        if trace: print("player elected to stand")
                
                        dealers_move(dealer_hand, deck)
                        break
    
                    break
        
                # if first_option == "s":
                #     if trace: print("player elected to split pair")
            
                #     if self.player.hand[0].rank == self.player.hand[1].rank:
                #         self.split()
                #         break
            
                #     print("> equal rank cards...unable split")
                #     continue
            
                if first_option == "d":
                    if trace: print("player elected to double down")
        
                    if define_value(player_hand[0]) + define_value(player_hand[1]) == 9 or define_value(player_hand[0]) + define_value(player_hand[1]) == 10 or define_value(player_hand[0]) + define_value(player_hand[1]) == 11:
                        initial_bet += initial_bet
                        player_bank -= (initial_bet/2)
    
                        print(f"Updated Player Bank: ${player_bank}")
    
                        hit_card = deck.pop()
                        player_hand.append(hit_card)
                            
                        player_hand_total += define_value(hit_card)
                    
                        print(f"updated player hand:")
                        print_hand(player_hand)
                        print(f"updated player hand total: {player_hand_total}") 
                    
                        dealers_hand_total = dealers_move(dealer_hand, deck)
                        
                        break
        
                    print("> cards total NOT 9, 10, or 11...unable double")
                    continue
        
                # elif first_option != "t" and first_option != "s" and first_option != "d" and first_option != "h":
                #     if trace: print("player elected to surrender")
                        
                #     self.surrender()
                #     break

        # game over logic
        if player_hand_total > 21:
            print("\n>>> Player Bust...You Lose")
            player_bank -= initial_bet

        elif dealer_hand_total > 21:
            print("\n>>> Dealer Bust...You Win")
            player_bank += initial_bet * 2
            
        elif player_hand_total == 21 and dealer_hand_total != 21:
            print("\n>>> Player has Blackjack...You Win")
            player_bank += initial_bet * 2
            
        elif dealer_hand_total == 21 and player_hand_total != 21:
            print("\n>>> Dealer has Blackjack...You Lose")
            player_bank -= initial_bet
            
        elif player_hand_total == 21 and dealer_hand_total == 21:
            print("\n>>> Both have Blackjack")
            player_bank += initial_bet
            
        elif player_hand_total < 21 and dealer_hand_total < 21:
            if player_hand_total > dealer_hand_total:
                print("\n>>> You are closer to 21...You Win")
                player_bank += initial_bet * 2
            
            elif player_hand_total == dealer_hand_total:
                print("\n>>> Equal Value...Its a Draw")
                player_bank += initial_bet
    
            else:
                player_hand_total < dealer_hand_total
                print("\n>>> Dealer is closer to 21...You Lose") 
                player_bank -= initial_bet

        print(f">>> Updated Player Bank: ${player_bank}")
        
        another_round = input("\nAnother Round? ").lower()

        if another_round[0] != "y":
            print("\n>>> Goodbye...\n")
            break

        os.system("clear")


# def split(self):
#     if debug: print("called split()")

#     split1 = []
#     split2 = []

#     split1.append(self.player_hand[0])
#     split2.append(self.player_hand[1])


# def surrender(self):
#     pass


if __name__ == "__main__":
    print(build_deck())

    # print_card((7,4))
    # print_card((1,2))
    # print_card((11,1))
 
    # print(define_value((7,4)))
    # print(define_value((1,2)))
    # print(define_value((11,1)))

    # play_game()
