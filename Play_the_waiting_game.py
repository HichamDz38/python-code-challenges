"""
    this script is for solving the chalenge:
        Play_the_waiting_game
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions
import time
import random

def wait():
    """My solution before seening the instuctor solution"""
    x_time = random.randint(2,4)
    print("your target time is {}\nseconds.".format(x_time))
    print(" ---Press Enter to Begin---")
    input()
    t1 = time.time()
    print("...Press Enter again after\n{} seconds...".format(x_time))
    input()
    t2 = time.time()
    result = t2-t1
    print("Elapsed time: {:.3f} seconds".format(result))
    if result < x_time:
        print('({:.3f} seconds too fast)'.format(x_time-result))
    elif result >x_time:
        print('({:.3f} seconds too slow)'.format(result-x_time))
    else:
        print("amazing")


# test the solution, we dont need to compare it with the instruction
# solution, there is no calculation here.
# my solution
print(wait.__doc__)
wait()
