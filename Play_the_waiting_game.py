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


def wait():
    """My solution before seening the instuctor solution"""
    print("your target time is 4\nseconds.")
    print(" ---Press Enter to Begin---")
    input()
    t1 = time.time()
    print("...Press Enter again after\n4 seconds...")
    input()
    t2 = time.time()
    result = t2-t1
    print("Elapsed time: {:.3f} seconds".format(result))
    if result < 4:
        print('({:.3f} seconds too fast)'.format(4-result))
    elif result > 4:
        print('({:.3f} seconds too slow)'.format(result-4))
    else:
        print("amazing")


# test the solution, we dont need to compare it with the instruction
# solution, there is no calculation here.
# my solution
print(wait.__doc__)
wait()
