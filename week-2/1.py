# a.
print('a:', end=' ')
for a in range(10):
    print(a, end=' ')
print('')

#b.
print('b:', end=' ')
for b in range(1, 11):
    print(b, end=' ')
print('')

#c.
print('c:', end=' ')
for c in range(10, 0, -1):
    print(c, end=' ')
print('')

#d.
print('d:', end=' ')
for d in range(6):
    for d2 in range(d):
        print(d2, end=' ')
print('')

#e
print('e:', end=' ')
for e3 in range(1, 6): 
    for e4 in range(e3, 21, e3):
        print(e4, end=' ')
    print('\n   ', end='')

    