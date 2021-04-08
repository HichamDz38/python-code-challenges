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
from collections import Counter
from random import randint


def simulation(*args):
    '''my solution without seeing the instructor solution'''
    # initialize the results holder DS
    results = {i: 0 for i in range(len(args), sum(args)+1)}
    for sample in range(10**6):
        some = 0
        for arg in args:  # for each dice
            some += random.randint(1, arg)  # sum of random faces
        results[some] += 1/10**6  # increase this propability
    return results

def simulation2(*dice, num_trials=1_000_000):
    '''the instructor solution'''
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1
    """
    for outcome in range(len(dice), sum(dice)+1):
        print('{}\t {:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))
    """
    return counts


# test the solutions
print(simulation.__doc__)
results = simulation(4, 6, 6)
for result in results:
    print("{:2} {:.2%}".format(result, results[result]))
print(simulation2.__doc__)
outcome = simulation2(4, 6, 6)
for outcome in range(len((4, 6, 6)), sum((4, 6, 6))+1):
    print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/1_000_000))


# compare the performance
print("My_solution         : ",
      timeit.timeit("simulation(4, 6, 6)",
                    setup="from __main__ import simulation",
                    number=10))
print("instructor_solution : ",
      timeit.timeit("simulation2(4, 6, 6)",
                    setup="from __main__ import simulation2",
                    number=10))