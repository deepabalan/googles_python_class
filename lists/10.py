

def front_x(words):
    t = []
    for ch in words[:]:
        if ch[0] == 'x':
            words.remove(ch)
            t.append(ch)
    new_t = sorted(t)
    new_t.extend(sorted(words))
    print new_t    

front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardwark'])
front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
