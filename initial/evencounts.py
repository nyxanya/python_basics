j = 1
k = 0
while j <= 10:
    inp = input("Enter a number: ")
    i = int(inp)
    if i%2 == 0:
        k = k + 1
    j = j + 1
print ("You Entered", k, "Even Numbers!" )
