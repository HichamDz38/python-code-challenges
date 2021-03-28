"""
    this script is for solving the chalenge:
        Sort a string
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions


def index_all(List, number):
    """my solution without seeing the instructor solution"""
    LL = []
    for i in range(len(List)):
        if type(List[i]) != list:
            if List[i] == number:
                LL += [i]
        else:
            pos = index_all(List[i], number)

            for p in pos:
                if type(p) != list:
                    LL += [[i]+[p]]
                else:
                    LL += [[i]+p]
    print(List, LL)
    return LL


# test the solutions
# my solution
print(index_all.__doc__)
print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))
