
def match_ends(words):
    count = 0
    for ch in words:
        if len(ch) >= 2 and ch[0] == ch[-1]:
            count += 1
    print count

match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
match_ends(['', 'x', 'xy', 'xyx', 'xx'])
match_ends(['aaa', 'bc', 'abc', 'hello'])
