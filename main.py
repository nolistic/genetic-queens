import random

# given a board, this function returns the number of good queens
def goodQueens(board):
    score = 0

    #for every item in the board
    for i in range(len(board)):
        isSafe = True
        # check all other items
        for j in range(len(board)):
            if i != j:
                # if the rows are not the same
                if board[i][0] == board[j][0]:
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

# randomly move a single queen
def mutate(board):

    queenNumber = random.randint(0, boardSize - 1)


    # pick a queen
    queen = board[queenNumber]

    # move the queen to a new row
    column =  random.randint(1, boardSize + 1)
    row = random.randint(1, boardSize + 1)

    #delete the old queen
    board[queenNumber] = (row,column)

    return board

# swap half the queens
def crossover(board1, board2):
    # add a one if odd number
    odd = len(board1) % 2

    # split place
    split = len(board1) // 2 + odd

    # shuffle the order of the queens to prevent getting stuck
    random.shuffle(board1)
    random.shuffle(board2)

    #split the queens from each board in half
    board1left = board1[0:split]
    board1right = board1[split:len(board1)]

    board2left = board2[0:split]
    board2right = board2[split:len(board2)]

    #combine them
    board1 = board1left + board2right
    board2 = board2left + board1right

    return board1, board2

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

testBoard1 = [(0,0), (0,0), (0,0), (0, 0)]
testBoard2 = [(1,1), (2,1), (3,1), (4,1)]
print(testBoard1)
print(testBoard2)
print(crossover(testBoard1, testBoard2))
