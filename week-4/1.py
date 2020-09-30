def easter_month(Y): # De maand waarin pasen valt in jaar Y volgens de cyclus van Meton
    a = Y % 19
    b = Y // 100
    c = Y % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    month = (h + L - 7 * m + 114) // 31
    return month

def easter_day(Y): # De dag van de maand waarop pasen valt in jaar Y volgens de cyclus van Meton
    a = Y % 19
    b = Y // 100
    c = Y % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    L = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * L) // 451
    day = ((h + L - 7 * m + 114) % 31) + 1
    return day

def is_leapyear(Y): # Deze functie bepaalt of jaar Y een schrikkeljaar is (geeft True/False)
    if Y % 4 == 0: # Als het niet deelbaar is door 4 is het geen schrikkeljaar
        if Y % 100 == 0: # Als het wel deelbaar is door 4 en niet door 100 is het een schrikkeljaar
            if Y % 400 == 0: # Als het wel deelbaar is door 100 (en 4) en niet door 400 is het geen schrikkeljaar, en anders wel
                return True
            return False
        return True
    return False

def days_in_month(Y): # Functie die een list geeft met het aantal dagen voor de maanden (index begint met 0, dus voor januari: days_in_month(Y)[0])
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leapyear(Y):
        days_in_month[1] = 29 # Als Y een schrikkeljaar is heeft feb 29 dagen
    return days_in_month

def day_number_in_year(d,m,Y): # Geeft de dag in het jaar voor een bepaalde dag in de maand (d), maand (m) en jaar (Y)
    day_number = 0
    for i in range(m - 1): # De laatste maand moet niet worden opgeteld dus m - 1
        day_number += days_in_month(Y)[i] # Telt voor alle voorgaande maanden de dagen op
    day_number += d # Telt de dagen in de huidige maand erbij op
    return day_number

def month_in_year_of_day_number(day_n,Y): # Geeft de maand voor een bepaalde dag in het jaar (day_n) en jaar (Y)
    i = 0
    while day_n > days_in_month(Y)[i]: # Zolang de overgebleven dagen groter is dan de dagen in de huidige maand,
        day_n -= days_in_month(Y)[i]   # wordt het aantal dagen in de maand eraf gehaald,
        i += 1                         # en gaat ie naar de volgende maand.
    return i + 1                       # Omdat de index met 0 begint ipv 1
        

def day_in_month_of_day_number(day_n,Y): # Geeft de dag in de maand voor een bepaalde dag in het jaar (day_n) en jaar (Y)
    for i in range(month_in_year_of_day_number(day_n, Y) - 1): 
        day_n -= days_in_month(Y)[i]     # De dagen van alle voorgaande maanden worden van day_n afgehaald
    return day_n

while True: # Deze loop blijft om een invoer vragen totdat er een positief getal wordt ingevoerd
    try:
        jaar = int(input('Voer een jaartal boven 0 in: ')) # Vraagt om een jaartal
        if jaar <= 0:
            raise Exception() # Geeft een error als het jaartal minder is dan of gelijk is aan 0, waardoor hij doorgaat naar de except
        break # Als er geen error is dan wordt de loop doorbroken
    except:
        print('Error, invoer is geen positief getal')

print('\nFeestdagen in {0}:'.format(jaar)) # Header
day_n_pasen = day_number_in_year(easter_day(jaar), easter_month(jaar), jaar)

# dvp - dagen voor pasen
# dnp - dagen na pasen

# Carnaval (7 weken voor pasen t/m dinsdag) 49 dvp - 47 dvp
day_n_begin_carnaval = day_n_pasen - 49
day_n_eind_carnaval = day_n_pasen - 47
print('Carnaval:      {0}/{1}/{2} - {3}/{4}/{2}'.format(day_in_month_of_day_number(day_n_begin_carnaval, jaar), month_in_year_of_day_number(day_n_begin_carnaval, jaar), jaar, day_in_month_of_day_number(day_n_eind_carnaval, jaar), month_in_year_of_day_number(day_n_eind_carnaval, jaar)))

# Goede vrijdag (vrijdag voor pasen) 2 dvp
day_n_goede_vrijdag = day_n_pasen - 2
print('Goede Vrijdag: {0}/{1}/{2}'.format(day_in_month_of_day_number(day_n_goede_vrijdag, jaar), month_in_year_of_day_number(day_n_goede_vrijdag, jaar), jaar))

# Pasen
print('Pasen:         {0}/{1}/{2}'.format(easter_day(jaar), easter_month(jaar), jaar))

# Hemelvaart (10 dagen voor pinksteren) 39 dnp 
day_n_hemelvaart = day_n_pasen + 39
print('Hemelvaart:    {0}/{1}/{2}'.format(day_in_month_of_day_number(day_n_hemelvaart, jaar), month_in_year_of_day_number(day_n_hemelvaart, jaar), jaar))

# Pinksteren (7 weken na pasen) 49 dnp 
day_n_pinksteren = day_n_pasen + 49
print('Pinksteren:    {0}/{1}/{2}\n'.format(day_in_month_of_day_number(day_n_pinksteren, jaar), month_in_year_of_day_number(day_n_pinksteren, jaar), jaar))


'''
Checks:
print("month: {0} day: {1}".format(easter_month(2020), easter_day(2020)))
print('1600, 2000, 2020:', is_leapyear(1600), is_leapyear(2000), is_leapyear(2020), is_leapyear(2400))
print('1700, 4053:', is_leapyear(1700), is_leapyear(4053), is_leapyear(1900), is_leapyear(2100), is_leapyear(2021))
print('1 maart 2020 (schrikkeljaar):', day_number_in_year(1,3,2020))
print('1 maart 2021:', day_number_in_year(1,3,2021))
print('maand met day_n = 60 en Y = 2020 (schrikkeljaar):', month_in_year_of_day_number(60, 2020))
print('maand met day_n = 60 en Y = 2021:', month_in_year_of_day_number(60, 2021))
print('dag in maand met day_n = 60 en Y = 2020:', day_in_month_of_day_number(60, 2020))
print('dag in maand met day_n = 60 en Y = 2021:', day_in_month_of_day_number(60, 2021))
'''
