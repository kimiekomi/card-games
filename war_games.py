#! /usr/bin/env python3

import random

debug = False
trace = True

def build_deck():
    if debug: print("called deck()")

    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]        
    ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")

    # if trace: print(f"deck({len(deck)}): {deck}")

    random.shuffle(deck)

    return deck


def deal_cards():
    if debug: print("called deal()")

    deck = build_deck()

    player_deck = []
    computer_deck = []
    cards_on_table = []

    while len(deck) > 0:
        player_deck.insert(0, deck.pop())
        computer_deck.insert(0, deck.pop())

    # if trace: print(f"\nplayer deck({len(player_deck)}): {player_deck}")
    # if trace: print(f"\ncomputer deck({len(computer_deck)}): {computer_deck}")

    return player_deck, computer_deck, cards_on_table


def play_game():
    if debug: print("called play_game()")

    player_deck = deal_cards()[0]
    computer_deck = deal_cards()[1]
    cards_on_table = deal_cards()[2]

    if trace: print(f"player deck({len(player_deck)}), computer deck({len(computer_deck)}), cards on table({len(cards_on_table)})")
    
    while len(player_deck) != 0 and len(computer_deck) != 0:
        if trace: print("\ngame_loop")
        if trace: print(f"cards on table({len(cards_on_table)}): {cards_on_table}")
        
        player_battle_card = player_deck.pop()
        cards_on_table.append(player_battle_card)

        computer_battle_card = computer_deck.pop()
        cards_on_table.append(computer_battle_card)

        if trace: print(f"player card: {player_battle_card}\ncomputer card: {computer_battle_card}")

        if player_battle_card == computer_battle_card:
            if trace: print("*** time for war ***")
                
            lets_war(player_deck, computer_deck, cards_on_table)
            continue

        if trace: print("*** time for battle ***")

        lets_battle(player_battle_card, computer_battle_card)

        if lets_battle:
            for card in cards_on_table:
                player_deck.insert(0, card)

        else:
            for card in cards_on_table:
                computer_deck.insert(0, card)

        cards_on_table = []
    
        if trace: print(f"table cleared: {len(cards_on_table)} cards on table")

        print(f"player score: {len(player_deck)}, computer score: {len(computer_deck)}")
    
        if trace: print(f"\nplayer deck({len(player_deck)}): {player_deck}\n\ncomputer deck({len(computer_deck)}): {computer_deck}")

    # Game has ended
    if len(player_deck) == 0:
        print("player deck empty\n\n>>> Game Over...Computer Won War\n")

    else:
        print("computer deck empty\n\n>>> Game Over...Player Won War\n")

    
def lets_war(player_deck, computer_deck, cards_on_table):

    if debug: print("lets_war()")

    for i in range(3):
        
        if len(player_deck) != 0 and len(computer_deck) != 0:
            cards_on_table.append(player_deck.pop())
            cards_on_table.append(computer_deck.pop())

    if trace: print(f"cards on table({len(cards_on_table)}): {cards_on_table}")

    
def lets_battle(player_card, computer_card):

    if debug: print("lets_battle()")

    if player_card > computer_card:
        print("<player card is higher>")
        return True

    print("<computer card is higher>")
    return False
        

if __name__ == "__main__":
    # print(build_deck())
    
    # print(f"player deck: {deal_cards()[0]}\n")
    # print(f"computer deck: {deal_cards()[1]}\n")
    # print(f"cards on table: {deal_cards()[2]}")

    play_game()

