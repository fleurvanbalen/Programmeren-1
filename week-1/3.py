a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4 * a * c
if D < 0:
    print('complexe getallen doen we niet aan')
    quit()

bn = 1
while abs(bn - D /(bn)) >1e-10:
    bn = (bn + D/(bn))/2

x1 = (-b - D)/(2 * a)
x2 = (-b + D)/(2 * a)
print('x1 is {0} en x2 is {1}'.format(x1, x2))