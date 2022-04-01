#! /usr/bin/env python3

debug = True
trace = True

def deal():
    if debug: print("called game()")

    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]        
    ranks = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

    deck = []
    
    for suit in suits:
        for rank in ranks:
            deck.append(f"{rank} of {suit}")

    if trace: print(f"deck: {deck}")

    player_deck = []
    computer_deck = []
    cards_on_table = []

    while len(deck) > 0:
        player_deck.insert(0, deck.pop())
        computer_deck.insert(0, deck.pop())

    if trace: print(f"\nplayer deck({len(player_deck)}): {player_deck}")
    
    if trace: print(f"\ncomputer deck({len(computer_deck)}): {computer_deck}")


def play():
    if debug: print("called play()")

    while len(player_deck) != 0 and len(computer_deck) != 0:
        if trace: print("\ngame_loop")

        if trace: print(f"cards on table({len(cards_on_table)}): {self.cards_on_table}")
        
        player_battle_card = player_deck.pop()
        cards_on_table.append(player_battle_card)

        computer_battle_card = computer_deck.pop()
        cards_on_table.append(computer_battle_card)

        if trace: print(f"player card: {player_battle_card}\ncomputer card: {computer_battle_card}")

        if player_battle_card == computer_battle_card:
            if trace: print("*** time for war ***")
                
            lets_war()
            continue

        if trace: print("*** time for battle ***")

        lets_battle(player_battle_card, computer_battle_card)

        print(f"player score: {len(self.player_deck)}, computer score: {len(self.computer_deck)}")
    
        if trace: print(f"\nplayer deck({len(self.player_deck)}): {self.player_deck}\n\ncomputer deck({len(self.computer_deck)}): {self.computer_deck}")


    # Game has ended
    if len(self.player_deck) == 0:
        print("player deck empty\n\n>>> Game Over...Computer Won War\n")

    else:
        print("computer deck empty\n\n>>> Game Over...Player Won War\n")

    
# def lets_war(self):

#     if debug: print("lets_war()")

#     for i in range(3):
        
#         if len(self.player_deck) != 0 and len(self.computer_deck) != 0:
#             self.cards_on_table.append(self.player_deck.pop())
#             self.cards_on_table.append(self.computer_deck.pop())

#     if trace: print(f"cards on table({len(self.cards_on_table)}): {self.cards_on_table}")

    
# def lets_battle(self, player_card, computer_card):

#     if debug: print("lets_battle()")

#     if player_card > computer_card:
#         print("<player card is higher>")

#         for card in self.cards_on_table:
#             self.player_deck.insert(0, card)

#     else:
#         print("<computer card is higher>")
        
#         for card in self.cards_on_table:
#             self.computer_deck.insert(0, card)

#     self.cards_on_table = []
    
#     if trace: print(f"table cleared: {len(self.cards_on_table)} cards on table")


if __name__ == "__main__":
    game()

