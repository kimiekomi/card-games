from blackjack import *


if __name__ == "__main__":
    sample_card = (Ace, Spades)
    sample_card2 = (8, Hearts)
    
    sample_hand = [(2, Spades), (4, Clubs), (6, Hearts), (8, Diamonds)]
    sample_hand2 = [(Ace, Spades), (Jack, Clubs), (Queen, Hearts), (King, Diamonds)]
    
    dealer_blackjack_test = [(), (2, Clubs), (King, Hearts), (4, Diamonds), (Ace, Spades)]
    dealer_ace_test       = [(), (2, Clubs), (9, Hearts), (4, Diamonds), (Ace, Spades)]
    
    player_blackjack_test  = [(), (Ace, Clubs), (6, Hearts), (10, Diamonds), (Ace, Spades)]
    player_double_test     = [(), (6, Clubs), (6, Hearts), (4, Diamonds), (Ace, Spades)]
    player_split_test      = [(), (10, Clubs), (6, Hearts), (10, Diamonds), (Ace, Spades)]

    # print("> should return 52 cards in order")
    # print(build_deck())

    # print("> should return 'Ace of Spades' and '8 of Hearts'")
    # print_card(sample_card)
    # print_card(sample_card2)

    # print("> should return '2 of Spades', '4 of Clubs', '6 of Hearts' and '8 of Diamonds'\n'Ace of Spades', 'Jack of Clubs', 'Queen of Hearts' and 'King of Diamonds'")
    # print_hand(sample_hand)
    # print_hand(sample_hand2)

    # print("> should return 11 and 8")
    # print(get_value(sample_card))
    # print(get_value(sample_card2))

    # print("> should return 20 and 41")
    print(calculate_total(sample_hand))
    print(calculate_total(sample_hand2))
    
    