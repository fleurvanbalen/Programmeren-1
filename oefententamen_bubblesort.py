def bubblesort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                a = lst[j]
                lst[j]= lst[j+1]
                lst[j+1] = a
    return lst

def alt_bubblesort(lst):
    for i in range(len(lst)-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

print(bubblesort([5,8,3,2]))

print(alt_bubblesort([5,8,3,2]))