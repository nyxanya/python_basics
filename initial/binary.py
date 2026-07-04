inp = input("Enter A Number")
i = int(inp)

n = 1
while n < i:
    n = n * 2


while n > 0: 
    if n <= i:
        i = i - n
        print(1, end="")
    else:
        print(0, end="")
    n = n // 2

print()
        


