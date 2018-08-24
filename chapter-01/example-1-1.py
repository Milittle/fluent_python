#!/usr/bin/python
#-*- coding: utf-8 -*-
# author: milittle
import collections

# create a named tuple Class
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits] # 笛卡儿积
    
    # dunder method in orde to support len() function 
    def __len__(self):
        return len(self._cards)

    # dunder method in order to implement object[] index calling
    def __getitem__(self, position):
        return self._cards[position]


# 测试namedtuple
def test_namedtuple():
    card = Card('7', 'diamonds')
    print(card)
    
# 测试我们写的测试类
def test_FrenchDeck():
    deck = FrenchDeck()
    print(len(deck))

    # first element
    print(deck[0]) # use __getitem__ method implement

    # last element
    print(deck[-1]) # same basic

def random_choice_deck():
    from random import choice
    deck = FrenchDeck()
    print(choice(deck))

def slice_deck():
    deck = FrenchDeck()
    print(deck[0:3]) # show deck form 0 to 3 indices
    print(deck[12::13]) # show deck from 12 to the end with interval is 13

def iterate_call():
    deck = FrenchDeck()
    for i in deck: # when we implement the __getitem__ method and it will make the deck can iteration
        print(i)

def reverse_call():
    deck = FrenchDeck()
    for i in reversed(deck):   # reversed() function implement reverse call
        print(i)


def sort_deck():
    suit_values = dict(spades=0, hearts=1, diamonds=2, clubs=4)
    def spades_high(card):
        rank_value = FrenchDeck.ranks.index(card.rank) # get cards every index for 0 to 12 and every four elements is one group
        return rank_value * len(suit_values) + suit_values[card.suit]
    deck = FrenchDeck()
    for i in sorted(deck, key=spades_high):
        print(i)


def main():
    reverse_call()

if __name__ == '__main__':
    main()
