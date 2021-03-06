print("TicTacToe für Arme")
print()

board = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9"
]
playerList = {"X", "O"}

def printGameboard():
    # Print Baoard
    print()
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
    print()


def playerAction():
    while True:
        action = input("Insert Value: ")
        try:
            action = int(action)
        except ValueError:
            print("Please instert a Number from 1-9")
        else:
            if 1 <= action <= 9:
                return action - 1
            else:
                print("Please instert a Number from 1-9")


def checkWin():
    winner = "null"
    openSpots = 0
    for i in range(9):
        if board[i] != "X" and board[i] != "O":
            openSpots += 1

    for player in playerList:
        # check row
        for i in range(0, 9, 3):
            if board[i] == player \
                    and str(board[i + 1]) == player \
                    and board[i + 2] == player:
                winner = player
            else:
                i += 3
        # check column
        for i in range(3):
            if board[i] == player \
                    and board[i + 3] == player \
                    and board[i + 6] == player:
                winner = player
        # check
        if board[0] == player \
                and board[4] == player \
                and board[8] == player:
            winner = player

        if board[2] == player \
                and board[4] == player \
                and board[6] == player:
            winner = player

    if winner == "null" and openSpots == 0:
        return "tie"
    elif winner != "null":
        return winner
    else:
        return "null"


def getCurrentPlayer(currentPlayer):
    if currentPlayer == "X":
        return "O"
    else:
        return "X"


def updateBoard(action, currentPlayer):
    board[action] = currentPlayer


def gamestate():
    currentPlayer = "O"
    winner = "null"
    while winner == "null":
        currentPlayer = getCurrentPlayer(currentPlayer)
        printGameboard()
        action = playerAction()
        updateBoard(action, currentPlayer)
        winner = checkWin()
    if winner == "tie":
        print("The game end with a", winner)
    else:
        print("Winner is", winner)
    printGameboard()


def minimax(board, death, isMaximizing):
    result = checkWin()
    if result != "null":
        return scores[result]


    if isMaximizing:
        bestScore = -100
        for i in range(9):
            # if spot is avainible?
            if board[i] != "X" and board[i] != "O":
                board[i] = "O"
                score = int(minimax(board, death + 1, False))
                board[i] = str(i + 1)
                bestScore = max(bestScore, score)

        return bestScore
    else:
        bestScore = 100
        for i in range(9):
            # if spot is avainible?
            if board[i] != "X" and board[i] != "O":
                board[i] = "X"
                score = int(minimax(board, death + 1, True))
                board[i] = str(i + 1)
                bestScore = min(score, bestScore)
        return bestScore


def bestMove():
    # AI calc the best bestMove()
    bestScore = -100
    for i in range(9):
        # if spot is avainible?
        if board[i] != "X" and board[i] != "O":
            boardcopy = board
            boardcopy[i] = "O"
            score = int(minimax(boardcopy, 0, False))
            boardcopy[i] = str(i + 1)
            if (score > bestScore):
                bestScore = score
                move = i
    return move


scores = {
    'X': -1,
    'O': 1,
    'tie': 0
}


def aigame():
    currentPlayer = "O"
    winner = "null"
    while winner == "null":
        currentPlayer = getCurrentPlayer(currentPlayer)
        printGameboard()
        if currentPlayer == "O":
            action = bestMove()
        else:
            action = playerAction()
        updateBoard(action, currentPlayer)
        winner = checkWin()
    if winner == "tie":
        print("The game end with a", winner)
    else:
        print("Winner is", winner)
    printGameboard()


print("It starts X")
game = input("AI or Normal game? Insert AI to play against MiniMax: ")
if game == "AI":
    aigame()
else:
    gamestate()
