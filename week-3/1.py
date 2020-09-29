alist = [-1, 16, 1, 2, 3, 2, 6, 30, 29, -50]
wordlist = ['blijf', 'ik', 'tot', 'in', 'den', 'dood', 'torljfdksfjt', 'dd']

#a.
def sum_list(items):
    sum = 0
    for n in items:
        sum += n
    return sum
print(sum_list(alist))

#b. 
def max_num_in_list(list):
    max_num = list[0]
    for n in list:
        if n > max_num:
            max_num = n
    return max_num
print(max_num_in_list(alist))

#c.
def match_words(words):
    n_words = 0
    for n in words:
        if len(n) > 2 and n[0] == n[-1]:
            n_words += 1
    return n_words
print (match_words(wordlist))