import random as r
from deck import Deck
from player import Player
import pdb


deck1 = Deck()
player1 = Player(20)
dealer = Player(20)


def ace_adjust(person):
    '''
    INPUT: Takes in a player and their attributes
    USAGE: If there is an ace in the players hand, it modifies the player's score to reflect a low Ace
    OUPUT: nothing
    '''
    if person.value > 21:

        for i in person.hand:
            if i.value == 11:
                i.value = 1
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
    OUTPUT: prints_info when appropriate
    '''
    h_or_s = input('(h)it or (s)tand? > ')
    if h_or_s == 's':
        print('Player1 Stands, Dealers Turn!')
        dealer_turn()
    elif h_or_s == 'h':
        print('Player1 Hits!')
        hit(player1)
        print_info()
        if player1.value <= 21:
            player1_turn()
    else:
        player1_turn()

def dealer_turn():
    '''
    INPUT: none
    USAGE: the flow of dealer's turn
    OUTPUT: prints reveal_dealer_cards when appropriate
    '''
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
    '''
    INPUT: none
    USAGE: to show the user what is going on
    OUTPUT: prints player 1 value and hand but only 1 card and its value for dealer
    '''

    print('[----------------------------------------------------------------------------]\
\nPlayer1:\nHand: {}\nValue: {}\nBet: {}\n\n\n\nDealer:\nDealer hand: {}\n\
Dealer Value: {}\nDealer Bet: {}\n'.format(player1.hand, player1.value, player1.bet,dealer.hand[0],
dealer.hand[0].value, dealer.bet))


def reveal_dealer_cards():
    '''
    INPUT: none
    USAGE: to show all cards and values
    OUTPUT: prints out all the cards in players hand and total value
    '''
    print('[----------------------------------------------------------------------------]\
\nPlayer1:\nHand: {}\nValue: {}\nBet: {}\n\n\n\nDealer:\nDealer hand: {}\n\
Dealer Value: {}\nDealer Bet: {}\n'.format(player1.hand, player1.value, player1.bet, dealer.hand, dealer.value,
dealer.bet))


def win_check():
    '''
    INPUT: none
    USAGE: to determine who wins blackjack outside natural blackjack
    OUTPUT: print statement saying who won and who loss
    '''
    if dealer.value > 21:
        print('Dealer Busts, Player1 Wins!!')
        winnings(player1, dealer, 1)
        reset_game(player1, dealer)
    elif player1.value > 21:
        print('Player1 Busts, Dealer Wins!!')
        winnings(dealer, player1, 1)
        reset_game(player1, dealer)
    elif player1.value > dealer.value:
        print('player1 Wins!')
        winnings(player1, dealer, 1)
        reset_game(player1, dealer)
    elif player1.value < dealer.value:
        print('Dealer Wins!')
        winnings(dealer, player1, 1)
        reset_game(player1, dealer)
    else:
        print('Stand off, nobody wins')
        player1.money += player1.bet
        dealer.money += dealer.bet
        reset_game(player1, dealer)

def winnings(winner, loser, modifier):
    '''
    INPUT: two objects, and a modifier for natural blackjack
    USAGE: to give the correct player the money bet and to reset bets
    OUTPUT: none
    '''

    loser_paid = (loser.bet * modifier)
    difference = (loser_paid - loser.bet)
    winner.money += loser_paid
    winner.money += winner.bet
    loser.money -= difference

def reset_game(person1, person2):
    '''
    INPUT: both player objects
    USAGE: to reset deck, hand, values, and bets
    OUTPUT: none
    '''

    person1.value, person2.value = 0, 0
    # pdb.set_trace()
    person1.bet, person2.bet = 0, 0
    deck1.card.extend(person1.hand)
    person1.hand = list()
    deck1.card.extend(person2.hand)
    person2.hand = list()
    # hand_amount = len(person1.hand)
    # for i in range(0, hand_amount):
    #     print('Here is player 1 hand before removal {}'.format(player1.hand))
    #     print('here is deck count before appending {}'.format(len(deck1.card)))
    #     card = person1.hand.pop()
    #     deck1.card.append(card)
    #     print('card per iteration {}'.format(card))
    #
    # hand_amount = len(person2.hand)
    # for i in range(0, hand_amount):
    #     print('Here is player 1 hand before removal {}'.format(player1.hand))
    #     print('here is deck count before appending {}'.format(len(deck1.card)))
    #     card = person2.hand.pop()
    #     deck1.card.append(card)
    #     print('card per iteration {}'.format(card))


def main():
    '''
    INPUT: none
    USAGE: to run blackjack game
    OUTPUT: fun
    '''


    while player1.money != 0 or dealer.money != 0:

        #the first question of the game, play yes or no?
        print('[-----------------------------------------------------------]\
\n\nYou have ${}\nDealer has ${}'.format(player1.money, dealer.money))
        y_or_no = input('Minimum buy in = $2\nReady to play Blackjack? (y)es or (n)o? > '.lower())
        print('length of deck {}'.format(len(deck1.card)))

        #loop to prevent no as an answer
        while y_or_no != 'y':
            y_or_no = input('\nReady to play Blackjack? (y)es or (n)o? > '.lower())

        #deal and show stats (does not show both or total value of dealer cards
        player1.money -= 2
        player1.bet += 2
        deal(player1)
        dealer.money -= 2
        dealer.bet += 2
        deal(dealer)
        print_info()


        if dealer.value == 21 and player1.value == 21:
            reveal_dealer_cards()
            print('Natural Blackjack Stand Off\nNobody wins')
            player1.money += player1.bet
            dealer.money += dealer.bet
            reset_game(player1, dealer)
            main()
        elif dealer.value == 21 and player1.value < 21:
            reveal_dealer_cards()
            print('Natural Blackjack, Dealer wins!')
            winnings(dealer, player1, 1)
            reset_game(player1, dealer)
            main()
        elif dealer.value < 21 and player1.value == 21:
            reveal_dealer_cards()
            print('Natural Blackjack, player1 wins')
            winnings(player1, dealer, 1.5)
            reset_game(player1, dealer)
            main()
        else:
            player1_turn()
            reveal_dealer_cards()
        win_check()


    if dealer.money == 0:
        print('You Scoundrel, Dealer ran out of money. Thanks for playing')
        exit()
    else:
        print('You have a gambling problem and we do not take IOUs, Thank you for your money!')
        exit()

main()

