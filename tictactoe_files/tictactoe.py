import random as r
from board import Board


def play_move(player, play, board):

    '''
    INPUT: this function takes in the player that is making a move, the play, and the board
    USAGE: to change the object.board list to correctly reflect the move that was played
    OUTPUT: returns the modified board.board
    '''

    if player == 'player_1':
        board.board[play - 1] = 'X'
    else:
        board.board[play - 1] = 'O'

    return board.board



def win_check(board, win_status, winner):
    '''
    INPUT: the board to be checked, the current win_status, and the winner
    USAGE: to check the board for any met win conditions
    OUTPUT: it returns win_status, and the winner, both of which are modified based on win conditions
    '''

    t = board.board

    # code below are the win conditions
    if t[0] == t[1] and t[1] == t[2]: #Top row
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[3] == t[4] and t[4] == t[5]: #Middle Row
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[6] == t[7] and t[7] == t[8]: #Bottom Row
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[0] == t[3] and t[3] == t[6]: #Left Column
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[1] == t[4] and t[4] == t[7]: #Middle Column
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[2] == t[5] and t[5] == t[8]: #Right Column
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[0] == t[4] and t[4] == t[8]: #Diagonal Top Left to Bottom Right
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    elif t[6] == t[4] and t[4] == t[2]: #Diagonal Bottom Left to Top Right
        win_status = True
        if t[0] == 'X':
            winner = 'player_1'
        else:
            winner = 'player_2'

    return win_status, winner


def game_logic(first_player, second_player, board, printable_board):
    '''
    INPUT: two players, a board, and a printable version of that board
    USAGE: this executes the tictactoe logic. You need this function to actually play tictactoe, otherwise you just
    have a tictactoe board with no way of playing it. However you need play_move and win_check in order for this to
    function.
    OUTPUT: various messages such as requests for the player to play and win message.
    '''

    game_count = 1
    win = False
    winner = ''

    while game_count != 10 or win == True:
        if game_count % 2 == 1:

            print(printable_board)
            play_location = int(input("{}, enter in the number where you would like to play > ".format(first_player)))
            board.board = play_move(first_player, play_location, board)
            printable_board = board.draw_board()
            win, winner = win_check(board, win, winner)
            if win == True:
                print('{} wins!!!!!'.format(winner))
                break
            game_count += 1


        else:
            print(printable_board)
            play_location = int(input("{}, enter in the number where you would like to play > ".format(second_player)))
            board.board = play_move(second_player, play_location, board)
            printable_board = board.draw_board()
            win, winner = win_check(board, win, winner)
            if win == True:
                print('{} wins!!!!!'.format(winner))
                break
            game_count += 1





def main():

    tictactoe = Board()
    tictactoe_board = tictactoe.draw_board()

    rand_num = r.randint(1, 50)
    player_1 = int(input("player_1 pick a number between 1 - 50 > "))
    player_2 = int(input("player_2 pick a number between 1 - 50 > "))

    if abs(player_1 - rand_num) < abs(player_2 - rand_num):
        print("My number was {}.\nplayer_1 you win, you are X's\nplayer_2, You are O's.".format(rand_num))
        player_1 = 'player_1'
        player_2 = 'player_2'
        game_logic(player_1, player_2, tictactoe, tictactoe_board)
    else:
        print("My number was {}.\nplayer_2 you win, you are X's\nplayer_1, You are O's.".format(rand_num))
        player_1 = 'player_1'
        player_2 = 'player_2'
        game_logic(player_2, player_1, tictactoe, tictactoe_board)




main()


