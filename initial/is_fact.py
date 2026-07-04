
def is_fact(num):
    
    i = 1
    l = []
    while i <= num:
        if num%i == 0:
            l.append(i)
        i = i + 1
    
    return l

l = 0
while l < 100:
    try:
        num = int(input("Enter a number: "))
        if num < 1:
            print("Please enter a positive integer.")
            continue
        else:
            print(is_fact(num), "are the factors.")
            l = l + 1
            
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        

print(is_fact(10))