fdataoud = open("Week6_data.txt", "r")
def fdatanieuw(B): #functie om voor elke B een nieuwe fileobject aan te maken
    return open("Week6_data_{0}.txt".format(str(B).zfill(2)), "a+") # str(B).zfill(2) voegt 'leading zeros' toe, bv. 3 wordt 03

line = fdataoud.readlines() # Slaat elke regel als een apart item op in een list
for B in range(1, 32):  # Doe de loop voor iedere B apart
    for i in range(2159, 3652): # golfnummer moet 260 tot 440 en dat is van regel 2160 t/m 3652 (index: 2159 en 3651)
        splitline = line[i].split() # neemt de regelnummer van het volgende golfnummer en deelt het op in aparte strings
        print(splitline[0], '\t', splitline[B], file=fdatanieuw(B-1)) #print het golfnummer en bijbehorende transmissie