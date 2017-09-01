
strs = ['xc', 'zb', 'yd', 'wa']

def last(word):
    return word[-1]

print sorted(strs, key=last)
