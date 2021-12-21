# %%
import numpy as np
import os
os.chdir(os.path.dirname(__file__))
# %%


class Player:
    def __init__(self, initialPosition, dice, name):
        self.position = initialPosition
        self.dice = dice
        self.name = name
        self.score = 0

    def rollDice(self):
        diceValue = self.dice.roll() + self.dice.roll() + self.dice.roll()
        self.position += diceValue
        self.position = (self.position-1) % 10 + 1
        self.score += self.position
        return self.score


class Dice:
    START_VALUE = 0

    def __init__(self):
        self.rollsCount = 0
        self.value = self.START_VALUE

    def roll(self):
        self.value = self.value % 100 + 1
        self.rollsCount += 1
        return self.value


# %%
dice = Dice()
player1 = Player(6, dice, "1")
player2 = Player(10, dice, "2")

while True:
    player1.rollDice()
    if player1.score >= 1000:
        winner = 1
        break
    player2.rollDice()
    if player2.score >= 1000:
        winner = 2
        break

if winner == 1:
    print(player2.score * dice.rollsCount)
else:
    print(player1.score * dice.rollsCount)
# %%
