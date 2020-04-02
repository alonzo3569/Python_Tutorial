# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:23:43 2020

@author: logan
"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
#player_busts = False
#dealer_busts = False
print(type(suits))
print(type(ranks))
print(type(values))


class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        msg = ''
        for card in self.deck:
            msg += card.__str__() + '\n'
        return msg

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'Ace' :
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.aces != 0 and self.value > 21 :
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
    def __str__(self):
        return f'Player has {self.total} chips!'

def take_bet():
    while True:
        try:
            global bet
            bet = int(input("Please input your bet: "))
        except:
            print("Your bet has to be an integer!")
        else:
            break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
        
def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck, hand)  # hit() function defined above
            break

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False
            break

        else:
            print("Sorry, please try again.")
            continue

def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('', dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')  # ?! ?? What?!!
    
def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)



## Main()
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        hit(deck, player_hand)
        hit(deck, dealer_hand)

        
    # Set up the Player's chips
    player_chip = Chips()
    
    # Prompt the Player for their bet
    take_bet()
    player_chip.bet = bet
    #print(player_chip)
 
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            #player_busts = True
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    while dealer_hand.value < 17 and player_hand.value <= 21:
        hit(deck, dealer_hand)
        #if dealer_hand.value > 21:
            
        
    # Show all cards
    show_all(player_hand,dealer_hand)
        
    # Run different winning scenarios
        
    # No one busted
    if player_hand.value <= 21 and  dealer_hand.value <= 21:
            
        # player win (player_hand.value > dealer_hand.value)
        if player_hand.value > dealer_hand.value:
            # player win chips
            player_chip.win_bet()
            print("No one busted, player win!")
            
        # player lose (player_hand.value < dealer_hand.value)
        elif player_hand.value < dealer_hand.value:
            # player lose chips
            player_chip.lose_bet()
            print("No one busted, dealer win!")
        # Call it even (player_hand.value = dealer_hand.value)
        else:
            print("Call it even!")
                
    # If player busted 
    if player_hand.value > 21:
        player_chip.lose_bet()
        print("Player busted, dealer win!")
            
    # If dealer busted 
    if dealer_hand.value > 21:
        print("Dealer busted, player win!")
        player_chip.win_bet()
    
    # Inform Player of their chips total
    print(player_chip)
    
    # Ask to play again
    #while True:
    re = input("Would you like to play again?(y/n) " )
    if re.lower() == 'y':
        playing = True
        continue
    else:
        break
        