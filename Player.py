class Player():

    def __init__(self, mark="X"):
        self.mark = mark # X or O
        self.matchWins = 0 #nbr of games won
        self.roundWins = 0 #nbr of rounds, in a game, won

    def getMark(self):
        return self.mark

    def __str__():
        return self.mark
