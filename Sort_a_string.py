"""
    this script is for solving the chalenge:
        Sort a string
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
"""
import timeit  # this module to compare between the solutions


def sort(phrase):
    """my solution without seeing the instructor solution"""
    words=phrase.split(" ")
    lower_words = phrase.lower().split(" ")
    words_dict=dict(zip(lower_words,words))
    lower_words.sort()
    sorted_phrase = []
    for word in lower_words:
        sorted_phrase += [words_dict[word]]
    return " ".join(sorted_phrase)


def sort2(phrase):
    """the instructor solution"""
    words = phrase.split() 
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(w)//2:] for w in words]
    return " ".join(words) 

# to make sure that the the solution output the same result
# my solution
print(sort('banana ORANGE apple'))

# instructor solution
print(sort2('banana ORANGE apple'))

# compare the performance
print("My_solution         : ",
      timeit.timeit("sort('banana ORANGE apple'*100000)",
                    setup="from __main__ import sort", number=100))
print("instructor_solution : ",
      timeit.timeit("sort2('banana ORANGE apple'*100000)",
                    setup="from __main__ import sort2", number=100))