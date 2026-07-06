
def is_monotonic(l):
    # l = [1, 2, 3, 4]
    i = 0
    k = 1
    while len(l) > k:
        # print(i,k)
        # if k < len(l):
        if l[i] > l[k]:
            return False
        i = i + 1
        k = k + 1
    return True



def main():
    print(is_monotonic([1,2,2,3]), "should be True")
    print(is_monotonic([6,2,2,3]), "should be False")
    print(is_monotonic([1,3,2,2,3]), "should be False")
    print(is_monotonic([1,2,2,3,3,3,3,3]), "should be True")
    print(is_monotonic([1,1,1,1,1,2,2,2,2,2,2,3]), "should be True")

if __name__ == "__main__":
    main()