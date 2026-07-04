
def is_fact(num):
    
    i = 1
    l = []
    while i <= num:
        if num%i == 0:
            l.append(i)
        i = i + 1
    
    return l
