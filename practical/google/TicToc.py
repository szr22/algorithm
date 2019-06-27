import random
class TicToc:
    def __init__(self):
        self.board = [['-' for _ in range(3)] for _ in range(3)]
        self.emptyPlaces = set()
        for row in range(3):
            for col in range(3):
                self.emptyPlaces.add((row, col))

    def draw(self):
        for row in self.board:
            print('|'.join(row))
    
    def addToken(self, row, col, token):
        self.board[row][col] = token
        self.emptyPlaces.remove((row, col))

    def isFull(self):
        return len(self.emptyPlaces)==0

    def isValidMove(self, row, col):
        return (row, col) in self.emptyPlaces
    
    def winner(self):
        for i in range(3):
            if self.board[i][0] != '-' and self.board[i][0]==self.board[i][1]==self.board[i][2]:
                return self.board[i][0]
            if self.board[0][i] != '-' and self.board[0][i]==self.board[1][i]==self.board[2][i]:
                return self.board[0][i]
        if self.board[1][1] != '-' and (self.board[0][0]==self.board[1][1]==self.board[2][2] \
                or self.board[2][0]==self.board[1][1]==self.board[0][2]):
            return self.board[1][1]
        return None

class Player():
    def __init__(self):
        pass
    def play(self):
        pass

class AIPlayer(Player):
    def __init__(self, token):
        self.token = token
        
    def play(self, emptyPlaces):
        row, col = random.choice(list(emptyPlaces))
        return row, col, self.token

class HumanPlayer(Player):
    def __init__(self, token):
        self.token = token

    def play(self, emptyPlaces):
        row, col = random.choice(emptyPlaces)
        return row, col, self.token

class Game():
    def __init__(self):
        ticToc = TicToc()
        tokens = ['o', 'x']
        random.shuffle(tokens)
        players = [AIPlayer(tokens[0]), AIPlayer(tokens[1])]
        turn = 0
        winner = None
        while not ticToc.isFull() and winner == None:
            print("this is player {}'s turn".format(players[turn].token))
            emptyPlaces = ticToc.emptyPlaces
            players[turn].play(emptyPlaces)
            row, col, token = players[turn].play(emptyPlaces)
            if ticToc.isValidMove(row, col):
                ticToc.addToken(row, col, token)
            ticToc.draw()
            turn = (turn+1)%2
            winner = ticToc.winner()
        
        print("the winner is: {}".format(winner))
        ticToc.draw()

def main():
    # g = Game()
    findAllWin()

if __name__ == "__main__":
    main()
