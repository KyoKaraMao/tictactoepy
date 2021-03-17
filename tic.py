print("TicTacToe für Arme")
print()

board = [" ",
    "1","2","3",
    "4","5","6",
    "7","8","9"
]
currentPlayer = "X"

def printGameboard():
    # Spielfeld ausgeben
    print (board[1] + "|" + board[2] + "|" + board[3] )
    print (board[4] + "|" + board[5] + "|" + board[6] )
    print (board[7] + "|" + board[8] + "|" + board[9] )

def playerAction():
    while True:
        action = input("Insert Value: ")
        try:
            action = int(action)
        except ValueError:
            print("Please instert a Number from 1-9")
        else:
            if 1 <= action <= 9:
                return action
            else:
                print("Please instert a Number from 1-9")

def checkWin():
    #check row
    for i in range(9):
        if board[i] == currentPlayer \
                and str(board[i+1]) == currentPlayer \
                and board[i+2] == currentPlayer:
            return True
        else:
            i +=3
    #check column
    for i in range(3):
        if board[i] == currentPlayer \
                and board[i+3] == currentPlayer \
                and board[i+6] == currentPlayer:
            winner = currentPlayer
            won = True
            return winner
        else:
            i +=3
    #check
    if board[1] == currentPlayer \
            and board[5] == currentPlayer \
            and board[9] == currentPlayer:
        winner = currentPlayer
        won = True
        return winner

    if board[3] == currentPlayer \
            and board[5] == currentPlayer \
            and board[7] == currentPlayer:
        winner = currentPlayer
        won = True
        return winner
    return False

def getCurrentPlayer(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"

def updateBoard(action,currentPlayer):
    board[action] = currentPlayer

def gamestate():
    currentPlayer = "O"
    won = False
    while won is False:
        currentPlayer = getCurrentPlayer(currentPlayer)
        printGameboard()
        action = playerAction()
        updateBoard(action,currentPlayer)
        won = checkWin()
    print("The winner is",currentPlayer)
    printGameboard()

print("It starts X")
gamestate()
