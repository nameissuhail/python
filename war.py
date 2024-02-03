import random
suits =('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks= ("Two",'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King', 'Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13, 'Ace':14}
class Card:
    def __init__(self,suit,rank):
        values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13, 'Ace':14}
        self.suit=suit
        self.rank=rank
        self.values=values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card=Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
class Player:
    def __init__(self,name):
        self.name=name
        self.all_cards=[]
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
p1=Player('one')
p2=Player('two')
new_deck=Deck()
new_deck.shuffle()
for x in range(26):
    p1.add_cards(new_deck.deal_one())
    p2.add_cards(new_deck.deal_one())
game_on=True
round_n=0
while game_on:
    round_n +=1
    print(f"Round {round_n}")
    if len(p1.all_cards)==0:
        print('Player one, out of cards! Player two wins!')
        game_on=False
        break
    if len(p2.all_cards)==0:
        print('Player two, out of cards! Player one wins!')
        game_on=False
        break
    p1_cards=[]
    p1_cards.append(p1.remove_one())
    p2_cards=[] 
    p2_cards.append(p2.remove_one())
    at_war=True
    while at_war:
        if p1_cards[-1].values>p2_cards[-1].values:
            p1.add_cards(p1_cards)
            p1.add_cards(p2_cards)
            at_war=False
        elif p1_cards[-1].values<p2_cards[-1].values:
            p2.add_cards(p1_cards)
            p2.add_cards(p2_cards)
            at_war=False
        else:
            print('WAR!')
            if len(p1_cards)<5:
                print('Player 1 unable to declare war')
                print('Player 2 wins!')
                game_on=False
                break
            elif len(p2_cards)<5:
                print('Player 2 unable to declare war')
                print('Player 1 wins!')
                game_on=False
                break
            else:
                for num in range(3):
                    p1_cards.append(p1.remove_one())
                    p2_cards.append(p2.remove_one())
        