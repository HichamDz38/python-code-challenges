
"""
    this script is for solving the chalenge:
        Count unique words
    from:
        Python Code Challenges
    link:
        https://www.linkedin.com/learning/python-code-challenges
    
    i diden't used the comparing here, because my first aproach was wrong
        => usindg split ( . , ! ?)
        so i just used the Re as the instructor solution
        
"""
import re
from collections import Counter
import timeit  # this module to compare between the solutions


def count_words(path):
    '''my solution before seening the instructor solution'''
    with open(path, "r", encoding='utf8') as File:  # open the giving file
        data = File.read().lower()  # read the file as a lower-string
        data = data.replace(',',' ').replace('.',' ')  # rep , . with spaces
        data = data.replace('!',' ').replace('?',' ')  # rep ? ! with spaces
        data = data.split()  # devide the string unto list where space or \n
    container = {}  # DS to store the frequency
    for i in data:
        container[i] = container.get(i, 0) + 1
    unique_words = list(container.keys())  # get the keys(unique words)
    unique_words.sort(key=lambda x:container[x], reverse=True)  # sorte values
    top_20_words = {i: container[i] for i in unique_words[:20]}  # top 20 words
    return top_20_words, len(unique_words)

def count_words2(path):
    '''the instructor solution'''
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        
        word_counts = Counter()
        for word in all_words:
            word_counts[word] += 1
        return word_counts, len(all_words)
        

def count_words3(path):
    '''my solution after seening the instructor solution'''
    with open(path, "r", encoding='utf8') as File:  # open the giving file
        data = File.read().lower()  # read the file as a lower-string
        data = re.findall(r'[a-zA-Z][a-zA-Z-]+', data )  # get all words/numbers
        # data = data.split()  # devide the string unto list where space or \n
    container = {}  # DS to store the frequency
    #print(data)
    for i in data:
        container[i] = container.get(i, 0) + 1
    unique_words = list(container.keys())  # get the keys(unique words)
    unique_words.sort(key=lambda x:container[x], reverse=True)  # sorte values
    top_20_words = {i: container[i] for i in unique_words[:20]}  # top 20 words
    return top_20_words, len(data)

# tests
print(count_words.__doc__)
words, total = count_words('shakespeare.txt')
print('Total Words: {}'.format(total))
print('\nTop 20 Words:')
for word in words.items():
    print('{}\t{}'.format(word[0], word[1]))
print('-'*50)

print(count_words2.__doc__)
word_counts, total = count_words2('shakespeare.txt')
print('Total Words: {}'.format(total))
print('\nTop 20 Words:')
for word in word_counts.most_common(20):
    print(word[0], '\t', word[1])
print('-'*50)

print(count_words3.__doc__)
words, total = count_words3('shakespeare.txt')
print('Total Words: {}'.format(total))
print('\nTop 20 Words:')
for word in words.items():
    print('{}\t{}'.format(word[0], word[1]))