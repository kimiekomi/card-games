#! /usr/bin/env python3

import unittest

from blackjack import *
from cards import *

sample_hand1 = [Two_of_Spades, Four_of_Clubs, Six_of_Hearts, Eight_of_Diamonds]
sample_hand2 = [Ace_of_Spades, Jack_of_Clubs, Queen_of_Hearts, King_of_Diamonds]
sample_hand3 = [Ace_of_Spades, Five_of_Clubs, Six_of_Hearts, Nine_of_Diamonds]

sample_hand4 = [Ace_of_Spades, Four_of_Diamonds, Six_of_Hearts]
sample_hand5 = [Four_of_Diamonds, Ace_of_Spades, Six_of_Hearts]
sample_hand6 = [Four_of_Diamonds, Six_of_Hearts, Ace_of_Spades]

blackjack_true = [Ace_of_Spades, Jack_of_Clubs]
blackjack_false = [Four_of_Clubs, Jack_of_Clubs]

sample_dealer_deck = [King_of_Diamonds, Seven_of_Diamonds, Eight_of_Hearts, Nine_of_Clubs]
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

class TestBlackJack(unittest.TestCase):
    
    def test_value(self):
        print("testing get_value()")
        self.assertEqual(value(Ace_of_Hearts), 11)
        self.assertEqual(value(Two_of_Hearts), 2)
        self.assertEqual(value(Three_of_Hearts), 3)
        self.assertEqual(value(Four_of_Hearts), 4)
        self.assertEqual(value(Five_of_Hearts), 5)
        self.assertEqual(value(Six_of_Hearts), 6)
        self.assertEqual(value(Seven_of_Hearts), 7)
        self.assertEqual(value(Eight_of_Hearts), 8)
        self.assertEqual(value(Nine_of_Hearts), 9)
        self.assertEqual(value(Ten_of_Hearts), 10)
        self.assertEqual(value(Jack_of_Hearts), 10)
        self.assertEqual(value(Queen_of_Hearts), 10)
        self.assertEqual(value(King_of_Hearts), 10)


    def test_total(self):
        print("testing calculate_total()")
        self.assertEqual(total(sample_hand1), 20)
        self.assertEqual(total(sample_hand2), 31)
        self.assertEqual(total(sample_hand3), 21)
        self.assertEqual(total(sample_hand4), 21)
        self.assertEqual(total(sample_hand5), 21)
        self.assertEqual(total(sample_hand6), 21)


    def test_is_blackjack(self):
        print("testing is_natural()")
        self.assertEqual(is_blackjack(blackjack_true), True)
        self.assertEqual(is_blackjack(blackjack_false), False)


    def test_dealers_move(self):
        print("testing dealers_move()")
        self.assertEqual(dealer_move(dealer_below_17, dealer_deck_below_17), 19)
        self.assertEqual(dealer_move(dealer_above_17, sample_dealer_deck), 20)
        self.assertEqual(dealer_move(dealer_hard_17, sample_dealer_deck), 17)
        self.assertEqual(dealer_move(dealer_soft_17, dealer_deck_soft_17), 17)
        self.assertEqual(dealer_move(dealer_ace_11, dealer_deck_ace_11), 19)
        self.assertEqual(dealer_move(dealer_ace_1, dealer_deck_ace_1), 17)


if __name__ == "__main__":
    unittest.main()

    