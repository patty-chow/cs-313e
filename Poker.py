#  File: Poker.py

#  Description: This program runs a game of poker with a set number of players. It shuffles cards, deals hands, and determines the type of hand given (ie. royal flush, straight, high card, etc.) as well as the winning hand.

#  Student's Name: Patty Chow

#  Student's UT EID: mpc2468   

#  Partner's Name: Natalie Castillo

#  Partner's UT EID: nac2732

#  Course Name: CS 313E 

#  Unique Number: 52600

#  Date Created: 09/18/2021

#  Date Last Modified: 09/20/2021


import sys, random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  def __eq__ (self, other):
    return self.rank == other.rank

  def __ne__ (self, other):
    return self.rank != other.rank

  def __lt__ (self, other):
    return self.rank < other.rank

  def __le__ (self, other):
    return self.rank <= other.rank

  def __gt__ (self, other):
    return self.rank > other.rank

  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.all_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.all_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.all_hands)):
      sorted_hand = sorted (self.all_hands[i], reverse = True)
      self.all_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand


    # determine winner and print


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''

    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'

  # determine if a hand is a straight flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'

  # determine if there is four-of-a-kind in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_four_kind (self, hand):
    handDic = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

    for i in range (len(hand)):
        handDic[hand[i].rank] += 1
    
    maxVal = max(handDic, key=handDic.get)
    if handDic[maxVal] != 4:
        return 0, ''

    for i in range(len(handDic)):
        if handDic[i+2] == 1:
            sideval = i + 2

    
    
    points = 8 * 15**5 + maxVal * 15**4 + maxVal * 15**3 + maxVal * 15**2 + maxVal * 15 + sideval

    return points, 'Four of a Kind'


  # determine if there is a full house in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_full_house (self, hand):
    handDic = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

    for i in range (len(hand)):
        handDic[hand[i].rank] += 1

    firstVal = max(handDic, key=handDic.get)
    if handDic[firstVal] != 3:
        return 0, ''

    firstVal = handDic.pop(firstVal)

    secondVal = max(handDic, key=handDic.get)
    if handDic[secondVal] != 2:
        return 0, ''

    if firstVal > secondVal:
        maxVal = firstVal
        minVal = secondVal
    else:
        maxVal = secondVal
        minVal = firstVal

    
    points = 7 * 15**5 + maxVal * 15**4 + maxVal * 15**3 + hand[2].rank * 15**2 + minVal * 15 + minVal

    return points, 'Full House'
    

  # determine if there is a flush in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Flush'

  # determine if there is a straight in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)

    if (not rank_order):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'

  # determine if there is three-of-a-kind in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_three_kind (self, hand):
    handDic = {2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0}

    for i in range (len(hand)):
        handDic[hand[i].rank] += 1
    
    maxVal = max(handDic, key=handDic.get)
    if handDic[maxVal] != 3:
        return 0, ''

    sideval1 = 0
    sideval2 = 0

    for i in range(len(handDic)):
        if handDic[i+2] >= 1 and i + 2 != maxVal and sideval1 == 0:
            sideval1 = i + 2
        elif handDic[i+2] >= 1 and i + 2 != maxVal:
            sideval2 = i + 2

    if sideval2 == 0:
        sideval2 = sideval1

    
    
    points = 4 * 15**5 + maxVal * 15**4 + maxVal * 15**3 + maxVal * 15**2 + sideval1 * 15 + sideval2

    return points, 'Three of a Kind'

  # determine if there are two pairs in a hand
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  def is_two_pair (self, hand):
    two_pair = 0
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        two_pair += 1
    if two_pair != 2:
      return 0, ''

    points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Two Pair'

  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  def is_one_pair (self, hand):
    one_pair = False
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        one_pair = True
        break
    if (not one_pair):
      return 0, ''

    lst = []
    for j in range(len(hand)):
        lst.append(hand[j].rank)

    for k in range(1, len(lst)):
        if hand[k].rank == hand[k-1].rank:
            num1 = lst.pop(k)
            num2 = lst.pop(k-1)


    points = 2 * 15 ** 5 + (num1) * 15 ** 4 + (num2) * 15 ** 3
    points = points + (lst[0]) * 15 ** 2 + (lst[1]) * 15 ** 1
    points = points + (lst[2])

    return points, 'One Pair'

  #takes the highest card of the deck and determines points
  def is_high_card (self,hand):
    points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'High Card'

def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int (line)
  if (num_players < 2) or (num_players > 6):
    return

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()

if __name__ == "__main__":
  main()
