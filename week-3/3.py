def f(a, x): # Bereken f(x) met a = [a0, a1, a3, ... , an]
    macht = 0
    y = 0.0
    for i in a:
        y += x**macht * i
        macht += 1
    return y

def df(a, x): # Bereken f'(x) met a = [a0, a1, a3, ... , an]
    macht = 0
    a.remove(a[0])
    y = 0.0
    for i in a:
        y += (macht + 1) * x**(macht) * i
        macht += 1
    return y

print('f(0) = ', f([-7,5,2], 0.0))
print('f\'(0) = ', df([-7,5,2], 0.0))


epsilon = 10**-7 #foutmarge

def NR(xn): # bereken de nulpunten met de Newton-Raphson methode
    while abs(f([-7,5,2], xn)) >= epsilon:
        xn -= f([-7,5,2], xn) / df([-7,5,2], xn) 
    return xn

print('nulpunt 1 op x = ', NR(-1.24))
print('nulpunt 2 op x = ', NR(-1.26))