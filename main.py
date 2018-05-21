import random

# given a board, this function returns the number of good queens
def goodQueens(board):
    score = 0

    #for every item in the board
    for i in range(len(board)):
            # check the next item
            for j in range(i+1, len(board)):
                #if the rows are not the same
                if i[0] != j[0]:
                    #if the columns are not the same
                    if i[1] != j[1]:
                        #if they are not on a diagonal
                        if abs(i[1] - j[1]) != abs(i[0] - j[0]):
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
