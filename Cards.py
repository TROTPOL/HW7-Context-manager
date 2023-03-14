import random
import itertools
shuffle_deck = False

class CardDeck():
   
   
    ranks = ["J", "K", "Q", "A", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    small_ranks = ["J", "K", "Q", "A", 7, 8, 9, 10]
    suits = ['\u2660 spades', 
       	     '\u2665 hearts',
             '\u2666 diamonds',
             '\u2663 clubs']
    
    

    def __init__(self):
        shuffle_deck = False
        self.deck = []
        self.deck_create()
        self.shuffle_deck = shuffle_deck
        
        

    def deck_create(self):
        self.deck = list(itertools.product(CardDeck.ranks, CardDeck.suits))
        return self.deck

    def __str__(self):
        return str(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)
        global shuffle_deck
        shuffle_deck = True
        return self.deck, shuffle_deck

    def __len__(self):
        return len(self.deck)

    def __getitem__(self, number):
        item = self.deck[number]
        if not isinstance(number, slice):
            return (item)
        return tuple(item)

    def __add__(self, new_card):
        if isinstance(new_card, list):
            for card in new_card:
                self.deck.append(card)
        else:
            self.deck.append(new_card)
        return self.deck

    def __contains__(self, card):
        return (card in self.deck)

    def __eq__(self, other):
        if self.deck == other:
            return True
        return False

    def __sub__(self, card_del):
          i = self.deck.index(card_del)
          self.deck.pop(i)
          return self.deck

    def __bool__(self):
             
        if shuffle_deck is True and bool(self.deck):
            
            return True
        else:
            return False


class SmallDeck(CardDeck):

    def __str__(self):
        return f'Deck is small card {self.deck} \n'

    def deck_create(self):
        self.deck = list(itertools.product(CardDeck.small_ranks, CardDeck.suits))
        return self.deck

class ClassicDeck(CardDeck):
    
    def deck_create(self):
        self.deck = list(itertools.product(CardDeck.ranks, CardDeck.suits))
        return self.deck


    def __str__(self):
        return f'Deck is classic card {self.deck}\n'

    
    
   
if __name__ == '__main__':
    cards = [('A', '♣ clubs'), (8, '♦ diamonds'), (2, '♥ hearts')]
    card = [('Q', '♣ clubs')]

    deck_1 = CardDeck()
    print(deck_1)
    deck_2 = SmallDeck()
    deck_3 = ClassicDeck()
    
    
    '''For check decks'''
    print(deck_2)
    print(deck_3)
    
    '''For check shuffled decks'''
    deck_2.shuffle()
    deck_3.shuffle()
    print('Sort ..... deck_2', deck_2)
    print('Sort ..... deck_3', deck_3)
    
    '''For check __len__'''
    print(len(deck_2))
    print(len(deck_3))
    
    '''for check __getitem__'''
    print(deck_2[5])
    print(deck_3[5:10])
    
    '''For check __add__'''
    deck_2 = deck_2 + cards
    print(len(deck_2))
    deck_3 = deck_3 + cards
    print(len(deck_3))
    print('Deck is add', deck_3)
    
    '''for check __sub__'''
    print(len(deck_1))
    print(deck_1.__sub__(('Q', '♣ clubs')))
    print(len(deck_1))
    
    '''for check __contains__'''
    print(('A', '♣ clubs') in deck_2)
    print(('A', '♣ clubs') in deck_3)
    
    '''for check __eq__ '''
    print (deck_2 == deck_3)

    '''for check __bool__ '''
    print(deck_1.__bool__())

    
    
   


