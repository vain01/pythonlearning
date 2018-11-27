import random


def cmp_two_element(left_hand, right_hand):
    if left_hand > right_hand:
        return 1
    elif left_hand == right_hand:
        return 0
    else:
        return -1


class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        left_hand = self.suit, self.rank
        right_hand = other.suit, other.rank
        return cmp_two_element(left_hand, right_hand)


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    # def sort(self):
    #     self.cards.sort(key=Card.__cmp__)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.cards.pop())


class Hand(Deck):
    def __init__(self, label=''):
        self.cards = []
        self.label = label


# card = Card(3, 13)
# print(str(card))
# other_card = Card(2, 3)
# print(card.__cmp__(other_card))

# deck = Deck()
# print(deck)
# print()

# deck = Deck()
# deck.shuffle()
# print(deck)
# print()

# deck.sort()
# print(deck)

hand = Hand(label='new hand')
print(hand.cards)
deck = Deck()
deck.shuffle()
card = deck.pop_card()
hand.add_card(card)
print(hand)
