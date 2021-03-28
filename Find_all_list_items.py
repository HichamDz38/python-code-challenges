"""
    this script is for solving the chalenge:
        Sort a string
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions
import random


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
    return LL


def index_all2(search_list, item):
    """the instructor solution"""
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all2(search_list[i], item):
                indices.append([i]+index)
    return indices


# test the solutions
# my solution
print(index_all.__doc__)
print(index_all([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))

# instructor solution
print(index_all2.__doc__)
print(index_all2([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))

# prepared simple
List = [[random.randint(1, 100) for i in range(random.randint(1, 100))]
        for j in range(random.randint(1, 100))]
Item = random.randint(1, 100)

# compare the performance
print("My_solution         : ",
      timeit.timeit("index_all(List,Item)",
                    setup="from __main__ import index_all, List, Item",
                    number=100))
print("instructor_solution : ",
      timeit.timeit("index_all2(List,Item)",
                    setup="from __main__ import index_all2, List, Item",
                    number=100))
