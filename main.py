from random import randint

class DeckOfCards:
    
    suits = ['H', 'D', 'C', 'S']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = [ x + y for x in self.suits for y in self.vals]

class PlayerBank:
    bank = 0
    
    def draw(self, amount):
        self.bank -= int(amount)
    
    def deposit(self, amount):
        self.bank += int(amount)
    

class Player(PlayerBank):

    def __init__(self):
        pass

