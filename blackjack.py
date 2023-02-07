import random

my_wins = 0
my_losses = 0
my_draw = 0
start_op = input('\nWould you like to play a game? Y/N ')
while True:
    if start_op.lower() == 'y':
        suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
        cards = []
        for card in range(13): cards.append(card+1)
        for card in range(13): cards.append(card+1)
        for card in range(13): cards.append(card+1)
        for card in range(13): cards.append(card+1)
        my_cards = []
        my_suits = []
        dealer_cards = []
        dealer_suits = []
        my_cards.append(random.choice(cards))
        my_cards.append(random.choice(cards))
        my_suits.append(random.choice(suits))
        my_suits.append(random.choice(suits))
        dealer_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
        dealer_suits.append(random.choice(suits))
        dealer_suits.append(random.choice(suits))
        
        if sum(my_cards) == 21:
            print('\nBlackjack! You win!')
            print(f'\nYour cards:\n{my_cards} of {my_suits}')
            print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
            my_wins += 1
            start_op = input('\nPlay again? y/n ')
        elif sum(my_cards) > 21:
            print('\nBust! That was quick.')
            print(f'\nYour cards:\n{my_cards} of {my_suits}')
            print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
            my_losses += 1
            start_op = input('\nPlay again? y/n ')
        elif sum(dealer_cards) == 21:
            print('\nDealer blackjack! Sorry!')
            print(f'\nYour cards:\n{my_cards} of {my_suits}')
            print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
            my_losses += 1
            start_op = input('\nPlay again? y/n ')
        elif sum(dealer_cards) > 21:
            print('\nDealer bust! Nice.')
            print(f'\nYour cards:\n{my_cards} of {my_suits}')
            print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
            my_wins += 1
            start_op = input('\nPlay again? y/n ')
        else:
            print(f'\nYour cards:\n{my_cards} of {my_suits}')
            print(f'Dealer Cards:\n{dealer_cards[0]} of {dealer_suits[0]}')
            while True:
                hit_op = input('\nWould you like to "hit" or "stand"?')
                if hit_op.lower() == 'hit':
                    my_cards.append(random.choice(cards))
                    my_suits.append(random.choice(suits))
                    dealer_cards.append(random.choice(cards))
                    dealer_suits.append(random.choice(suits))
                    if sum(my_cards) > 21:
                        print('\nBust! Try again.')
                        print(f'\nYour cards:\n{my_cards} of {my_suits}')
                        print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
                        my_losses += 1
                        start_op = input('\nPlay again? y/n ')
                        break
                    elif sum(dealer_cards) > 21:
                        print('\nDealer bust! You lucky dog!')
                        print(f'\nYour cards:\n{my_cards} of {my_suits}')
                        print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
                        my_wins += 1
                        start_op = input('\nPlay again? y/n ')
                        break
                    else:
                        print(f'\nYour cards:\n{my_cards} of {my_suits}')
                        print(f'Dealer cards:\n{dealer_cards[0]} of {dealer_suits[0]}')
                elif hit_op.lower() == 'stand':
                    print(f'\nYour cards:\n{my_cards} of {my_suits}')
                    print(f'Dealer cards:\n{dealer_cards} of {dealer_suits}')
                    if sum(my_cards) > sum(dealer_cards):
                        print('\nYou win! All monies for you!')
                        my_wins += 1
                        start_op = input('\nPlay again? y/n ')
                        break
                    elif sum(my_cards) < sum(dealer_cards):
                        print('\nYou lose! Hahaha sucks!')
                        my_losses += 1
                        start_op = input('\nPlay again? y/n ')
                        break
                    else:
                        print("\nWell that's odd. It's a draw!")
                        start_op = input('\nPlay again? y/n ')
                        my_draw += 1
                        break
                else:
                    continue
    elif start_op.lower() == 'n':
        print(f'\nK bye!\nWins: {my_wins}\nLosses: {my_losses}\nDraw: {my_draw}')
        break
    else:
        start_op = input("\nIt's a 'y' or 'n' question, bud. ")

