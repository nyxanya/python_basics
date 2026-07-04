from is_fact import is_fact
from prime2 import is_prime
from smallest import is_smallest

def smallest_prime(l):
    primes = set()
    num = 0
    for element_of_list in l:
        y = is_fact(element_of_list)
        # print("factors =", y)
        for factor in y:
            if is_prime(factor):
                primes.add(factor)
            # print("The set of primes after ",element_of_list, "is :", primes)
    prime = is_smallest(primes)
    return prime

        
# for p in y:
#             primes.add(p)
#     primes.pop()
#     print(primes)
#     answer = primes.pop()
#     return answer


def main():
    print (smallest_prime([10, 20, 30]), "should be 2")
    print (smallest_prime([49, 121, 343]), "should be 7")
    print (smallest_prime([25, 125, 49, 121]), "should be 5")
    print (smallest_prime([64, 121, 1001]), "should be 2")
 

if __name__ == "__main__":
    main()

# how do i turn the list into a set


