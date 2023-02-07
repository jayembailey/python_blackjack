import random

class Deck():
    def __init__(self):
        self = self
        self.stack = [['A', 11], ('2', 2), ('3', 3), ('4', 4), ('5', 5), 
            ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('J', 10),
            ('Q', 10),('K', 10),]*4    
class Game():
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def start_button(self):
        self.button = input('\nShall we begin? y/n ')
        while True:
            if self.button.lower() == 'y':
                blackjack.start()
                break
            elif self.button.lower() == 'n':
                print('\nSee you soon!')
                break
            else:
                self.button = input('please enter "y" or "n"')
    
    def restart(self):
        self.button = input('\nPlay again? y/n ')
        while True:
            if self.button.lower() == 'y':
                blackjack.start()
                break
            elif self.button.lower() == 'n':
                break
            else:
                self.button = input('Quit playin. "y" or "n": ')

    def deal_card(self):
        self.player.hand.append(random.choice(self.deck.stack))
        if self.dealer.score < 17:
            self.dealer.hand.append(random.choice(self.deck.stack))
    
    def start(self):
        self.player.hand = []
        self.dealer.hand = []
        self.player.score = 0
        self.dealer.score = 0
        self.player.hand.append(random.choice(self.deck.stack))
        self.dealer.hand.append(random.choice(self.deck.stack))
        self.player.hand.append(random.choice(self.deck.stack))
        self.dealer.hand.append(random.choice(self.deck.stack)) 
        if sum([card[1] for card in self.player.hand]) == 21:
            print('\nBlackjack! You win!')
            blackjack.print_hands()
            blackjack.restart()
        elif sum([card[1] for card in self.dealer.hand]) == 21:
            print('\nDealer Blackjack! You lose!')
            blackjack.print_hands()
            blackjack.restart()
        else:
            if self.dealer.hand[0][0] == 'A' and self.dealer.hand[1][0] == 'A':
                self.dealer.hand[1][1] = 1
            blackjack.check_score()
            blackjack.hit_op()

    def print_hands(self):
        print(f'\nPlayer hand: {[card[0] for card in self.player.hand]} - Score: {sum([card[1] for card in self.player.hand])}')
        print(f'Dealer hand: {[card[0] for card in self.dealer.hand]} - Score: {sum([card[1] for card in self.dealer.hand])}')
    
    def check_score(self):
        self.player.score = 0
        for card in self.player.hand:
            if card[0] == 'A':
                print([card[0] for card in self.player.hand])
                card[1] = int(input('Ace in hand. 1 or 11? '))
                if card[1] != 1 and card[1] != 11:
                    card[1] = int(input('Ace in hand. 1 or 11? '))
            self.player.score += card[1]
        if self.player.score > 21:
            print('\nBust. Losing time.')
            return False
        elif self.player.score == 21:
            print('\n21! You win!')
            return False

        dealer_prev = self.dealer.score
        self.dealer.score = 0
        for card in self.dealer.hand:
            if card[0] == 'A':
                if card[1] + dealer_prev > 21:
                    card[1] = 1
            self.dealer.score += card[1]
        if self.dealer.score > 21:
            print('\nDealer bust! Nice one.')
            return False
        elif self.dealer.score == 21:
            print('\nDealer 21. Sorry!')
            return False
       
    def hit_op(self):
        while True:
            print(f'\nPlayer hand: {[card[0] for card in self.player.hand]} - Score: {self.player.score}')
            print(f'Dealer hand: {[self.dealer.hand[0][0]]} - Score: {self.dealer.hand[0][1]}')
            question = input('\nWould you like to "hit" or "stand"? ')
            if question.lower() == 'hit':
                blackjack.deal_card()
                if blackjack.check_score() == False:
                    blackjack.print_hands()
                    blackjack.restart()
                    break
            elif question.lower() == 'stand':
                while self.dealer.score < 17:
                    self.dealer.hand.append(random.choice(self.deck.stack))
                    blackjack.check_score()
                blackjack.compare()
                break
            else:
                print('\nEnter "hit" or "stand" ')

    def compare(self):
        if self.player.score > self.dealer.score:
            if blackjack.check_score() == False:
                blackjack.print_hands()
                blackjack.restart()
            else:
                print('\nYou win!')
                blackjack.print_hands()
                blackjack.restart()
        elif self.dealer.score > self.player.score:
            if self.dealer.score > 21:
                blackjack.print_hands()
                blackjack.restart()

            else:
                print('\nYou lose!')
                blackjack.print_hands()
                blackjack.restart()

        else:
            print("\nIt's a draw. Everybody wins!")
            blackjack.print_hands()
            blackjack.restart()

class Dealer():
    def __init__(self):
        self.score = 0
        self.hand = []

class Player(Dealer):
    def __init__(self):
        self.hand = []
        self.score = 0
blackjack = Game()
blackjack.start_button()