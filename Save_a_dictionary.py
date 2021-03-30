"""
    this script is for solving the chalenge:
        Find_all_list_items
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions


def save_dict(dict_object, path):
    """Mysolution without seening the instructor solution"""
    try:
        F = open(path, "w")
        F.write(str(dict_object))
        F.close()
        return True
    except Exception as e:
        print(e)
        return False


def get_dict(path):
    """Mysolution without seening the instructor solution"""
    try:
        F = open(path, 'r')
        M = F.read()
        F.close()
        return eval(M)
    except Exception as e:
        print(e)
        return False


# test

D = {1:1, 2:4}

save_dict(D, 'test')
D2 = get_dict('test')
print(D == D2)