inp = input("Enter Number: ")
num = int(inp)
i = 2

while i <num:
    if num%i == 0:
    
       print("composite")
       break
    i = i + 1 

if num == i:
    print("prime")
print('Exited at ', i)
#  35742549198872617291353508656626642567
    