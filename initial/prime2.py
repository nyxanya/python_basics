inp = input("Enter Number: ")
num = int(inp)
i = 1
j = 0
while i <= num//i:
    if num%i == 0:
    #    print(num//i, i)
       j = j + 2
    i = i + 1

if j == 2:
    print(num, "Is Prime")
else:
    print(num, "Is Composite")
# 35,742,549,198,872,617,291,353,508,656,626,642,567