"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""

count = {'th': 0}


def count_th(word):
    if len(word) < 2:
        a = count['th']
        count['th'] = 0
        return a
    if word[-2:] == 'th':
        count['th'] += 1
    return count_th(word[:-1])
