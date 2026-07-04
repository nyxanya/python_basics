import math
pos_inf = math.inf
neg_inf = -math.inf

j = 1
k = 0
x = math.inf
while j <= 10:
    inp = input("Enter a number: ")
    i = int(inp)
    if i < x:
        x = i
    j = j + 1
print (x, "Is The Smallest Number!") 
