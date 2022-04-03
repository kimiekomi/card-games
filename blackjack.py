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

    if rank == 1:
        rank = "Ace"

    elif rank == 11:
        rank = "Jack"

    elif rank == 12:
        rank = "Queen"

    elif rank == 13:
        rank = "King" 

    else:
        rank = str(rank)

    if suit == 1:
        suit = "Spades"

    elif suit == 2:
        suit = "Clubs"

    elif suit == 3:
        suit = "Hearts"

    elif suit == 4:
        suit = "Diamonds"
        
    print(f"{rank} of {suit}")
    

def define_value(card):
    if debug: print("called define_value()")

    if card[0].isnumeric():
        return int(card[0])

    if card[0] == 1:
        return 11

    if card[0] == 11 or card[0] == 12 or card[0] == 13:
        return 10


def play_game():
    if debug: print(f"\ncalled play()")

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
            
        # print(f"\nPlayer Bank: ${player_bank}\n")
        
        try:
            initial_bet = int(input("Enter initial bet: $ ") or 10)

        except ValueError:
            print("> Error: Enter a valid number\n")
            continue

        player_bank -= initial_bet

        # print(f"Updated Player Bank: ${player_bank}")

        for i in range(2):
            if len(deck) > 0:
                player_hand.append(deck.pop())
                dealer_hand.append(deck.pop())

        print(f"\ncards dealt\nplayer hand: {player_hand}\ndealer hand: [ _ of _, {dealer_hand[1]}]")

        player_hand_total = 0
        for card in player_hand:
            card = card.split()
            player_hand_total += define_value(card[0])
            
        dealer_hand_total = 0
        for card in dealer_hand:
            card = card.split()
            dealer_hand_total += define_value(card[0])

        print(f"player hand total: {player_hand_total}") 
        if trace: print(f"dealer hand total: {dealer_hand_total}")
        print(f"dealer card2 value: {define_value(dealer_hand[1].split()[0])}") 

        if define_value(dealer_hand[1].split()[0]) == 11:
            want_insurance = input("Do you want insurance? ").lower()

            while True: 
                if want_insurance == "y":
                    if trace: print("player wants insurance")
                    
                    while True:
                        print(f"initial bet: ${initial_bet}")
                        insurance_bet = int(input("Enter insurance amount: "))
                
                        if insurance_bet <= (initial_bet/2):
                            break
                            
                        if insurance_bet > (initial_bet/2):
                            print("> may only bet up to HALF the initial bet")
                            continue
                        
                    if is_natural(player_cards, dealer_cards, player_bank, initial_bet):
                        player_bank += ((insurance_bet * 2) + insurance_bet)
                        player_bank -= initial_bet
                        break
    
                    player_bank -= insurance_bet
                    break

                break

        if define_value(dealer_hand[1].split()[0]) == 10 or define_value(dealer_hand[1].split()[0]) == 11 and dealer_hand_total == 21:
            is_natural(player_hand, dealer_hand, deck, player_bank, initial_bet)
            break
        
        player_options(player_hand, dealer_hand, deck, player_bank, initial_bet)
        
        another_round = input("\nAnother Round? ").lower()

        if another_round[0] != "y":
            print("\n>>> Goodbye...\n")
            break

        os.system("clear")


def player_options(player_cards, dealer_cards, card_deck, player_bank, initial_bet):
    if debug: print("called player_options()")

    # if trace: print(player_cards)

    player_card1_rank = player_cards[0].split()[0]
    player_card2_rank = player_cards[1].split()[0]

    # if trace: print(player_card1_rank, player_card2_rank)

    if define_value(player_card1_rank) + define_value(player_card2_rank) == 21:
        is_natural(player_cards, dealer_cards, card_deck, player_bank, initial_bet)
        return

    if define_value(player_card1_rank) + define_value(player_card2_rank) == 21:
        double(player_cards, dealer_cards, card_deck, player_bank, initial_bet)

    while True:
        first_option = input("\nEnter first move (t-stand, h-hit, d-double): ").lower()
    
        if first_option == "t":
            if trace: print("player elected to stand")
                
            updated_dealer_cards = dealers_move(dealer_cards, card_deck)
            define_winner(player_cards, updated_dealer_cards, player_bank, initial_bet)
            break

        if first_option == "h":
            if trace: print("player elected to hit")

            hit_loop(player_cards, dealer_cards, card_deck, player_bank, initial_bet)
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

            if define_value(player_card1_rank) + define_value(player_card2_rank) == 9 or define_value(player_card1_rank) + define_value(player_card2_rank) == 10 or define_value(player_card1_rank) + define_value(player_card2_rank) == 11:
                double(player_cards, dealer_cards, card_deck, player_bank, initial_bet)
                break

            print("> cards total NOT 9, 10, or 11...unable double")
            continue

        # elif first_option != "t" and first_option != "s" and first_option != "d" and first_option != "h":
        #     if trace: print("player elected to surrender")
                
        #     self.surrender()
        #     break

    return player_bank

def hit_loop(player_cards, dealer_cards, card_deck, player_bank, initial_bet):
    if debug: print("called hit_loop()")
        
    while True:
        player_hand_total = calculate_total(player_cards)

        hit_card = card_deck.pop()
        player_cards.append(hit_card)
        
        player_hand_total += define_value(hit_card.split()[0])
    
        if hit_card.split()[0] == "Ace" and player_hand_total > 21:
            if trace: print("soft hand")
            player_hand_total -= 10

        print(f"updated player hand: {player_cards}")
        print(f"updated player hand total: {player_hand_total}") 
        print(f"dealer card1 value: {define_value(dealer_cards[1].split()[0])}") 

        if player_hand_total == 21: 
            dealers_move(dealer_cards, card_deck)
            define_winner(player_cards, dealer_cards, player_bank, initial_bet)
            break

        if player_hand_total > 21: 
            define_winner(player_cards, dealer_cards, player_bank, initial_bet)
            break

        next_option = input("\nEnter next move (t - stand, h - hit): ").lower()

        if next_option == "h":
            continue

        if trace: print("player elected to stand")

        dealers_move(dealer_cards, card_deck)
        define_winner(player_cards, dealer_cards, player_bank, initial_bet)
        break
        

# def split(self):
#     if debug: print("called split()")

#     split1 = []
#     split2 = []

#     split1.append(self.player_hand[0])
#     split2.append(self.player_hand[1])


def double(player_cards, dealer_cards, card_deck, player_bank, initial_bet):
    if debug: print("called double()")
        
    initial_bet += initial_bet
    player_bank -= (initial_bet/2)

    print(f"Updated Player Bank: ${player_bank}")

    player_hand_total = calculate_total(player_cards)

    hit_card = card_deck.pop()
    player_cards.append(hit_card)
        
    player_hand_total += define_value(hit_card.split()[0])

    print(f"updated player hand: {player_cards}")
    print(f"updated player hand total: {player_hand_total}") 

    dealers_move(dealer_cards, card_deck)
    define_winner(player_cards, dealer_cards, player_bank, initial_bet)


# def surrender(self):
#     pass


def calculate_total(cards_list):
    if debug: print("called calculate_total()")

    total = 0

    for card in cards_list:
       total += define_value(str(card.split()[0]))

    return total


def is_natural(player_cards, dealer_cards, player_bank, initial_bet):
    if debug: print("called is_natural()")

    player_hand_total = define_value(player_cards[0].split()[0]) + define_value(player_cards[1].split()[0])
    dealer_hand_total = define_value(dealer_cards[0].split()[0]) + define_value(dealer_cards[1].split()[0])

    if player_hand_total == 21 and dealer_hand_total != 21:
        print("\n>>> Player has Natural...You Win")
        player_bank += initial_bet * 2.5
        return 

    if dealer_hand_total == 21 and player_hand_total != 21:
        print("\n>>> Dealer has Natural...You Lose")
        return True

    if player_hand_total == 21 and dealer_hand_total == 21:
        print("\n>>> Both have Natural...Its a Draw")
        player_bank += initial_bet
        return False


def dealers_move(dealer_cards, deck_of_cards):
    if debug: print("called dealers_move()")

    print(f"dealer hand revealed: {dealer_cards}")

    dealer_hand_total = calculate_total(dealer_cards)
         
    while dealer_hand_total < 17:
        dealer_card = deck_of_cards.pop()
        dealer_cards.append(dealer_card)
        dealer_hand_total += define_value(dealer_card.split()[0])
        
        if dealer_card.split()[0] == "Ace" and dealer_hand_total >= 17:
            break

    print(f"updated dealer hand: {dealer_cards}")
    print(f"updated dealer hand total: {dealer_hand_total}")

    return dealer_cards

    
def define_winner(player_cards, dealer_cards, player_bank, initial_bet):
    if debug: print("called define_winner()")

    print(f"initial bet: {initial_bet}")

    player_hand_total = calculate_total(player_cards)
    dealer_hand_total = calculate_total(dealer_cards)

    if player_hand_total > 21:
        print("\n>>> Player Bust...You Lose")
        print(f">>> Updated Player Bank: ${player_bank}")
        
        return

    if dealer_hand_total > 21:
        print("\n>>> Dealer Bust...You Win")
        player_bank += initial_bet * 2
        print(f">>> Updated Player Bank: ${player_bank}")
        
        return
        
    if player_hand_total == 21 and dealer_hand_total != 21:
        print("\n>>> Player has Blackjack...You Win")
        player_bank += initial_bet * 2
        print(f">>> Updated Player Bank: ${player_bank}")
        
        return

    if dealer_hand_total == 21 and player_hand_total != 21:
        print("\n>>> Dealer has Blackjack...You Lose")
        print(f">>> Updated Player Bank: ${player_bank}")
        
        return
        
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("\n>>> Both have Blackjack")
        player_bank += initial_bet
        print(f">>> Updated Player Bank: ${player_bank}")
        
        return
        
    if player_hand_total < 21 and dealer_hand_total < 21:
        if player_hand_total > dealer_hand_total:
            print("\n>>> You are closer to 21...You Win")
            player_bank += initial_bet * 2
        
        elif player_hand_total == dealer_hand_total:
            print("\n>>> Equal Value...Its a Draw")
            player_bank += initial_bet

        else:
            player_hand_total < dealer_hand_total
            print("\n>>> Dealer is closer to 21...You Lose") 

        print(f">>> Updated Player Bank: ${player_bank}")

        return player_bank


if __name__ == "__main__":
    # print(build_deck())

    print_card((7,4))
    print_card((1,2))
    print_card((11,1))
 
    # print(define_value("Ace"))
    # print(define_value("3"))
    # print(define_value("Jack"))

    # play_game()
