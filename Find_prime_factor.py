"""
    this script is for solving the chalenge:
        Find prime factors
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions


def factor(n):
    """my solution before seeing the instructor solution"""
    for i in range(2, round(n**0.5)+1):
        if not(n % i) and factor(i) == [i]:
            return [i] + factor(n // i)
    return [n]


def factor2(n):
    """my solution after seeing the instructor solution"""
    for i in range(2, round(n**0.5)+1):
        if not(n % i):  # we dont need to check if the divider is prime
            return [i] + factor(n//i)
    return [n]


def factor3(N):
    """this is the instructor solution"""
    factors = list()
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N / divisor
        else:
            divisor += 1
    return factors


# to make sure that the the solution output the same result
print(factor.__doc__)
print(factor(2))
print(factor(3))
print(factor(4))
print(factor(5))
print(factor(6))
print(factor(100))
print(factor(630))

print(factor2.__doc__)
print(factor2(2))
print(factor2(3))
print(factor2(4))
print(factor2(5))
print(factor2(6))
print(factor2(100))
print(factor2(630))

print(factor3.__doc__)
print(factor3(2))
print(factor3(3))
print(factor3(4))
print(factor3(5))
print(factor3(6))
print(factor3(100))
print(factor3(630))

# compare the performance
print("My_solution         : ",
      timeit.timeit("factor(1234567891250)",
                    setup="from __main__ import factor", number=1))
print("My_solution2        : ",
      timeit.timeit("factor2(1234567891250)",
                    setup="from __main__ import factor2", number=1))
print("instructor_solution : ",
      timeit.timeit("factor3(1234567891230)",
                    setup="from __main__ import factor3", number=1))
