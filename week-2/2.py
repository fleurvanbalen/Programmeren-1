# pi = 3.141592653589793238462643383279...

# Functie voor de benadering van pi volgens Leibniz methode
def Leibniz(nmax): 
    arctan_1 = 0.0          #defineren van var
    for n in range(nmax+1): #de sommatie formule (nmax+1 omdat range(0) niet wordt uitgevoerd)
        arctan_1 += ((-1)**n)/(2*n+1)
    pi_leibniz = arctan_1 * 4   #arctan(1) geeft pi/4
    return pi_leibniz

# Dit is een kleine aanpassing op de bovenstaande functie. Leibniz_2 is geen
# functie maar een oneindige generator. Zo kan de convergentie van de reeks
# aanschouwd worden op het standaard uitput scherm.
def Leibniz_2():
    n = 0
    pi = 0
    while True:
        term = ((-1)**n)/(2*n+1)
        pi += 4*term
        n += 1
        yield pi


def bbp(nmax):
    pi_bbp = 0.0            #defineren van var
    for n in range(nmax+1): #de sommatie formule
        pi_bbp += (1/16**n)*((4/(8*n+1))-(2/(8*n+4))-(1/(8*n+5))-(1/(8*n+6)))
    return pi_bbp

#print(bbp(1000))
#print(bbp(10000))
3.1415926535897913
3.141592653589793

#3.141592653589793238462643383279 - 3.14159 = 2.6535898e-6 (fout marge voor 5 decimalen nauwkeurig)

# Met onderstaande code wordt uitgerekend bij welke nmax de benadering nauwkeurig is op 5 cijfers achter de komma (error < 2.6535898e-6) voor de Leibniz methode
# nmax is rond de 400000 voor 5 cijfers achter de komma
# met `n5 in range(100000, 10000000, 10000)` geeft een n5 van 1010000, dus het zit tussen 1000000 en 1010000
# range(1000000, 1010000, 100) geeft n5 = 1000100
# range(1000000, 1000100, 1) geeft 1000001 als n5
# Met een n van twee wordt met de Leibniz sommatie pi dus op 5 decimalen achter de komma benaderd

diff = 1.0
for n5 in range(376800, 482516, 1): # Een zelfgemaakte schatting wat de nmax is, aan de hand van de gemaakte berekeningen kan de range en grote van de stappen worden aangepast
    est = Leibniz(n5)
    diff = abs(est - 3.141592653589793238462643383279) # berekening van de fout
    print(n5, diff, est)
    if diff < 2.6535898e-6 : # Als de fout kleiner is dan 1e-6, wordt de loop onderbroken
        break

#Berekening van bbp(10) geeft 3.141592653589793
print(bbp(10))
