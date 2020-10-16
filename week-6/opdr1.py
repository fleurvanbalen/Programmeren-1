f = open("powers.txt", "w+")
for i in range(1, 1001):
    print(i,'\t', i**2,'\t', i**3,'\t', i**4, file=f)