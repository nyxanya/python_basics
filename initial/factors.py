inp = input("Enter Number: ")
num = int(inp)
i = 1
while i <= num:
    if num%i == 0:
        print(i)
    i = i + 1

print("Exited at ", i)