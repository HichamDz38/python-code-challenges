"""
    this script is for solving the chalenge:
        identify a palidrome
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import re  # the instuctor solution used the re module
import timeit  # this module to compare between the solutions


def palindrom(S):
    """this is my solution without seeing the instructor solution"""
    SP = ''
    for i in S:
        j = ord(i)
        if j > 90:
            j = j - 32
        if j >= 65 and j <= 90:
            SP += chr(j)
    return SP == SP[::-1]


def palindrom2(phrase):
    """instuctor solution"""
    forwards = "".join(re.findall(r"[a-z]+", phrase.lower()))
    backwards = forwards[::-1]
    return forwards == backwards


# my solution
print(palindrom.__doc__)
print(palindrom("Go hang a salami - I'm a lasagna hog"))

# the instructor solution
print(palindrom2.__doc__)
print(palindrom2("Go hang a salami - I'm a lasagna hog"))

print("My_solution         : ",
      timeit.timeit('palindrom("Go hang a salami - \
                    I\'m a lasagna hog"*10000)',
                    setup="from __main__ import palindrom", number=100))
print("instructor_solution : ",
      timeit.timeit('palindrom2("Go hang a salami - \
                    I\'m a lasagna hog"*10000)',
                    setup="from __main__ import palindrom2", number=100))
