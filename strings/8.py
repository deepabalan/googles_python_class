
ustring = u'A unicode \xc6\x8e string \xc3\xb1'

s = ustring.encode('utf-8')
print s

t = unicode(s, 'utf-8')
print t == ustring
