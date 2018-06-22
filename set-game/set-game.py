#!/bin/python3
"""
Part 1

We will be implementing a modified version of the real card game Set.
Our version of Set involves a deck of 27 cards. Each Set card has a
shape, shading and count. Possible values for each attribute are:

shapes = ["oval", "squiggle", "diamond"]
shadings = ["solid", "striped", "open"]
counts = [1, 2, 3]

Create a class SetCard that models a Set card.
This class must include a means of printing a SetCard as a string.
Then print the string representation of a card.

Part 2

Create a SetGame class. On initialization, generate a deck of Set cards
that is stored within the class instance. The order of the deck does not matter,
as long as all 27 unique cards are present.

Part 3

In a game of Set, cards are dealt onto the table at a given time. Edit SetGame
to track the cards that are currently on the table using an instance
variable "table." Write a function deal(num_cards) in SetGame that deals
num_cards random cards onto the table from the deck.

Part 4

Write a function is_set() that accepts three cards and returns a boolean
indicating whether the three cards make up a valid set. A set is valid if all three
conditions hold:
1. Shape: all the same shape OR all different shapes
2. Shading: all the same shading OR all different shading
3. Count: all the same count OR all different count

Example set:
["oval", "solid", 1], ["oval", "solid", 2], ["oval", "solid", 3]

Example _not_ set:
["oval", "solid", 1], ["oval", "striped", 2], ["oval", "solid", 3]

Part 5

Write a function find_set() in class SetGame that finds one possible set
among the table cards and prints it out. The function should return a boolean
indicating whether or not a set was found. Handle the case where there are no sets in a graceful manner.
"""

import random


class SetCard(object):
    def __init__(self, shape, shading, count):
        self.shape = shape
        self.shading = shading
        self.count = count

    def __repr__(self):
        return "{count} {shading} {shape}".format(count=self.count, shading=self.shading, shape=self.shape)


class SetGame(object):
    def __init__(self):
        self.deck = set()
        self.table = set()
        shapes = ["oval", "squiggle", "diamond"]
        shadings = ["solid", "striped", "open"]
        counts = [1, 2, 3]
        for shape in shapes:
            for shading in shadings:
                for count in counts:
                    self.deck.add(SetCard(shape, shading, count))

    def deal(self, num_cards):
        if len(self.deck) < num_cards:
            raise ValueError("cannot deal more cards than are in the deck")
        deck = list(self.deck)
        for _ in range(num_cards):
            card = random.choice(deck)
            self.deck.remove(card)
            self.table.add(card)

    def find_set(self):
        if len(self.table) < 3:
            return False
        table = list(self.table)
        for i in range(len(table)-2):
            for j in range(i+1, len(table)-1):
                for k in range(j+1, len(table)):
                    if SetGame.is_set([table[i], table[j], table[k]]):
                        print([table[i], table[j], table[k]])
                        return True
        return False

    @staticmethod
    def is_set(cards):
        shapes = set()
        shadings = set()
        count = set()

        for card in cards:
            shapes.add(card.shape)
            shadings.add(card.shading)
            count.add(card.count)

        return ((len(shapes) == 1 or len(shapes) == 3) and
                (len(shadings) == 1 or len(shadings) == 3) and
                (len(count) == 1 or len(count) == 3))


game = SetGame()

game.deal(3)
print(game.table)
print(game.find_set())
