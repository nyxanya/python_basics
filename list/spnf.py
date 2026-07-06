from is_fact import is_fact
from prime2 import is_prime
from smallest import is_smallest

def prime_factors(l):
    primes = set()
    num = 0
    np = set()
    for element_of_list in l:
        y = is_fact(element_of_list)
        # print("factors =", y)
        for factor in y:
            if is_prime(factor):
                primes.add(factor)

        # print("The set of primes after ",element_of_list, "is :", primes)
    return primes

def smallest_prime(l):
    s = prime_factors(l)
    k = 2
    
    while True:
        if is_prime(k):
            if k not in s:
                return k
        k = k + 1
        
    #find factors 
    #find primes not equal to factors
    #find smallest
        

# for p in y:
#             primes.add(p)
#     primes.pop()
#     print(primes)
#     answer = primes.pop()
#     return answer


def main():
    print (smallest_prime([10, 20, 30]), "should be 7")
    print (smallest_prime([49, 121, 343]), "should be 2")
    print (smallest_prime([25, 125, 49, 121]), "should be 2")
    print (smallest_prime([64, 121, 1001]), "should be 3")

if __name__ == "__main__":
    main()



