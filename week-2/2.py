#benaderingen van pi (3.141592653589793238462643383279)
def leibniz(nmax): 
    arctan_1 = 0.0              #defineren van var
    for n in range(nmax):       #de sommatie formule
        arctan_1 += ((-1)**n)/(2*n+1)
    pi_leibniz = arctan_1 * 4   #arctan(1) geeft pi/4
    return pi_leibniz

#print(leibniz(1000))       #3,140592653839794
#print(leibniz(1000000))    #3,1415916535897743
#print(leibniz(10000000))

def bbp(nmax):
    pi_bbp = 0.0                #defineren van var
    for n in range(nmax):       #de sommatie formule
        pi_bbp += (1/16**n)*((4/(8*n+1))-(2/(8*n+4))-(1/(8*n+5))-(1/(8*n+6)))
    return pi_bbp

#print(bbp(1000))
#print(bbp(10000))

# Met onderstaande code wordt uitgerekend bij welke nmax de benadering nauwkeurig is op 5 cijfers achter de komma (error < 1e-6) voor de Leibniz methode
# nmax is rond de 1000000 voor 5 cijfers achter de komma
# met `n5 in rarange(100000, 10000000, 10000)` geeft een n5 van 1010000, dus het zit tussen 1000000 en 1010000
# range(1000000, 1010000, 100) geeft n5 = 1000100
# range(1000000, 1000100, 1) geeft 1000001 als n5
# Met een n van twee wordt met de Leibniz sommatie pi dus op 5 decimalen achter de komma benaderd

diff = 1.0
for n5 in range(1000000, 1010000, 1): # Een zelfgemaakte schatting wat de nmax is, aan de hand van de gemaakte berekeningen kan de range en grote van de stappen worden aangepast
    est = leibniz(n5)
    diff = abs(est - 3.141592653589793238462643383279) # berekening van de fout
    print(n5, diff, leibniz(n5))
    if diff < 1e-6 : # Als de fout kleiner is dan 1e-6, wordt de loop onderbroken
        break

#Berekening van de fout bij bbp(10)
diff_bbp = abs(bbp(10) - 3.141592653589793238462643383279)
print(bbp(10))
print(diff_bbp) #De fout van bbp(10) is 1,77635684e-15