# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed.
    board1 = "|       |       |       |"
    board2 = "|   " + board[1] + "   |   " + board[2] + "   |   " + board[3] + "   |"
    board3 = "|_______|_______|_______|"
    board4 = "|       |       |       |"
    board5 = "|   " + board[4] + "   |   " + board[5] + "   |   " + board[6] + "   |"
    board6 = "|_______|_______|_______|"
    board7 = "|       |       |       |"
    board8 = "|   " + board[7] + "   |   " + board[8] + "   |   " + board[9] + "   |"
    board9 = "|       |       |       |"

    print
    print board1
    print board2
    print board3
    print board4
    print board5
    print board6
    print board7
    print board8
    print board9
    print

    # "board" is a list of 10 strings representing the board (ignore index 0)


def inputPlayerLetter():

    letter = ""
    while letter != "x" or letter != "o":
        letter = raw_input("Please select your letter: (x/o) ")
        if letter == "x":
            return ["x", "o"]
        if letter == "o":
            return ["o", "x"]
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    # the first element in the tuple is the player's letter, the second is the computer's letter.


def whoGoesFirst():
    return random.randint(0,1)

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    response = input("Would you like to play again? y/n")
    while response not in "yn":
        response = input("Please select y or n")
    if response == "y":
        return True
    if response == "n":
        return False



def makeMove(board, letter, move):
    board[move] = letter
    return board

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    if le == bo[1] == bo[4] == bo[7]:
        return True

    if le == bo[2] == bo[5] == bo[8]:
        return True

    if le == bo[3] == bo[6] == bo[9]:
        return True

    if le == bo[1] == bo[2] == bo[3]:
        return True

    if le == bo[4] == bo[5] == bo[6]:
        return True

    if le == bo[7] == bo[8] == bo[9]:
        return True

    if le == bo[1] == bo[5] == bo[9]:
        return True

    if le == bo[3] == bo[5] == bo[7]:
        return True

    else:
        return False


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    if move not in range(1,10):
        return False
    if board[move] == " ":
        return True
    else:
        return False


def getPlayerMove(board):
    move = input("What is your move (1-9)? ")
    while not (0 < move < 10):
        move = input("Please choose a value between 1 and 9. ")
    return move

def getStupidMove(board):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    valids = []
    for pos in range(1, 10):
        if isSpaceFree(board, pos):
            valids.append(pos)

    return random.choice(valids)


def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move and return that move.

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move

    valids = []
    for pos in range(1, 10):
        if isSpaceFree(board, pos):
            valids.append(pos)

    for num in valids:
        board[num] = computerLetter
        if isWinner(board, computerLetter):
            return num
        else:
            board[num] = " "

    # Check if the player could win on his next move, and block them.

    if computerLetter == "x":
        playerLetter = "o"
    else:
        playerLetter = "x"

    for num in valids:
        board[num] = playerLetter
        if isWinner(board, playerLetter):
            return num
        else:
            board[num] = " "

    # Try to take one of the corners, if they are free.

    cornervalids = []
    for num in valids:
        if (num == 1 or num == 3 or num == 7 or num == 9):
            cornervalids.append(num)

    if len(cornervalids) > 0:
        return random.choice(cornervalids)

    # Try to take the center, if it is free.

    if 5 in valids:
        return 5

    # Move on one of the sides.

    return random.choice(valids)


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1,10):
        if runboard[i] == " ":
            return False
    return True

    # Reset the board
    # Check playing conditions
            # Player's turn.
            # Computer's turn.

if __name__ == "__main__":
    restart = ""

    while restart != "q":

        # initialize an empty board
        runboard = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        drawBoard(runboard)
        # plist[0] is always the player. p1 is the first mover.
        plist = inputPlayerLetter()
        p1 = plist[whoGoesFirst()]

        if p1 == "x":
            p2 = "o"
        else:
            p2 = "x"

        # cycles through p1 and p2
        order = [p1, p2] * 12

        for round in order:
            if not (isBoardFull(runboard)):
                # player move
                if round == plist[0]:
                    pmove = getPlayerMove(runboard)
                    while not isSpaceFree(runboard, pmove):
                        print "Move is not allowed. Please try again."
                        pmove = getPlayerMove(runboard)
                    makeMove(runboard, plist[0], pmove)
                    if isWinner(runboard, plist[0]):
                        drawBoard(runboard)
                        print "You win!"
                        break

                # computer move
                elif round == plist[1]:
                    pmove = getComputerMove(runboard, plist[1])
                    makeMove(runboard, plist[1], pmove)
                    drawBoard(runboard)
                    if isWinner(runboard, plist[1]):
                        print "You lose!"
                        break

        restart = raw_input("Press any key to play again or 'q' to exit. ")
