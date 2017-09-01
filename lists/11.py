
def fun(s):
    return s[-1]

def sort_last(tuples):
    print sorted(tuples, key=fun)

sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
sort_last([('a', 'x'), ('b', 'n'), ('a', 'a')])
