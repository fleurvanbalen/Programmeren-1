fdataoud = open("Week6_data.txt", "r")
fdatatabel = open("W6_data_tabel.txt", "w+")
line = fdataoud.readlines() # Slaat elke regel als een apart item op in een list
for B in range(1, 32):  # Doe de loop voor iedere B apart
    minTransmissie = 10.0
    maxTransmissie = 0.0
    totTrValues = 0
    count = 0
    for i in range(2159, 3154): # golfnummer tussen 260 en 380 en dat is van regel 2160 t/m 3154 (index: 2159 en 3153)
        splitline = line[i].split() # neemt de regelnummer van het volgende golfnummer en deelt het op in aparte strings
        trValue = float(splitline[B])
        if trValue > maxTransmissie:
            maxTransmissie = trValue
        if trValue < minTransmissie:
            minTransmissie = trValue
        totTrValues += trValue
        count += 1
    for i in range(3237, 3652): # golfnummer tussen 390 en 440 en dat is van regel 3238 en 3652 (index: 3237 en 3651)
        splitline = line[i].split() # neemt de regelnummer van het volgende golfnummer en deelt het op in aparte strings
        trValue = float(splitline[B])
        if trValue > maxTransmissie:
            maxTransmissie = trValue
        if trValue < minTransmissie:
            minTransmissie = trValue
        totTrValues += trValue
        count += 1
    gemTransmissie = totTrValues/count
    print(B-1, gemTransmissie, minTransmissie, maxTransmissie, sep ='\t', file=fdatatabel)

