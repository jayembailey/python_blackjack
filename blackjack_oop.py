import random
# objects are deck, dealer, player, and i suppose the overall game, or table. 
class Deck():
    def __init__(self):
        self = self
        self.stack = [['A', 11], ('2', 2), ('3', 3), ('4', 4), ('5', 5), 
            ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10),
            ('Q', 10),('K', 10),]*4
        self.shuffle_deck = random.shuffle(self.stack)
    
class Game():
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    # def start_button(self):
    #     self.button = input('\nShall we begin? y/n ')
    #     while True:
    #         if self.button.lower() == 'y':
    #             blackjack.start()
    #             break
    #         elif self.button.lower() == 'n':
    #             print('\nSee you soon!')
    #             break
    #         else:
    #             self.button = input('please enter "y" or "n"')

    def deal_card(self):
        next_card = random.choice(self.deck.stack)
        print(f'next card: {next_card}')
        print(f'before score: {sum([card[1] for card in self.player.hand])}')
        if next_card == ['A', 11] and sum([card[1] for card in self.player.hand]) + next_card[1] > 21:
            next_card = ['A', 1]
            print(random.choice(self.deck.stack))
        self.player.hand.append(next_card)
        if sum([card[1] for card in self.dealer.hand]) < 17:
            print(f'dealer before score: {sum([card[1] for card in self.dealer.hand])}')
            if next_card == ['A', 11] and sum([card[1] for card in self.dealer.hand]) + next_card[1] > 21:
                next_card = ['A', 1]
            self.dealer.hand.append(next_card)

    def start(self):
        
        self.player.hand.append(random.choice(self.deck.stack))
        self.dealer.hand.append(random.choice(self.deck.stack))
        self.player.hand.append(random.choice(self.deck.stack))
        self.dealer.hand.append(random.choice(self.deck.stack))
        # print(f'Your hand:\n{self.player.hand}\nDealer hand:\n{self.dealer.hand}')
        
        if sum([card[1] for card in self.player.hand]) == 21:
            print('\nBlackjack! You win!')
            blackjack.print_hands()
        # elif sum([card[1] for card in self.player.hand]) > 21:
        #     print('\nBust. Losing time.')
        elif sum([card[1] for card in self.dealer.hand]) == 21:
            print('\nDealer Blackjack! You lose!')
            blackjack.print_hands()
        # elif sum([card[1] for card in self.dealer.hand]) > 21:
        #     print('\nDealer bust! Nice one.')
        else:
            blackjack.check_score()
            blackjack.hit_op()

    def print_hands(self):
        print(f'Player hand: {[card[0] for card in self.player.hand]} - Score: {sum([card[1] for card in self.player.hand])}')
        print(f'Dealer hand: {[card[0] for card in self.dealer.hand]} - Score: {sum([card[1] for card in self.dealer.hand])}')
    
    def check_score(self):
        # for card in self.player.hand:
        #     if card[0] == 'A':
        #         if sum([card[1] for card in self.player.hand]) > 21:
        #             card[1] = 1
        #             print(f'test: {self.player.hand}')

        if sum([card[1] for card in self.player.hand]) > 21:
            for card in self.player.hand:
                # print(f'test: {card}')
                if card == ['A', 11]:
                    card = ['A', 1]
                    print(f'test hand: {self.player.hand}')
                    return
                else:
                    print('\nBust. Losing time.')
                    return False
        elif sum([card[1] for card in self.player.hand]) == 21:
            print('\n21! You win!')
            # blackjack.print_hands()
            return False
        elif sum([card[1] for card in self.dealer.hand]) > 21:
            for card in self.dealer.hand:
                # print(f'test: {card}')
                if card == ['A', 11]:
                    card = ['A', 1]
                    print(f'test dealer: {self.dealer.hand}')
                    return
                else:
                    print('\nDealer bust! Nice one.')
                    return False
        elif sum([card[1] for card in self.dealer.hand]) == 21:
            print('Dealer 21. Sorry!')
            # blackjack.print_hands()
            return False
        # for card in self.dealer.hand:
        #     if card[0] == 'A':
        #         if sum([card[1] for card in self.dealer.hand]) > 21:
        #             card[1] = 1
        #             print(f'test: {self.dealer.hand}')
        #     if sum([card[1] for card in self.dealer.hand]) > 21:
        #         print('\nDealer bust! Nice one.')
        #         return 'bust'
       
    def hit_op(self):
        
        while True:
            print(f'Player hand: {[card[0] for card in self.player.hand]} - Score: {sum([card[1] for card in self.player.hand])}')
            print(f'Dealer hand: {[self.dealer.hand[0][0]]} - Score: {self.dealer.hand[0][1]}')
            question = input('\nWould you like to "hit" or "stand"?')
            if question.lower() == 'hit':
                blackjack.deal_card()
                if blackjack.check_score() == False:
                    blackjack.print_hands()
                    break

            elif question.lower() == 'stand':
                while sum([card[1] for card in self.dealer.hand]) < 17:
                    if random.choice(self.deck.stack)[0] == 'A' and sum([card[1] for card in self.player.hand]) > 21:
                        random.choice(self.deck.stack)[1] = 1
                    self.dealer.hand.append(random.choice(self.deck.stack))
                blackjack.compare()
                break
            else:
                print('Enter "hit" or "stand"')
    def compare(self):
        if sum([card[1] for card in self.player.hand]) > sum([card[1] for card in self.dealer.hand]):
            if blackjack.check_score() == False:
                return
            else:
                print('\nYou win!')
        elif sum([card[1] for card in self.dealer.hand]) > sum([card[1] for card in self.player.hand]):
            if blackjack.check_score() == False:
                blackjack.print_hands()
                return
            else:
                blackjack.print_hands
                print('\nYou lose!')
        else:
            blackjack.check_score()
            print("\nIt's a draw. Everybody wins!")
            blackjack.print_hands()
class Dealer():
    def __init__(self):
        self.score = 0
        self.hand = []

class Player(Dealer):
    def __init__(self):
        self.hand = []
        self.score = 0
blackjack = Game()
blackjack.start()