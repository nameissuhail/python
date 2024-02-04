import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ("Two", 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11,
          'Queen': 12, 'King': 13, 'Ace': 14}
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.values = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)
                self.cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.cards)
    def deal_one(self):
        if self.cards:
            return self.cards.pop()
        else:
            print("Error: Deck is empty.")
            return None
            
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self, card):
        if type(card) == type([]):
            self.cards.extend(card)
        else:
            self.cards.append(card)
    def adjust_for_ace(self):
        if self.value==values['Ace'] and self.value > 21:
                self.value -= 10
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    def win_bet(self):
        self.total += self.bet
    def lose_bet(self):
        self.total -= self.bet
def take_bet(player_chips):
    while True:
        try:
            bet = int(input("Enter the amount you want to bet!"))
            if 1 <= bet <= player_chips.total:
                player_chips.bet = bet
                break
            else:
                print(f'Please enter the amount between 1 and {player_chips.total}')
        except ValueError:
            print('Invalid')
    return player_chips.bet
def hit(deck, hand):
    new_card = deck.deal_one()
    hand.add_card(new_card)
    hand.adjust_for_ace()
def hit_or_stand(deck, hand):
    global playing
    while playing:
        choice = input("Do you want to hit or stand? Enter 'h' for hit or 's' for stand: ").lower()
        if choice == 'h':
            hit(deck, hand)
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                player_busts(player_chips)
                break
        elif choice == 's':
            print("Player stands. Dealer's turn.")
            playing = False
        else:
            print("Invalid input. Please enter 'h' or 's'.")
            continue
def show_some(player, dealer):
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print("\nDealer's hand:")
    print("Hidden Card")
    print(dealer.cards[1])
def show_all(player, dealer):
    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)
    print("\nDealer's hand:")
    for card in dealer.cards:
        print(card)
def player_busts(player_chips):
    print("Player busts! You lose the bet.")
    player_chips.lose_bet()
def player_wins(player_chips):
    print("Player wins! You win the bet.")
    player_chips.win_bet()
def dealer_busts(player_chips):
    print("Dealer busts! You win the bet.")
    player_chips.win_bet()
def dealer_wins(player_chips):
    print("Dealer wins! You lose the bet.")
    player_chips.lose_bet()
def push(player_chips):
    print("It's a push! Your bet is returned.")
playing = True
player_chips = Chips()
while True:
    print("Welcome to Blackjack!")
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())
    take_bet(player_chips)
    show_some(player_hand, dealer_hand)
    while playing:
        hit_or_stand(deck, player_hand)
        show_some(player_hand, dealer_hand)
        if player_hand.value > 21:
            player_busts(player_chips)
            break
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)
    show_all(player_hand, dealer_hand)
    if dealer_hand.value > 21:
        dealer_busts(player_chips)
    elif player_hand.value > dealer_hand.value:
        player_wins(player_chips)
    elif player_hand.value < dealer_hand.value:
        dealer_wins(player_chips)
    else:
        push(player_chips)
    print(f"Your total chips: {player_chips.total}")
    play_again = input("Do you want to play again? Enter 'yes' or 'no': ").lower()
    if play_again != 'yes':
        break