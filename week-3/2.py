def zeef(n):
    getallen = []
    for i in range(2, n+1): # Maak een lijst van getallen van 2 tot n
        getallen.append(i)
    iteratie = 0
    p = 2
    while p <= n:
        p = getallen[iteratie] # Neem het volgende getal uit de lijst
        wegstrepen = []
        if p**2 > n:
            print(getallen)
            break
        for i in range(p**2, n + 1, p): # Maak een lijst met getallen die weggestreept moeten worden
            wegstrepen.append(i)
        for i in wegstrepen: # Haal alle waardes in 'wegstrepen' weg uit 'getallen'
            if i in getallen:
                getallen.remove(i)
        iteratie += 1

zeef(100)
zeef(1000)
