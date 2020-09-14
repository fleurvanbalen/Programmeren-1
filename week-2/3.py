

def factorise(n) :
    print('\nDe priemfactoren van {0} zijn:'.format(n))
    prime_factors = [] # aanmaken van een lege list voor de priemfactoren
    p = 2 # priemfactor begint bij 2 want 0 geeft een delen door 9 error en 1 blijft oneindig doorgaan omdat alles oneindig door 1 kan worden gedeeld
    while n > 1: # Als alle priemfactoren zijn gevonden is n = 1 en stopt de loop
        if n % p == 0: # Als p een priemfactor van n is, dan geeft n modulo p = 0
            prime_factors.append(p) # Voeg de priemfactor aan de list toe
            n = n / p 
            continue # Ga naar het begin van de while loop
        p += 1 # Als n geen factor p (meer) heeft, ga dan naar p + 1
    print(*prime_factors, '\n') # Print de lijst van priemfactoren

    
factorise(6936)
factorise(86400000)
factorise(7919) # priemgetal
invoer = int(input('Voer een getal in: '))
factorise(invoer)
