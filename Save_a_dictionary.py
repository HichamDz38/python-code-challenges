"""
    this script is for solving the chalenge:
        Find_all_list_items
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions
import pickle


def save_dict(dict_object, path):
    """Mysolution saving without seening the instructor solution"""
    try:
        f = open(path, "w")
        f.write(str(dict_object))
        f.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_dict(path):
    """Mysolution reading without seening the instructor solution"""
    try:
        f = open(path, 'r')
        m = f.read()
        f.close()
        return eval(m)
    except Exception as e:
        print(e)
        return False


def save_dict2(dict_object, path):
    """instructor solution saving"""
    with open(path, 'wb') as file:
        pickle.dump(dict_object, file)


def get_dict2(path):
    """instructor solution reading"""
    with open(path, 'rb') as file:
        return pickle.load(file)


# test the solution

D = {1: 1, 2: 4}

# my solution
print(save_dict.__doc__)
save_dict(d, 'test')
print(get_dict.__doc__)
D2 = get_dict('test')
print(D == D2)

# instructor solution
print(save_dict2.__doc__)
save_dict2(D, 'test')
print(get_dict2.__doc__)
D2 = get_dict2('test')
print(D == D2)

# preparing simple

D = {i: i**2 for i in range(1500)}
MY_FILE = "Test1.txt"
INS_FILE = "Test2.txt"

# compare the performance writing
print("My_solution         : ",
      timeit.timeit("save_dict(d, my_file)",
                    setup="from __main__ import save_dict, D, MY_FILE",
                    number=100))
print("instructor_solution : ",
      timeit.timeit("save_dict2(d, ins_file)",
                    setup="from __main__ import save_dict2, D, INS_FILE",
                    number=100))

# compare the performance reading
print("My_solution         : ",
      timeit.timeit("print(get_dict(my_file) == d)",
                    setup="from __main__ import get_dict, d, my_file",
                    number=100))
print("instructor_solution : ",
      timeit.timeit("print(get_dict2(ins_file) == d)",
                    setup="from __main__ import get_dict2, d, ins_file",
                    number=100))
