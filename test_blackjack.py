#! /usr/bin/env python3

from blackjack import *
from cards import *


insurance_dealer_blackjack = [Ace_of_Hearts, Seven_of_Hearts, Jack_of_Clubs, Six_of_Diamonds, Ace_of_Spades]
insurance_neither_blackjack = [Ace_of_Hearts, Seven_of_Hearts, Four_of_Clubs, Six_of_Diamonds, Ace_of_Spades]
insurance_player_blackjack = [Ace_of_Hearts, Ten_of_Hearts, Seven_of_Clubs, Ace_of_Diamonds, Ace_of_Spades]
insurance_both_blackjack = [Ace_of_Hearts, Queen_of_Hearts, Jack_of_Clubs, Ace_of_Diamonds, Ace_of_Spades]

dealer_ten_blackjack_player_lose = [Ace_of_Hearts, Seven_of_Hearts, Ace_of_Clubs, Six_of_Diamonds, Ten_of_Spades]
dealer_ten_blackjack_draw = [Ace_of_Hearts, Ace_of_Diamonds, Ace_of_Clubs, Queen_of_Diamonds, Ten_of_Spades]

player_blackjack_dealer_17 = [Ace_of_Hearts, Queen_of_Hearts, Seven_of_Clubs, Ace_of_Diamonds, Ten_of_Spades]
player_blackjack_dealer_below_17 = [Ace_of_Hearts, Queen_of_Hearts, Two_of_Clubs, Ace_of_Diamonds, Ten_of_Spades, Five_of_Hearts]
both_blackjack = [Ace_of_Hearts, Queen_of_Hearts, Ace_of_Clubs, Ace_of_Diamonds, Ten_of_Spades, Jack_of_Hearts]

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
    ("insurance neither blackjack", insurance_neither_blackjack),
    ("insurance player blackjack", insurance_player_blackjack),
    ("insurance both blackjack", insurance_both_blackjack),
    ("dealer ten blackjack player lose", dealer_ten_blackjack_player_lose),
    ("dealer ten blackjack draw", dealer_ten_blackjack_draw),
    ("player blackjack dealer 17", player_blackjack_dealer_17),
    ("player blackjack dealer below 17", player_blackjack_dealer_below_17),
    ("both blackjack", both_blackjack),
    ("player hit soft hand 21", player_hit_soft_hand_21),
    ("player hit reg ace 21", player_hit_reg_ace_21),
    ("player hit no ace 21", player_hit_no_ace_21),
    ("player hit bust", player_hit_bust),
    ("player hit twice bust", player_hit_twice_bust),
    ("player hit hit stand dealer win", player_hit_hit_stand_dealer_win),
    ("player hit stand player win", player_hit_stand_player_win),
    ("player stand dealer bust", player_stand_dealer_bust),
    ("double player bust", double_player_bust),
    ("double dealer bust", double_dealer_bust),
    ("double player win", double_player_win),
    ("double player lose", double_player_lose),
]


if __name__ == "__main__":
    for i, test in enumerate(Tests):
        print(f"{i+1} - {test[0]}")
              
    test = input("\nEnter a test: ")
    
    play(Tests[test][1])
    # fix double down...

