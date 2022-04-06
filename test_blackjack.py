#! /usr/bin/env python3

import unittest
from blackjack import *
from cards import *

sample_hand = [Two_of_Spades, Four_of_Clubs, Six_of_Hearts, Eight_of_Diamonds]
sample_hand2 = [Ace_of_Spades, Jack_of_Clubs, Queen_of_Hearts, King_of_Diamonds]

natural_true = [Ace_of_Spades, Jack_of_Clubs]
natural_false = [Four_of_Clubs, Jack_of_Clubs]

dealer_deck = [King_of_Diamonds, Seven_of_Diamonds, Eight_of_Hearts, Nine_of_Clubs]
dealer_deck_below_17 = [Six_of_Spades, Three_of_Clubs, Five_of_Hearts, Seven_of_Diamonds]
dealer_deck_soft_17 = [Two_of_Hearts, Seven_of_Diamonds, Queen_of_Hearts, Three_of_Clubs]
dealer_deck_ace_11 = [Ace_of_Spades, Four_of_Clubs, Six_of_Hearts, Eight_of_Diamonds]
dealer_deck_ace_1 = [Ace_of_Spades, Jack_of_Clubs, Queen_of_Hearts, King_of_Diamonds]


dealer_below_17 = [Ace_of_Hearts, Two_of_Clubs]
dealer_above_17 = [Jack_of_Clubs, Queen_of_Hearts]
dealer_hard_17 = [King_of_Diamonds, Seven_of_Diamonds]
dealer_soft_17 = [Eight_of_Hearts, Seven_of_Diamonds]
dealer_ace_11 = [Six_of_Hearts, Two_of_Clubs]
dealer_ace_1 = [Seven_of_Hearts, Nine_of_Clubs]


dealer_blackjack_test = [Ace_of_Hearts, Two_of_Clubs, King_of_Hearts, Four_of_Diamonds, Ace_of_Spades]
dealer_ace_test = [Ace_of_Hearts, Two_of_Clubs, Nine_of_Hearts, Four_of_Diamonds, Ace_of_Spades]

player_blackjack_test = [Ace_of_Hearts, Ace_of_Clubs, Six_of_Hearts, Ten_of_Diamonds, Ace_of_Spades]
player_double_test = [Ace_of_Hearts, Six_of_Clubs, Six_of_Hearts, Ten_of_Diamonds, Ace_of_Spades]
player_split_test = [Ace_of_Hearts, Ten_of_Clubs, Six_of_Hearts, Ten_of_Diamonds, Ace_of_Spades]


class TestBlackJack(unittest.TestCase):
    
    def test_build_deck(self):
        print("testing build_deck()")
        self.assertEqual(len(build_deck()), 52)

    
    def test_print_card(self):
        print("testing print_card()")
        self.assertEqual(print_card(Ace_of_Spades), 'Ace of Spades')
        self.assertEqual(print_card(Eight_of_Hearts), '8 of Hearts')

    
    def test_print_hand(self):
        print("testing print_hand()")
        print(sample_hand)
        self.assertEqual(print_hand(sample_hand), ['2 of Spades', '4 of Clubs', '6 of Hearts', '8 of Diamonds'])
        self.assertEqual(print_hand(sample_hand2), ['Ace of Spades', 'Jack of Clubs', 'Queen of Hearts', 'King of Diamonds'])

    
    def test_get_value(self):
        print("testing get_value()")
        self.assertEqual(get_value(Ace_of_Spades), 11)
        self.assertEqual(get_value(Eight_of_Hearts), 8)


    def test_calculate_total(self):
        print("testing calculate_total()")
        self.assertEqual(calculate_total(sample_hand), 20)
        self.assertEqual(calculate_total(sample_hand2), 41)


    def test_is_natural(self):
        print("testing is_natural()")
        self.assertEqual(is_natural(natural_true), True)
        self.assertEqual(is_natural(natural_false), False)


    def test_dealers_move(self):
        print("testing dealers_move()")
        self.assertEqual(dealers_move(dealer_below_17, dealer_deck_below_17), 19)
        self.assertEqual(dealers_move(dealer_above_17, dealer_deck), 20)
        self.assertEqual(dealers_move(dealer_hard_17, dealer_deck), 17)
        self.assertEqual(dealers_move(dealer_soft_17, dealer_deck_soft_17), 17)
        self.assertEqual(dealers_move(dealer_ace_11, dealer_deck_ace_11), 19)
        self.assertEqual(dealers_move(dealer_ace_1, dealer_deck_ace_1), 17)
        

if __name__ == "__main__":
    unittest.main()

    