
def print_words(filename):
    t = []
    f = open(filename, 'rU')
    for line in f:
        t.append(line.strip())
    print t
print_words('foo.txt')
