
s1 = 'abcd'
s2 = 'xy'

# s = 'abcxydez'

def front_back(a, b):
    if len(s1) % 2 != 0:
        a_front = s1[:len(s1)/2 + 1]
        a_back = s1[len(s1)/2 + 1:]
    else:
        a_front = s1[:len(s1)/2]
        a_back = s1[len(s1)/2:]
    if len(s2) % 2 != 0:
        b_front = s2[:len(s2)/2 + 1]
        b_back = s2[len(s2)/2 + 1:]
    else:
        b_front = s2[:len(s2)/2]
        b_back = s2[len(s2)/2:]
    return a_front + b_front + a_back + b_back
print front_back(s1, s2)
