

def factorise(n) :
    number = n 
    prime_factors = [] # aanmaken van een lege array voor de priemfactoren
    p = 2 # priemfactor begint bij 2 want 0 geeft een delen door 9 error en 1 blijft oneindig doorgaan omdat alles oneindig door 1 kan worden gedeeld
    while n > 1: # Als alle priemfactoren zijn gevonden is n = 1 en stopt de loop
        if n % p == 0: # Als p een priemfactor van n is, dan geeft n modulo p = 0
            prime_factors.append(p) # Voeg de priemfactor aan de array toe
            n = n / p 
            continue # Ga naar het begin van de while loop
        p += 1 # Als er geen factoren (meer) zijn voor p, ga dan naar p + 1
        
    print('\nDe priemfactoren van {0} zijn:'.format(number))
    print(*prime_factors, '\n')
    #for i in range(len(prime_factors)): 
    #    print(prime_factors[i], end=' ')
    
factorise(6936)
factorise(86400000)
factorise(7919) # priemgetal
invoer = int(input('Voer een getal in: '))
factorise(invoer)
