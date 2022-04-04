#! /usr/bin/env python3

import unittest
from blackjack import *

sample_card = (Ace, Spades)
sample_card2 = (8, Hearts)

sample_hand = [(2, Spades), (4, Clubs), (6, Hearts), (8, Diamonds)]
sample_hand2 = [(Ace, Spades), (Jack, Clubs), (Queen, Hearts), (King, Diamonds)]

natural_true = [(Ace, Spades), (Jack, Clubs)]
natural_false = [(4, Clubs), (Jack, Clubs)]

dealer_blackjack_test = [(), (2, Clubs), (King, Hearts), (4, Diamonds), (Ace, Spades)]
dealer_ace_test = [(), (2, Clubs), (9, Hearts), (4, Diamonds), (Ace, Spades)]

player_blackjack_test = [(), (Ace, Clubs), (6, Hearts), (10, Diamonds), (Ace, Spades)]
player_double_test = [(), (6, Clubs), (6, Hearts), (4, Diamonds), (Ace, Spades)]
player_split_test = [(), (10, Clubs), (6, Hearts), (10, Diamonds), (Ace, Spades)]


class PythonTDD(unittest.TestCase):
    
    def test_build_deck(self):
        print("testing build_deck()")
        self.assertEqual(len(build_deck()), 52)

    
    def test_print_card(self):
        print("testing print_card()")
        self.assertEqual(print_card(sample_card), 'Ace of Spades')
        self.assertEqual(print_card(sample_card2), '8 of Hearts')

    
    def test_print_hand(self):
        print("testing print_hand()")
        self.assertEqual(print_hand(sample_hand), ['2 of Spades', '4 of Clubs', '6 of Hearts', '8 of Diamonds'])
        self.assertEqual(print_hand(sample_hand2), ['Ace of Spades', 'Jack of Clubs', 'Queen of Hearts', 'King of Diamonds'])

    
    def test_get_value(self):
        print("testing get_value()")
        self.assertEqual(get_value(sample_card), 11)
        self.assertEqual(get_value(sample_card2), 8)


    def test_calculate_total(self):
        print("testing calculate_total()")
        self.assertEqual(calculate_total(sample_hand), 20)
        self.assertEqual(calculate_total(sample_hand2), 41)


    def test_is_natural(self):
        print("testing is_natural()")
        self.assertEqual(is_natural(natural_true), True)
        self.assertEqual(is_natural(natural_false), False)
        

if __name__ == "__main__":
    unittest.main()

    