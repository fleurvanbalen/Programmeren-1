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

# Functie voor de benadering van pi volgens Bailey, Borwein en Plouffe methode
def bbp(nmax):
    pi_bbp = 0.0            #defineren van var
    for n in range(nmax+1): #de sommatie formule
        pi_bbp += (1/16**n)*((4/(8*n+1))-(2/(8*n+4))-(1/(8*n+5))-(1/(8*n+6)))
    return pi_bbp

# bbp_2 is ook de generator versie van bbp om de convergentie
# van de variabele pi te bekijken.
def bbp_2():
    n = 0
    pi = 0
    while True:
        term = (16**(-n))*((4/(8*n+1))-(2/(8*n+4))-(1/(8*n+5))-(1/(8*n+6)))
        pi += term
        n += 1
        yield pi


# Hieronder zullen de vragen beantwoord worden die bij deze opdracht
# van het computer practicum horen beantwoord worden.

# 3.141592653589793238462643383279 - 3.14159 = 2.6535898e-6 (fout marge voor 5 decimalen nauwkeurig)



# Met onderstaande code wordt uitgerekend bij welke nmax de benadering nauwkeurig is op 5 cijfers achter de komma (error < 2.6535898e-6) voor de Leibniz methode
# nmax is rond de 400000 voor 5 cijfers achter de komma
# met `n5 in range(300000, 1000000, 10000)` geeft een voor de laatste n5 380000, dus het zit tussen 370000 en 380000
# range(370000, 380000, 100) geeft n5 = 376900, dus het zit tussen 376800 en 376900
# range(376800, 376900, 1) geeft n5 = 376848, dit is dus de laagste n met een error kleiner dan 2.6535898e-6

# een nmax van 376847 geeft dus de laatste benadering waarbij de vijfde
# decimaal incorrect is. Vanaf nmax = 376848 zal pi dus consistent op vijf
# decimalen correct benaderd worden.

# NB: deze nmax is niet de laagste nmax waarvoor de eerste vijf decimalen correct
# zijn, maar de laagste nmax waarbij de eerste vijf decimalen bij álle hogere
# hogere nmax ook goed is en het dus geen "toevalstreffer" is.

diff = 1.0
for n5 in range(376800, 376900, 1): # Een zelfgemaakte schatting wat de nmax is, aan de hand van de gemaakte berekeningen kan de range en grote van de stappen worden aangepast
    est = Leibniz(n5)
    diff = abs(est - 3.141592653589793238462643383279) # berekening van de fout
    print(n5, diff, est)
    if diff < 2.6535898e-6 : # Als de fout kleiner is dan 2.6535898e-6, wordt de loop onderbroken
        break

# Om de nauwkeurigheid van bbp(10) te bepalen wordt deze functie gewoon gecalled:
print('bbp met nmax = 10: ', bbp(10))

# met als output:
# 3.14159 26535 89793

# pi is :
# 3,14159 26535 89793 23846 …

# De eerste 15 digits van de benadering pi komen dus allemaal overeen met de
# werkelijke waarde van pi. De benadering heeft waarschijnlijk niet meer
# decimalen omdat python maar een beperkt aantal bits per float beschikbaar stelt
# en deze dus ergens na de komma moeten worden afgekapt. Na 15 decimalen dus
# blijkbaar.