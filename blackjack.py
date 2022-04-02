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
        
        if suit == Spades:
            suit = "Spades"

        elif suit == Clubs:
            suit = "Clubs"
    
        elif suit == Hearts:
            suit = "Hearts"
    
        elif suit == Diamonds:
            suit = "Diamonds"
        
        for rank in ranks:
            
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
            
            deck.append(f"{rank} of {suit}")

    random.shuffle(deck)

    return deck


def define_value(rank):
    if debug: print("called define_value()")

    value = 0

    if rank.isnumeric():
        value = int(rank)

    else:
        if rank == "Ace":
            value = 1

        if rank == "Jack" or rank == "Queen" or rank == "King":
            value = 10

    return value


def play_game():
    if debug: print(f"\ncalled play()")

    initial_bet = 0
    player_bank = 0

    deck = build_deck()

    # burn card
    deck.pop()

    if trace: print(f"\ngame deck({len(deck)}): {deck}")

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

        player_bank -= initial_bet

        print(f"Updated Player Bank: ${player_bank}")

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
        print(f"dealer card2 value: {define_value(dealer_hand[1][0])}") 

        player_options(player_hand, dealer_hand, deck)
        
        print(f">>> Updated Player Bank: ${player_bank}")

        another_round = input("\nAnother Round? ").lower()

        if another_round[0] != "y":
            print("\n>>> Goodbye...\n")
            break

        os.system("clear")


def player_options(player_cards, dealer_cards, card_deck):
    if debug: print("called player_options()")

    if trace: print(player_cards)

    player_card1_rank = player_cards[0].split()[0]
    player_card2_rank = player_cards[1].split()[0]

    if trace: print(player_card1_rank, player_card2_rank)

    if define_value(player_card1_rank) + define_value(player_card2_rank) == 21:
        is_natural(player_cards, dealer_cards)
        return

    while True:
        first_option = input("\nEnter first move: ").lower()
    
        if first_option == "t":
            if trace: print("player elected to stand")
                
            updated_dealer_cards = dealers_move(dealer_cards, card_deck)
            define_winner(player_cards, updated_dealer_cards)
            break

        # elif first_option == "h":
        #     if trace: print("player elected to hit")
                
        #     self.hit_loop()
        #     break
    
        # elif first_option == "s":
        #     if trace: print("player elected to split pair")
    
        #     if self.player.hand[0].rank == self.player.hand[1].rank:
        #         self.split()
        #         break
    
        #     print("> equal rank cards...unable split")
        #     continue
    
        # elif first_option == "d":
        #     if trace: print("player elected to double down")

        #     if self.player.hand[0].value + self.player.hand[0].value == 9 or self.player.hand[0].value + self.player.hand[0].value == 10 or self.player.hand[0].value + self.player.hand[0].value == 11:
        #         self.double()
        #         break

        #     print("> cards total not 9, 10, or 11...unable double")
        #     continue
    
        # elif first_option != "t" and first_option != "s" and first_option != "d" and first_option != "h":
        #     if trace: print("player elected to surrender")
                
        #     self.surrender()
        #     break
    

# def hit_loop(self):
#     if debug: print("called hit_loop()")
        
#     while True:
#         self.player.hit()

#         self.player_hand_total += self.player.hit_card.value

#         print(f"updated player hand: {self.player.hand}")
#         print(f"updated player hand total: {self.player_hand_total}") 
#         print(f"dealer card1 value: {self.dealer.hand[1].value}") 

#         if self.player_hand_total >= 21: 
#             self.define_winner()
#             break

#         next_option = input("\nEnter next move: ").lower()

#         if next_option == "h":
#             continue

#         if trace: print("player elected to stand")

#         self.dealers_move()
#         self.define_winner()
#         break
        

# def hit(self):
#     if debug: print("called hit()")

#     hit_card = self.deck.get_card()
#     self.player_hand.append(hit_card)
#     self.player_hand_total += hit_card.value

#     if hit_card.rank == Ace and self.player_hand_total > 21:
#         self.player_hand_total -= 10

#     print(f"updated player hand: {self.player_hand}")
#     print(f"updated player hand total: {self.player_hand_total}") 
#     print(f"dealer card1 value: {self.dealer_hand[0].value}") 

    
# def split(self):
#     if debug: print("called split()")

#     split1 = []
#     split2 = []

#     split1.append(self.player_hand[0])
#     split2.append(self.player_hand[1])


# def double(self):
#     if debug: print("called double()")
        
#     self.initial_bet += self.initial_bet
#     self.player_bank -= (self.initial_bet/2)

#     print(f"Updated Player Bank: ${self.player_bank}")

#     self.player.hit()
#     self.define_winner()


# def insurance(self):
#     pass


# def surrender(self):
#     pass


def calculate_total(cards_list):
    if debug: print("called calculate_total()")

    total = 0

    for card in cards_list:
       total += define_value(card[0]) 

    return total


def is_natural(player_cards, dealer_cards):
    if debug: print("called is_natural()")

    updated_dealer_cards = dealers_move(dealer_cards)

    player_hand_total = define_value(player_cards[0][0]) + define_value(player_cards[1][0])
    dealer_hand_total = calculate_total(updated_dealer_cards)

    if player_hand_total == 21 and dealer_hand_total != 21:
        print("\n>>> Player has Natural...You Win")
        player_bank += self.initial_bet * 2.5
        return

    if dealer_hand_total == 21 and player_hand_total != 21:
        print("\n>>> Dealer has Natural...You Lose")
        return

    if player_hand_total == 21 and dealer_hand_total == 21:
        print("\n>>> Both have Natural...Its a Draw")
        player_bank += initial_bet
        return

    define_winner()


def dealers_move(dealer_cards, deck_of_cards):
    if debug: print("called dealers_move()")

    print(f"dealer hand revealed: {dealer_cards}")

    dealer_hand_total = calculate_total(dealer_cards)
         
    while dealer_hand_total < 17:
        dealer_card = deck_of_cards.pop()
        dealer_cards.append(dealer_card)
        dealer_hand_total += define_value(dealer_card[0])
        
        if dealer_card[0] == "Ace" and dealer_hand_total >= 17:
            break

    return dealer_cards

    print(f"updated dealer hand: {dealer_hand}")
    print(f"updated dealer hand total: {dealer_hand_total}")

    
def define_winner(player_cards, dealer_cards):
    if debug: print("called define_winner()")

    player_hand_total = calculate_total(player_cards)
    dealer_hand_total = calculate_total(dealer_cards)

    if player_hand_total > 21:
        print("\n>>> Player Bust...You Lose")
        return

    if dealer_hand_total > 21:
        print("\n>>> Dealer Bust...You Win")
        self.player_bank += self.initial_bet * 2
        return
        
    if player_hand_total == 21 and dealer_hand_total != 21:
        print("\n>>> Player has Blackjack...You Win")
        player_bank += self.initial_bet * 2
        return

    if dealer_hand_total == 21 and player_hand_total != 21:
        print("\n>>> Dealer has Blackjack...You Lose")
        return
        
    if player_hand_total == 21 and dealer_hand_total == 21:
        print("\n>>> Both have Blackjack")
        player_bank += initial_bet
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

        return


if __name__ == "__main__":
    # print(build_deck())
 
    # print(define_value("Ace"))
    # print(define_value("3"))
    # print(define_value("Jack"))

    play_game()
