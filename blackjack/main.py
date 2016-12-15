import random as r
from deck import Deck
from player import Player


deck1 = Deck()
player1 = Player()
dealer = Player()

def ace_adjust(person):
    '''
    INPUT: Takes in a player and their attributes
    USAGE: If there is an ace in the players hand, it modifies the player's score to reflect a low Ace
    OUPUT: nothing
    '''
    if person.value > 21:

        for i in person.hand:
            if i.value == 11:
                person.value -= 10
                break

def deal(person):
    '''
    INPUT: none
    USAGE: Deals out initial hand and adds value of cards to repective player
    OUTPUT: none
    '''

    for i in range(0, 2):

        card = r.choice(deck1.card)
        person.value += card.value
        person.hand.append(card)
        deck1.card.remove(card)
        ace_adjust(person)

def player1_turn():
    '''
    INPUT: none
    USAGE: the flow of user's turn
    OUTPUT: none
    '''
    h_or_s = input('(h)it or (s)tand? > ')
    if h_or_s == 's':
        print('Player1 Stands, Dealers Turn!')
        dealer_turn()
    elif h_or_s == 'h':
        print('Player1 Hits!')
        hit(player1)
        print_info()
        if player1.value < 21:
            player1_turn()
    else:
        player1_turn()

def dealer_turn():
    if player1.value <= 21 and dealer.value <= 16:
        print('Dealer Hits!')
        hit(dealer)
        reveal_dealer_cards()
        if dealer.value <= 16:
            dealer_turn()
    elif dealer.value > 21:
        return
    else:
        print('Dealer Stands!')

def hit(person):
    '''
    INPUT: a player object
    USAGE: chooses random card object from deck objects, removes it from deck, adds to player.hand attribute,
    adds value, and adjusts ace value if over 21
    OUTPUT: none
    '''
    card = r.choice(deck1.card)
    person.value += card.value
    person.hand.append(card)
    deck1.card.remove(card)
    ace_adjust(person)

def print_info():

    print('[----------------------------------------------------------------------------]\
\nPlayer1:\nHand: {}\nValue: {}\n\n\n\nDealer:\nDealer hand: {}\n\
Dealer Value: {}\n'.format(player1.hand, player1.value,dealer.hand[0], dealer.hand[0].value))

def reveal_dealer_cards():

    print('[----------------------------------------------------------------------------]\
\nPlayer1:\nHand: {}\nValue: {}\n\n\n\nDealer:\nDealer hand: {}\n\
Dealer Value: {}\n'.format(player1.hand, player1.value, dealer.hand, dealer.value))

def win_check():
    if dealer.value > 21:
        print('Dealer Busts, Player1 Wins!!')
    elif player1.value > 21:
        print('Player1 Busts, Dealer Wins!!')
    elif player1.value > dealer.value:
        print('player1 Wins!')
    elif player1.value < dealer.value:
        print('Dealer Wins!')
    else:
        print('Stand off, nobody wins')

def main():


    #the first question of the game, play yes or no?
    y_or_no = input('Ready to play Blackjack? (y)es or (n)o? > '.lower())

    #loop to prevent no as an answer
    while y_or_no != 'y':
        y_or_no = input('Ready to play Blackjack? (y)es or (n)o? > '.lower())

    #deal and show stats (does not show both or total value of dealer cards
    deal(player1)
    deal(dealer)
    print_info()

    if dealer.value == 21 and player1.value == 21:
        reveal_dealer_cards()
        print('Natural Blackjack Stand Off\nNobody wins')
        exit()
    elif dealer.value == 21 and player1.value < 21:
        reveal_dealer_cards()
        print('Natural Blackjack, Dealer wins!')
        exit()
    elif dealer.value < 21 and player1.value == 21:
        reveal_dealer_cards()
        print('Natural Blackjack, player1 wins')
        exit()
    else:
        player1_turn()
    win_check()

main()

