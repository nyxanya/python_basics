

def reverse_list(l):
    i = -1
    j = 0
    while j < len(l)//2:
         t = l[j]
         l[j] = l[i] 
         l[i] = t
         i -= 1
         j += 1      
    return l


def main():
     print(reverse_list([1, 2, 3, 4, 5]), "is 5, 4, 3, 2, 1")
     print(reverse_list([1]), "is 1")
     print(reverse_list([]), "is None")

if __name__== "__main__":
     main()