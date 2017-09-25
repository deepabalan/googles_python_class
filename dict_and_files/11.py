

def count_word(filename):
    word_dict = {}
    f = open(filename)
    for line in f:
        word_list = line.split()
        for char in word_list:
            chars = char.lower()
            if chars in word_dict:
                word_dict[chars] += 1
            else:
                word_dict[chars] = 1
#    for word, count in sorted(word_dict.items(), reverse=True):
#        print word, '\t', count
    return word_dict

def print_result(filename):
    result = count_word(filename)
    t = sorted(result.items(), reverse=True)
    for word, count in t[2:]:
        print word, '\t', count
    

print_result('foo.txt')
