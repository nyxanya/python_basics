
def is_monotonic(l):
    # l = [1, 2, 3, 4]
    i = 0
    k = 1
    while len(l) > k:
        # print(i,k)
        # if k < len(l):
        if l[i] < l[k]:
            return False
        i = i + 1
        k = k + 1
    return True



def main():
    print(is_monotonic([5,3,2,1]), "should be True")
    print(is_monotonic([6,2,3]), "should be False")
    print(is_monotonic([1,3,2,2,3]), "should be False")
    print(is_monotonic([6,5,4,3,2,1,0]), "should be True")
    print(is_monotonic([6,5,4,3,7,2,1]), "should be False")

if __name__ == "__main__":
    main()