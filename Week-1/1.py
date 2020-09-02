getal = -27
a = 1
while abs(a - getal /(a*a)) >1e-10:
    a = (a + getal/(a*a))/2

print(a)