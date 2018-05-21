import random

# given a board, this function returns the number of good queens
def goodQueens(board):
    score = 0

    #for every item in the board
    for i in range(len(board) - 1):
        isSafe = True
        # check all other items
        for j in range(len(board) -1):
            if i == j:
                isSafe = False
            # if the rows are not the same
            if board[i][0] == board[j][0]: \
                    isSafe = False
            #if the columns are not the same
            if board[i][1] == board[j][1]:
                isSafe = False
            #if they are not on a diagonal
            if abs(board[i][1] - board[j][1]) == abs(board[i][0] - board[j][0]):
                isSafe = False

        #if none of those conditions are met, score++
        if isSafe == True:
            score += 1

        return score

# set size of board
boardSize = 4

# set size of population
populationSize = 100

# create list of boards
boards = []

# generate population
for j in range(populationSize):
    # initialize blank board
    board = [(0, 0)] * boardSize

    # generate available rows
    availableRow = list(range(1, boardSize + 1))

    # generate a single board
    for i in range(boardSize):
        column = i + 1
        rowIndex = random.randint(0, boardSize - i - 1)

        row = availableRow[rowIndex]
        del availableRow[rowIndex]

        board[i] = (row, column)

    boards += [board]

testBoard = [(1,1), (2,1), (3,4), (4, 2)]
result = goodQueens(testBoard)
print(result)