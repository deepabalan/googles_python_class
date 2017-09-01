

def not_bad(s):
    no = s.find('not')
    b = s.find('bads')
    if b > no:
        return s[:no] + 'good' + s[b+4:]
    else:
        return s
print not_bad('This movie is not so bads')
print not_bad('This dinner is not that bads!')
print not_bad('This tea is not hot')
print not_bad('Its bads yet not')
