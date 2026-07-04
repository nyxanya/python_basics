from fun3 import is_prime

inp = input("Enter A Number: ")
n1 = int(inp)



def goldbach(n):
    i = 3
    while (n - i)>i:
        if is_prime(i):
            difference = n - i
            if is_prime(difference):
                print (n1, "=", i, "+", difference)
        i = i + 2
            
goldbach(n1)
