class Board():

    def __init__(self, rowsCols=3):
        self.reset()


    def reset(self):
        #the coordinates of the board
        self.board = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]

    def insertMark(self, inputCoords, mark):
        """
        insert a player mark into the board.
        param inputCoords - coordinates where mark is to be inserted.
        param mark - should be  X or O (players marks)
        """
        try:
            row, col = self.translateCoordinates(inputCoords)
            if self.board[row][col] == "X" or self.board[row][col] == "O":
                return False
            self.board[row][col] = mark
            return True

        except Exception:
            return False



    def translateCoordinates(self, markInput):
        """
        Translate coordinates from string to int - indexes in the board list.
        00 is the top left corner and 22 is the right bottom corner.
        param markInput - coordinates as string.
        """
        r = int(markInput[0])
        c = int(markInput[1])

        return r, c


    def printBoard(self):
        """
        Returns a string of board that can be outputted to print().
        """
        boardStr = "";

        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                boardStr += self.board[r][c] + " "
                if len(self.board[r][c]) == 1:
                    boardStr += " "
            boardStr += "\n"

        return boardStr


    def checkWinner(self):
        """
        Check if there is a winner.
        If there is a winner - return that players mark.
        """
        #first, is this a tie round?
        tieCount = 9
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == "X" or self.board[r][c] == "O":
                   tieCount -= 1
        if tieCount == 0:
            return "TIE"


        #rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][0] == self.board[row][2]:
                return self.board[row][0]
        #cols
        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col]:
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return self.board[0][2]

        return False





    def __str__(self):
        """
        Returns a string representation of the board.
        """
        return self.printBoard()
