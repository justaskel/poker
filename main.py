from random import randint

class DeckOfCards:
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.deck = [ y + " of " + x for x in self.suits for y in self.vals]

    def deal(self, num_cards):
        res = []
        for x in range(num_cards):
            num = randint(0, len(self.deck)-1)
            card = self.deck.pop(num)
            res.append(card)
        return res

class PlayerBank:

    def __init__(self):
        self.bank = 0
    
    def draw(self, amount):
        self.bank -= int(amount)
    
    def deposit(self, amount):
        self.bank += int(amount)
    

class Player(PlayerBank):

    def __init__(self):
        super(Player, self).__init__()

    def hand(self, cards):
        self.hand = cards


class Game(DeckOfCards):

    def __init__(self):
        super(Game, self).__init__()

    def start(self):
        list_cards = self.deal(3)
        str_cards = ', '.join(list_cards)
        print(f"Cards on the table: {str_cards}")
    
    

if __name__ == "__main__":
    print("Hi what's your name?")
    p1_name = input()
    print(f"Wellcome {p1_name}, how much money would you like to put into your bank?")
    money = input()
    p1 = Player()
    p1.deposit(money)
    game = Game()
    player_hand = game.deal(2)
    p1.hand(player_hand)
    game.start()
    print(f"{p1_name} hand: {', '.join(p1.hand)}")
