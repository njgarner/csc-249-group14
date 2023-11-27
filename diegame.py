"""
Purpose: class module for defining a die to be used in dice mini-games
"""
import random


class Die:
    def __init__(self, sides=6):
        self.sides = sides
        self.value = 0

    def roll(self):
        self.value = random.randint(1, self.sides)

    def __str__(self):
        return f'{self.sides}-sided die value: {self.value}'
