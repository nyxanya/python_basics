inp = input("Enter Number: ")
num = int(inp)
i = 1

while i <= num//i:
    if i * i == num:
        print(i)
    elif num%i == 0:
       print(num//i, i)
    
    i = i + 1
print("Exited at ", i)


#no # in b3tween * 2 num