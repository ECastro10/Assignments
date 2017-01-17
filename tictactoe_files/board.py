class Board:


    def __init__(self):
        self.board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']



    def draw_board(self):
        counter = 0
        horiz_break = ('-----------\n')
        empty_row = (('   |   |   ') + '\n')
        board = ''

        for i in range(3):

            play_row = ((' ' + self.board[counter] + ' | ' + self.board[counter + 1] + ' | ' + self.board[counter + 2] + ' ') + '\n')

            board += empty_row
            board += play_row
            board += empty_row
            counter += 3

            if i <= 1:
                board += horiz_break
        return board






