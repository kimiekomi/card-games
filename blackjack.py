#! /usr/bin/env python3

import random
import os

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

        if rank == "Jack":
            value = 11

        if rank == "Queen":
            value = 12

        if rank == "King":
            value = 13

    return value


if __name__ == "__main__":
    # print(build_deck())
 
    print(define_value("Ace"))
    print(define_value("3"))
    print(define_value("Jack"))

    # play_game()
