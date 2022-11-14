import math
from random import choice


# template class
class Player:
    def __init__(self, letter):
        self.letter = letter

    def move(self, g):
        pass


# Human class
class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, g):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in g.available_move():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val


# Bot that choice random spaces
class StupidBot(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, g):
        return choice(g.available_move())


# Bot that think before it makes a move (unlike you)
class SmartBot(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def move(self, g):
        if len(g.available_move()) == 9:
            square = choice(g.available_move())
        else:
            square = self.be_smart(g, self.letter)['pos']
        return square

    def be_smart(self, state, player):
        me = self.letter  # the bot
        other_player = 'X' if player == 'O' else 'O'

        # Check if the previous move is a winner
        if state.currWinner == other_player:
            return {'pos': None, 'score': 1 * (state.empty_space_count() + 1) if other_player == me else -1 * (
                    state.empty_space_count() + 1)}
        elif not state.empty_spaces():
            return {'pos': None, 'score': 0}

        if player == me:
            best = {'pos': None, 'score': -math.inf}  # each score should maximize
        else:
            best = {'pos': None, 'score': math.inf}  # each score should minimize
        for possible_move in state.available_move():
            state.make_move(possible_move, player)
            sim_score = self.be_smart(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.currWinner = None
            sim_score['pos'] = possible_move  # this represents the move optimal next move

            if player == me:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
