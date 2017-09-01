
dict = {'a': 1, 'b': 2, 'c': 3}
for keys, values in dict.items():
    print keys, values

# By default, iterating over a dict iterates over its keys.
for key in dict:
    print key

print dict.keys()
print dict.values()
