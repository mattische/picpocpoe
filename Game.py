from Player import Player
from Board import Board
from random import randint
import colorama

import sys, os

class Game():


    def __init__(self, rounds):
        self.x = Player("X")
        self.o = Player("O")

        self.board = Board()

        #whos starting the game
        self.whosTurn = self.whosStarting()

        #the winner is the one who wins most rounds
        self.bestOfNbrRounds = rounds
        #the current round played
        self.currentRound = 0
        #if there is a winner
        self.weHaveAWinner = False
        #if there is a winner of the current round
        self.roundWinner = True
        #if the current round is a tie
        self.tie = False


    def whosStarting(self):
        """
        Randomize who's starting the game.
        """
        w = randint(0,1)

        if w == 0:
            return "X"
        else:
            return "O"


    def turn(self, player, coordinates):
        """
        Do a turn and also change next turns player.
        Inserts current players mark into board.
        Returns True if ok, False if coordinates of board is not correct.
        param player - the player doing the turn.
        param coordinates - the coordinates to insert players mark onto
        """

        #make sure everything is reset
        self.tie = False
        self.weHaveAWinner = False
        self.roundWinner = False

        #insert players mark on bord.
        #If coordinates incorrect, return False
        if not self.board.insertMark(coordinates, player):
            self.whosTurn = player
            return False


        #insert player X mark and change turn to player O
        if player == self.x.getMark():
            #change turn to player O
            self.whosTurn = self.o.getMark()
        #player O
        else:
            #change player turn to X
            self.whosTurn = self.x.getMark()

        #check if this turn has a winner or is a tie of the current round
        w = self.board.checkWinner()


        #O wins the round
        if w == "X":
            self.x.roundWins += 1
            self.currentRound += 1
            self.roundWinner = True
            #did X win the whole game?
            if self.x.roundWins == self.bestOfNbrRounds:
                self.weHaveAWinner = True
        #O wins the round
        elif w == "O":
            self.o.roundWins += 1
            self.currentRound += 1
            self.roundWinner = True
            #did O win the whole game?
            if self.o.roundWins == self.bestOfNbrRounds:
                self.weHaveAWinner = True
        #Is it a tie?
        elif w == "TIE":
            self.tie = True

        #everything ok, mark could be inserted to board
        return True



    def mainLoop(self):
        """
        Play the game...
        """
        q = False
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print("BEST OF", self.bestOfNbrRounds, "rounds.")
            print(colorama.Fore.RED + "X:", self.x.roundWins, colorama.Fore.BLUE + "O:", self.o.roundWins)
            print("ROUND:", (self.currentRound+1), "\n")
            print(self.board)
            cc = input(colorama.Fore.YELLOW + self.whosTurn + " insert mark coordinates: ")
            if cc == "quit":
                sys.exit()

            #if inserting coordinates is not successful - do again.
            #Otherwise, marks is inserted.
            while not self.turn(self.whosTurn, cc):
                print(colorama.Fore.RED + "Wrong coordinates. Try again: ")
                import time
                time.sleep(2)
                break

            #somebody won either a round or the whole game - or it's a tie
            if self.weHaveAWinner:# we have a game winner
                os.system('cls' if os.name == 'nt' else 'clear')
                print(colorama.Fore.RED + "HOORAY!!!", colorama.Fore.WHITE + self.board.checkWinner(), colorama.Fore.YELLOW + "WON!!!")
                print(self.board)
                if "y" == input("Another game (y/n)? "):
                    setup()
                else:
                    sys.exit()
            elif self.roundWinner:#we have a round winner
                print(colorama.Fore.YELLOW + self.board.checkWinner(), "won round", (self.currentRound))
                input("continue...")
                self.board.reset()
            elif self.tie:#we have a tie round
                print(colorama.Fore.RED + "It's a tie. Go again!")
                input("continue...")
                self.board.reset()

            #clear screen
            os.system('cls' if os.name == 'nt' else 'clear')



def setup():
    """
    setup everything... creating a game object that is...
    """
    def run():
         try:
            nbr = int(input("Number of rounds: "))
            g = Game(nbr)#create Game object
            g.mainLoop()#go!
         except Exception as err:
            print(colorama.Fore.RED + "Wrong number!" + str(err))
            run()

    #first, clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    colorama.init(autoreset=True)
    run()




if __name__ == "__main__":
    setup()
