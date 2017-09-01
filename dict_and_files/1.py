
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
print dict

print dict['a']
dict['a'] = 6
print dict

print 'a' in dict
#print dict['z']
if 'z' in dict:
    print dict['z']
print dict.get('z')
