def safebox(board, r, c):
 
    for i in range(r):
        if board[i][c] == 'Q':
            return False
 
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j - 1
 
    (i, j) = (r, c)
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i = i - 1
        j = j + 1
 
    return True
 
 
def printSolution(mat):
    for r in mat:
        print(str(r).replace(',', '').replace('\'', ''))
       
    print()
 
 
def assign(board, r):
 
    if r == len(board):
        printSolution(board)
        return
 
    for i in range(len(board)):
 
        if safebox(board, r, i):
            board[r][i] = 'Q'
 
            assign(board, r + 1)

            board[r][i] = '*'
 
    
SQUARE = int(input("Enter the value of 'n':"))
 
board = [['*' for x in range(SQUARE)] for y in range(SQUARE)]
 
assign(board, 0)