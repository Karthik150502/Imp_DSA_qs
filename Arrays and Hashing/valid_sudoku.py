


def isValidSudoku(board):

    def isSudokuValid(r, c, num):
        for i in range(9):
            if board[r][i] == num and i != c or board[i][c] == num and i != r:
                return False 
        quadr = r//3
        quadc = c//3
        for i in range(3*quadr,3*quadr+3):
            for j in range(3*quadc,3*quadc+3):
                if i!=r and j!=c and board[i][j] == num:
                    return False
        return True
    ROWS = len(board)
    COLS = len(board[0])
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] !='.' and not isSudokuValid(r,c,board[r][c]):
                return False
    return True




board = [
    [5,3,'.','.',7,'.','.','.','.'],    
    [6,'.','.',1,9,5,'.','.','.'],
    ['.',9,8,'.','.','.','.',6,'.'],
    [8,'.','.','.',6,'.','.','.',3],
    [4,'.','.',8,'.',3,'.','.',1],
    [7,3,'.','.',7,'.','.','.',6],
    ['.',6,'.','.','.','.',2,8,'.'],
    ['.','.','.',4,1,9,'.','.',5],
    ['.','.','.','.',8,'.','.',7,9],
]


res = isValidSudoku(board)
print(res)