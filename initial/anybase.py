
inp = input("Enter A Base: ")
b = int(inp)

if b >= 10:
    print("Base Is Too Large!")
elif b <= 1:
    print("Base Is Too Small!")
else:
    inp = input("Enter A Number: ")
    i = int(inp)

    n = 1
    while n < i:
        n = n * b

    while n > 0 and b < 10: 
        if n <= i:
            print(i // n, end="")
            i = i % n
        else:
            print(0, end="")
        n = n // b

    print()
            


