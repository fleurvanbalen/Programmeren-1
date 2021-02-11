'''
s = [[7,9,6, 0,0,0, 3,0,0],
    [0,0,0, 0,0,6, 9,0,0],
    [8,0,1, 2,3,0, 0,7,6],
    [0,0,0, 0,0,5, 0,0,2],
    [0,0,5, 4,1,8, 7,0,0],
    [4,0,0, 7,0,0, 5,1,0],
    [6,1,0, 0,9,0, 0,0,8],
    [0,8,2, 3,0,0, 0,9,7],
    [3,0,9, 0,0,0, 0,5,4]]
'''
oplossing = [[7,9,6, 8,5,4, 3,2,1],
    [2,4,3, 1,7,6, 9,8,5],
    [8,5,1, 2,3,9, 4,7,6],
    [1,3,7, 9,6,5, 8,4,2],
    [9,2,5, 4,1,8, 7,6,3],
    [4,6,8, 7,2,3, 5,1,9],
    [6,1,4, 5,9,7, 2,3,8],
    [5,8,2, 3,4,1, 6,9,7],
    [3,7,9, 6,8,2, 1,5,4]]


start  = [[7,9,0, 0,0,0, 3,0,0],
    [0,0,0, 0,0,6, 9,0,0],
    [8,0,0, 0,3,0, 0,7,6],
    [0,0,0, 0,0,5, 0,0,2],
    [0,0,5, 4,1,8, 7,0,0],
    [4,0,0, 7,0,0, 0,0,0],
    [6,1,0, 0,9,0, 0,0,8],
    [0,0,2, 3,0,0, 0,0,0],
    [0,0,9, 0,0,0, 0,5,4]]

def print_Sudoku(s,start):
    for r in range(9):
        for k in range(9):
            if s[r][k] == 0:
                print('  .  ', end='')
            elif start[r][k] == 0:
                print('  {0:1d}  '.format(s[r][k]), end='')
            else:
                print(' *{0:1d}* '.format(s[k][r]), end='')
        print('')

def deelsudoku_is_correct(s, k_r, g_r, k_k, g_k):
    waardes = []
    for r in range(k_r, g_r + 1):
        for k in range(k_k, g_k + 1):
            if s[r][k] != 0:
                if s[r][k] in waardes:
                    return False
                waardes.append(s[r][k])
    return True

def sudoku_is_correct(s):
    for r in range(9):
        if deelsudoku_is_correct(s, r, r, 0, 8) == False:
            return False
    for k in range(9):
        if deelsudoku_is_correct(s, 0, 8, k, k) == False:
            return False
    for r in range(0, 9, 3):
        for k in range(0, 9, 3):
            if deelsudoku_is_correct(s, r, r+2, k, k+2) == False:
                return False
    return True

def sudoku_is_opgelost(s):
    if sudoku_is_correct(s) == False:
        return False
    for r in range(9):
        for k in range(9):
            if s[r][k] == 0:
                return False
    return True

print(sudoku_is_opgelost(oplossing))
