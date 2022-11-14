# import
import math
from time import sleep
from player import StupidBot, Human, SmartBot


# the game
class Game:
    def __init__(self):
        self.board = self.create_board()  # board
        self.currWinner = None  # to detect current winner

    def available_move(self):
        return [i for i, j in enumerate(self.board) if j == " "]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    # Print the board to the terminal
    @staticmethod
    # create a board
    def create_board():
        return [' ' for _ in range(9)]

    @staticmethod
    # print the tutorial board
    def print_tutorial_board():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def check_winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False
    # returns true if there is a winner else false

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.currWinner = letter
            return True
        return False
    # check if there is an empty spaces left

    def empty_space_count(self):
        count = self.board.count(' ')
        return count
    # returns how many empty space

    def empty_spaces(self):
        return ' ' in self.board


# call this function to play the game
def play(game, x, o, see_game=True):
    if see_game:
        game.print_tutorial_board()

    letter = 'X'
    while game.empty_spaces():
        if letter == 'O':
            s = o.move(game)
        else:
            s = x.move(game)
        if game.make_move(s, letter):

            if see_game:
                print(letter + ' makes a move to square {}'.format(s))
                game.print_board()
                print('')

            if game.currWinner:
                if see_game:
                    print(letter + ' wins!')
                return letter  # ends the loop and exits the game
            letter = 'O' if letter == 'X' else 'X'  # switches player

        # delay the time so that it don't look flashy
        sleep(.6)

    if see_game:
        print('It\'s a tie!')


inp = ''
x_point = 0
o_point = 0

# Enemy
o = None

game_mode = input("i: impossible mode, p: possible mode. If input is invalid then game mode will be the possible mode >> ").lower()
if game_mode == 'i':
  o = SmartBot('O')
elif game_mode = 'p':
  o = StupidBot('O')
else:
  o = StupidBot('O')
  
while inp != 'n':
    # Create human player: Human
    x = Human('X')

    # create new game
    g = Game()

    play(g, x, o, True)
    if g.currWinner == 'X':
        x_point += 1
    elif g.currWinner == 'O':
        o_point += 1
    print(f'X score : {x_point}\nO score : {o_point}')
    inp = input('Play again?(y/n) : ').lower()
    while inp != 'y' and inp != 'n':
        print('Incorrect input. Try again')
