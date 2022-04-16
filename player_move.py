def player_move(hand, deck):

    while True:
        first_option = input("\nEnter first move (s-stand, h-hit, d-double): ").lower()
    
        if first_option == "s":
            if trace: print("player elected to stand")
            break

        if first_option == "h":
            if trace: print("player elected to hit")

            while True:

                if len(deck) == 0:
                    raise Exception("Handle later...need at least 4 cards")
            
                hit_card = deck.pop(0)
                hit_card_rank = hit_card[0]
                hand.append(hit_card)
                
                # player_hand_total = total(hand)
            
                print("\nupdated player hand:")
                print_hand(hand)
                print(f"\nupdated player hand total: {total(player_hand)}") 
        
                if total(player_hand) == 21: 
                    break
        
                if total(player_hand) > 21: 
                    break
        
                next_option = input("\nEnter next move (s-stand, h-hit): ").lower()
        
                if next_option == "h":
                    continue
        
                if trace: print("player elected to stand")
        
                break

        break

        if first_option == "d":
            if trace: print("player elected to double down")

            if len(player_hand) == 2:
                if total(player_hand) == 9 or total(player_hand) == 10 or total(player_hand) == 11:
                    initial_bet += initial_bet
                    player_earnings -= (initial_bet/2)

                    print(f"Updated Player Bank: ${player_bank}")

                    if len(deck) == 0:
                        raise Exception("Handle later...need at least 4 cards")
            
                    hit_card = deck.pop(0)
                    hand.append(hit_card)
                        
                    print("\nupdated player hand:")
                    print_hand(player_hand)
                    print(f"updated player hand total: {total(player_hand)}") 
                    break

                print("> cards total NOT 9, 10, or 11...unable double")
                continue

            print("> unable double after initial move")
            continue

    return total(player_hand)
