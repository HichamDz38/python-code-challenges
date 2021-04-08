"""
    this script is for solving the chalenge:
        Play_the_waiting_game
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import random
import timeit  # this module to compare between the solutions


def simulation(*args):
    '''my solution without seeing the instructor solution'''
    # initialize the results holder DS
    results = {i: 0 for i in range(len(args), sum(args)+1)}
    for sample in range(10**6):
        some = 0
        for arg in args:  # for each dice
            some += random.randint(1, arg)  # sum of random faces
        results[some] += 1/10**6  # increase this propability
    # display the results
    for result in results:
        print("{:2} {:.2%}".format(result, results[result]))

    
# test the solutions
simulation(4, 6, 6)
