wachtwoord = 'wachtwoord'
ingelogd = False

print('We gaan tafels oefenen. Hoe heet je?')
naam = input()

print('Welkom ', naam, ', wat is het wachtwoord?')
invoerwachtwoord = input()

if wachtwoord == invoerwachtwoord:
    ingelogd = True
else:
    while ingelogd == False:
        print('Dat is niet goed. Geef het juiste wachtwoord in:')
        invoerwachtwoord = input()
        if wachtwoord == invoerwachtwoord:
            ingelogd = True

print('Welke tafel wil je oefenen?')
tafel = input()
try:
    tafel = int(tafel)
except:
    while True:
        print('Voer een nummer in')
        tafel = input()
        try:
            tafel = int(tafel)
            break
        except:
            continue

print('Prima daar gaan we!')

n = 1
nfout = 0
while n < 11:
    print('Hoeveel is {0} x {1}?'.format(n, tafel))
    antwoord = input()
    try:
        antwoord = int(antwoord)
    except:
        print('Voer een nummer in')
        continue
    if int(antwoord) == n * tafel:
        print('Goed zo!')
        n += 1
    else:
        print(str(antwoord), 'is helaas fout. Probeer het nog eens.')
        nfout += 1

print('Klaar! Beste {0}, je had er {1} fout.'.format(naam, nfout))