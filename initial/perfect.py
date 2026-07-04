
def is_perfect(n):
    i = 1
    j = 0
    f = []
    while n>i:
        if n%i == 0:  
            f.append(i)
            j = j + i
        i = i + 1

    if j == n:
        print(f, "+")
        return True
    else:
        return False

while True:
    try:
        num = int(input("Enter a number: "))
        if num < 1:
            print("Please enter a positive integer.")
            continue
        else:
            if(is_perfect(num)):
                print(f"{num} is a perfect number.")
            else:
                print(f"{num} is not a perfect number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")