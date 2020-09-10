def factorise(n) :
    for p in range(100):
        if n % p == 0 :
            n = n / 2
            continue
        else: 
            break

factorise(6936)