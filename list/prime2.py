
def is_prime(num):
    if num < 2:
        return False
    if num <= 3:
        return True
    i = 2
    while i <= num//i:
        if num%i == 0:
            return False
        i = i + 1

    return(True)
# 35,742,549,198,872,617,291,353,508,656,626,642,567

def main():

    print(f"Is prime(25) == {is_prime(25)}")
    print(f"Is prime(125) == {is_prime(125)}")
    print(f"Is prime(27) == {is_prime(27)}")
    print(f"Is prime(29) == {is_prime(29)}")
    print(f"Is prime(251) == {is_prime(251)}")
    
if __name__ == "__main__":
    main()