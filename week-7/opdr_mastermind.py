import random

def Word_to_list(nColours, nPositions, Duplicates):
    while True:
        try:
            userInput = input('Geef je gok: ')
            guessed_digits_list = []
            for i in range(len(userInput)):
                guessed_digits_list.append(int(userInput[i]))
            if len(guessed_digits_list) != nPositions :
                raise Exception()
            #duplicate en within colour range check:
            for digit in guessed_digits_list:
                if digit >= nColours:
                    print('Geef geen cijfer hoger dan', nColours - 1)
                    raise Exception()
                if Duplicates == False:
                    if guessed_digits_list.count(digit) > 1:
                        print('Duplicaten staan uit')
                        raise Exception()
            break
        except ValueError:
            print('Geef alleen cijfers')
            continue
        except:
            print('Geef {0} cijfers'.format(nPositions))
            continue
    return guessed_digits_list

def Count_blacks(code, guess):
    nBlacks = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            nBlacks += 1
    return nBlacks

def Count_whites(code, guess):
    nWhites = 0
    times_in_code = [0] * 9 #deze list houdt bij hoe vaak een kleur in de code voor komt, de index is hier dan de kleur
    times_in_guess = [0] * 9 #deze list houdt bij hoe vaak een kleur in de gok voor komt
    for i in range(len(code)):
        times_in_code[code[i]] += 1
        if guess[i] == code[i]: #kijkt voor welke waardes al hoeveel blacks zijn gegeven, omdat dit niet gecheck wordt in de volgende for loop
            times_in_guess[guess[i]] += 1
    
    for i in range(len(code)):
        if guess[i] in code and guess[i] != code[i]: #als de kleur wel voor komt, maar niet op de goede plek staat
            times_in_guess[guess[i]] += 1 
            if times_in_guess[guess[i]] <= times_in_code[guess[i]]: #alleen als er voor die kleur nog een positie is waar nog geen black of white voor is gegeven wordt er een white gegeven.
                nWhites += 1
    return nWhites

def mastermind(nColours=6, nPositions=4, nMaxMoves=9, Duplicates=True):
    #genereer random code
    code = []
    gewonnen = False
    #genereer de random code om te kraken:
    for i in range(nPositions):
        random_int = random.randrange(0, nColours)
        if Duplicates == False:
            while random_int in code:
                random_int = random.randrange(0, nColours)
        code.append(random_int)
    print(code)
    #het gokken:
    for i in range(nMaxMoves):
        guess = Word_to_list(nColours, nPositions, Duplicates)
        if Count_blacks(code, guess) == nPositions:
            gewonnen = True
            zet_gewonnen = i+1
            break
        print('wit: {0}, zwart: {1}'.format(Count_whites(code, guess), Count_blacks(code, guess)))
    if gewonnen == True:
        print("Dat is de correcte code, gefeliciteerd! Het is je gelukt in {0} van de {1} zetten.".format(zet_gewonnen, nMaxMoves))
    else:
        print("Het is je helaas niet gelukt, de code was:", code)

mastermind()




