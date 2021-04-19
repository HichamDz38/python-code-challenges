"""
    this script is for solving the chalenge:
        Solve_a_sodoku
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions
import random

def check(puzzel):
    """this function will check if the provided puzzel is correct"""
    for row in grid:
        R = ''.join(row).replace('0','')
        for r in R:
            if R.count(r)>1:
                return False
    gridp = list(zip(*grid))
    
    for row in gridp:
        R = ''.join(row).replace('0','')
        for r in R:
            if R.count(r)>1:
                return False
    groups = []
    for i in range(3):
        for j in range(3):
            groups.append([G[j*3:j*3+3] for G in grid[i*3:i*3+3]])
    groups = list(map(lambda x:x[0]+x[1]+x[2],groups))
    for g in groups:
        R = ''.join(g).replace('0','')
        for r in R:
            if R.count(r)>1:
                return False
    return True


def is_full(puzzel):
    """this function will check if the board is full"""
    for r in range(9):
        for c in range(9):
            if puzzel[r][c]==0:
                return False
    return True


def solve(puzzel):
    """my solution before seen the  instructor's solution"""

    if is_full(puzzel):
        return check(puzzel)

    for r in range(9):
        for c in range(9):
            if puzzel[r][c]==0:
                for n in range(1,10):
                    if n not in puzzel[r]:
                        new_puzzel = [i for i in puzzel]
                        new_puzzel[r][c] = n
                        result = solve(new_puzzel)
                        if result and check(result):
                            return result
                return False
    return False


# tests
print(solve.__doc__)
puzzel = [[0,0,1,0,0,0,0,0,0],
          [2,0,0,0,0,0,0,7,0],
          [0,7,0,0,0,0,0,0,0],
          [1,0,0,4,0,6,0,0,7],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,1,2,5,4,6],
          [3,0,2,7,6,0,9,8,0],
          [0,6,4,9,0,3,0,0,1],
          [9,8,0,5,2,1,0,6,0]]
print(solve(puzzel))