class Board():
    def __init__(self) -> None:
        self.board = {'7': '  ', '8': '  ', '9': '  ',
                      '4': '  ', '5': '  ', '6': '  ',
                      '1': '  ', '2': '  ', '3': '  '}
        self.isX = True
        self.tiles = {
            'a1': '7',
            'a2': '4',
            'a3': '1',
            'b1': '8',
            'b2': '5',
            'b3': '2',
            'c1': '9',
            'c2': '6',
            'c3': '3'
        }

    def __str__(self) -> str:
        ans = ''''''
        ans += '  a  b  c \n'
        ans += '1' + self.board['7'] + ' |' + \
            self.board['8'] + '|' + self.board['9'] + '\n'
        ans += '  --+--+--' "\n"
        ans += '2' + self.board['4'] + ' |' + \
            self.board['5'] + '|' + self.board['6'] + '\n'
        ans += '  --+--+--' + '\n'
        ans += '3' + self.board['1'] + ' |' + \
            self.board['2'] + '|' + self.board['3'] + '\n'
        return ans

    def switch(self):
        self.isX = not self.isX

    def move(self, input: str):
        if input[0].lower() not in 'abc' or input[1] not in '123':
            return 'Invalid move try again'
        else:
            command = input.lower()

            if self.board[self.tiles[command]] in [' X', ' O']:
                return 'Invalid move try again'
            if self.isX:
                self.board[self.tiles[command]] = ' X'
            else:
                self.board[self.tiles[command]] = ' O'
            self.switch()

    def hasWin(self):
        if self.board[self.tiles['a1']] == self.board[self.tiles['a2']] == self.board[self.tiles['a3']] and self.board[self.tiles['a3']] in [' X', ' O']:
            return [True, self.board[self.tiles['a1']][1]]
        if self.board[self.tiles['b1']] == self.board[self.tiles['b2']] == self.board[self.tiles['b3']] and self.board[self.tiles['b3']] in [' X', ' O']:
            return [True, self.board[self.tiles['b1']][1]]
        if self.board[self.tiles['c1']] == self.board[self.tiles['c2']] == self.board[self.tiles['c3']] and self.board[self.tiles['c3']] in [' X', ' O']:
            return [True, self.board[self.tiles['c1']][1]]
        if self.board[self.tiles['a1']] == self.board[self.tiles['b1']] == self.board[self.tiles['c1']] and self.board[self.tiles['a1']] in [' X', ' O']:
            return [True, self.board[self.tiles['a1']][1]]
        if self.board[self.tiles['a2']] == self.board[self.tiles['b2']] == self.board[self.tiles['c2']] and self.board[self.tiles['a2']] in [' X', ' O']:
            return [self.board[self.tiles['a2']][1]]
        if self.board[self.tiles['a3']] == self.board[self.tiles['b3']] == self.board[self.tiles['c3']] and self.board[self.tiles['a3']] in [' X', ' O']:
            return [True, self.board[self.tiles['a3']][1]]
        if self.board[self.tiles['a1']] == self.board[self.tiles['b2']] == self.board[self.tiles['c3']] and self.board[self.tiles['a1']] in [' X', ' O']:
            return [True, self.board[self.tiles['a1']][1]]
        if self.board[self.tiles['a3']] == self.board[self.tiles['b2']] == self.board[self.tiles['c1']] and self.board[self.tiles['c1']] in [' X', ' O']:
            return [True, self.board[self.tiles['a3']][1]]
        return [False, 'L']

    def hasTie(self):
        if self.hasWin()[0] == False:
            for i in self.board.values():
                if i == '  ':
                    return False
            return True
        return False

    def play(self):
        print('Game starts \n')
        print(self)
        while self.hasWin()[0] == False and self.hasTie() == False:
            turn = input(
                'Please input the square you want to place: (ex.: a1) ')
            print('\n')
            self.move(turn)
            print(self)
        if self.hasTie():
            self.board = {'7': '  ', '8': '  ', '9': '  ',
                          '4': '  ', '5': '  ', '6': '  ',
                          '1': '  ', '2': '  ', '3': '  '}
            self.isX = True
            print('Game is a Tie')
            return 'Game is a Tie'

        else:
            self.board = {'7': '  ', '8': '  ', '9': '  ',
                          '4': '  ', '5': '  ', '6': '  ',
                          '1': '  ', '2': '  ', '3': '  '}
            self.isX = True
            return f'The winner is {self.hasWin()[1]}'


def game():
    board = Board()
    print('Game starts \n')
    print(board)
    while board.hasWin()[0] == False and board.hasTie() == False:
        turn = input('Please input the square you with to play at: ')
        print('\n')
        board.move(turn)
        print(board)


board = Board()
board.play()
