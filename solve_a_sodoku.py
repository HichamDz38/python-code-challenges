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
import logging
logging.basicConfig(level=logging.DEBUG)


def check(grid):
    """this function will check if the provided puzzel is correct"""
    for row in grid:
        R = row
        for r in R:
            if r!=0 and R.count(r)>1:
                logging.debug('row conflict',r)
                logging.debug(R)
                return False
    gridp = list(zip(*grid))
    
    for row in gridp:
        R = row
        for r in R:
            if r!=0 and R.count(r)>1:
                logging.debug('column conflict',r)
                logging.debug(R)
                return False
    groups = []
    for i in range(3):
        for j in range(3):
            groups.append([G[j*3:j*3+3] for G in grid[i*3:i*3+3]])
    groups = list(map(lambda x:x[0]+x[1]+x[2],groups))
    for g in groups:
        R = g
        for r in R:
            if r!=0 and R.count(r)>1:
                logging.debug('inner grid coflect',r)
                logging.debug(R)
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
        if check(puzzel):
            return puzzel

    for r in range(9):
        for c in range(9):
            if puzzel[r][c]==0:
                for n in range(1,10):
                    new_puzzel = [i for i in puzzel]
                    new_puzzel[r][c] = n
                    if check(new_puzzel):
                        result = solve(new_puzzel)
                        if result :
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

puzzel = [[1,0,3,4,5,6,7,8,9],
          [4,5,0,7,8,9,1,2,3],
          [7,8,9,1,2,3,4,5,6],
          [2,3,4,5,6,0,8,9,1],
          [5,6,7,8,9,1,2,3,4],
          [8,9,1,2,3,4,5,6,7],
          [3,4,5,0,7,8,9,1,2],
          [6,7,8,9,1,2,3,0,0],
          [9,1,2,3,4,5,6,7,0]]

puzzel =  [[2,3,0,4,1,5,0,6,8],
           [0,8,0,2,3,6,5,1,9],
           [1,6,0,9,8,7,2,3,4],
           [3,1,7,0,9,4,0,2,5],
           [4,5,8,1,2,0,6,9,7],
           [9,2,6,0,5,8,3,0,1],
           [0,0,0,5,0,0,1,0,2],
           [0,0,0,8,4,2,9,0,3],
           [5,9,2,3,7,1,4,8,6]]
print(solve(puzzel))