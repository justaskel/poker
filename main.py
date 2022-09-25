from random import randint

class DeckOfCards:
    
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    strength = {
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }

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
        self.list_cards = list_cards
        print(f"Cards on the table: {str_cards}")
    
    def calc_hand(self, hand):
        lst = [x.split(" of")[0] for x in hand]
        res = []
        for x in lst:
            try:
                res.append(int(x))
            except:
                res.append(self.strength[x])
        return res
    
    def match_hand(self, hand):
        lst_c = [x.split(" of")[0] for x in self.list_cards]
        lst_h = [x.split(" of")[0] for x in hand]
        res = []
        for x in lst_c:
            res.append(x) if x in lst_h else None
        for x in lst_h:
            res.append(x) if x in lst_c else None
        return res


    def winner(self, hand_1, hand_2):
        h_1 = self.match_hand(hand_1)
        h_2 = self.match_hand(hand_2)
        h_1 = self.calc_hand(h_1)
        h_2 = self.calc_hand(h_2)

        if sum(h_1) == 0 and sum(h_2) == 0:
            mh_1 = max(self.calc_hand(hand_1))
            mh_2 = max(self.calc_hand(hand_2))
            if mh_1 > mh_2:
                winner = 'p'
            else:
                winner = 'c'
        elif sum(h_1) > sum(h_2):
            winner = 'p'
        else:
            winner = 'c'
        return winner

    
# print(f"Wellcome {p1_name}, how much money would you like to put into your bank?")
# money = input()
# p1.deposit(money)
def play():
    print("Hi what's your name?")
    p1_name = input()
    p1 = Player()
    p2 = Player()
    game = Game()
    player_hand = game.deal(2)
    computer_hand = game.deal(2)
    p1.hand(player_hand)
    p2.hand(computer_hand)
    game.start()
    print(f"{p1_name} hand: {', '.join(p1.hand)}")
    print(f"Computer hand: {', '.join(p2.hand)}")
    if game.winner(p1.hand, p2.hand) == 'p':
        print(f"{p1_name} wins")
    else:
        print("Computer wins")

if __name__ == "__main__":
    end = False
    play()
    while not end:
        print("Play again?")
        answer = input()
        if answer.lower().startswith('y'):
            play()
        else:
            exit()
