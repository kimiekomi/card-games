#! /usr/bin/env python3

from blackjack import *
from cards import *


insurance_dealer_blackjack = [Ace_of_Hearts, Seven_of_Hearts, Jack_of_Clubs, Six_of_Diamonds, Ace_of_Spades]
insurance_neither_blackjack = [Ace_of_Hearts, Seven_of_Hearts, Four_of_Clubs, Six_of_Diamonds, Ace_of_Spades]
insurance_player_blackjack = [Ace_of_Hearts, Ten_of_Hearts, Seven_of_Clubs, Ace_of_Diamonds, Ace_of_Spades]
insurance_both_blackjack = [Ace_of_Hearts, Queen_of_Hearts, Jack_of_Clubs, Ace_of_Diamonds, Ace_of_Spades]

dealer_ten_natural_player_lose = [Ace_of_Hearts, Seven_of_Hearts, Ace_of_Clubs, Six_of_Diamonds, Ten_of_Spades]
dealer_ten_natural_draw = [Ace_of_Hearts, Ace_of_Diamonds, Ace_of_Clubs, Queen_of_Diamonds, Ten_of_Spades]

player_natural_dealer_17 = [Ace_of_Hearts, Queen_of_Hearts, Seven_of_Clubs, Ace_of_Diamonds, Ten_of_Spades]
player_natural_dealer_below_17 = [Ace_of_Hearts, Queen_of_Hearts, Two_of_Clubs, Ace_of_Diamonds, Ten_of_Spades, Five_of_Hearts]
both_natural = [Ace_of_Hearts, Queen_of_Hearts, Ace_of_Clubs, Ace_of_Diamonds, Ten_of_Spades, Jack_of_Hearts]

player_hit_soft_hand_21 = [Ace_of_Hearts, Seven_of_Spades, Nine_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Ace_of_Diamonds, Seven_of_Hearts]
player_hit_reg_ace_21 = [Ace_of_Hearts, Seven_of_Spades, Nine_of_Clubs, Three_of_Diamonds, Eight_of_Hearts, Ace_of_Diamonds, Seven_of_Hearts]
player_hit_no_ace_21 = [Ace_of_Hearts, Seven_of_Spades, Ten_of_Clubs, Five_of_Diamonds, Eight_of_Hearts, Nine_of_Diamonds]
player_hit_bust = [Ace_of_Hearts, Eight_of_Spades, Four_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Ten_of_Diamonds]
player_hit_twice_bust = [Ace_of_Hearts, Eight_of_Spades, Four_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Two_of_Diamonds, Nine_of_Spades]
player_hit_hit_stand_dealer_win = [Ace_of_Hearts, Five_of_Spades, Ten_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Five_of_Diamonds]
player_hit_stand_player_win = [Ace_of_Hearts, Five_of_Spades, Ten_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Nine_of_Diamonds]
player_stand_dealer_bust = [Ace_of_Hearts, Ten_of_Spades, Six_of_Clubs, Ten_of_Diamonds, Eight_of_Hearts, Nine_of_Diamonds]


double_player_bust = [Ace_of_Hearts, Six_of_Spades, Four_of_Clubs, Five_of_Diamonds, Eight_of_Hearts, Ten_of_Diamonds, Five_of_Clubs]
double_dealer_bust = [Ace_of_Hearts, Six_of_Spades, Four_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Eight_of_Diamonds, Ten_of_Diamonds]
double_player_win = [Ace_of_Hearts, Six_of_Spades, Four_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Eight_of_Diamonds, Five_of_Diamonds]
double_player_lose = [Ace_of_Hearts, Six_of_Spades, Four_of_Clubs, Six_of_Diamonds, Eight_of_Hearts, Five_of_Diamonds, Eight_of_Diamonds]

Tests = [
    ("insurance dealer blackjack", insurance_dealer_blackjack),
    ("insurance neither blackjack", insurance_neither_blackjack)
    
]


if __name__ == "__main__":
    play_game(insurance_dealer_blackjack)
    # fix double down...

