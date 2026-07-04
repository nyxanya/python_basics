import math
pos_inf = math.inf
neg_inf = -math.inf

def is_smallest(s):
    x = math.inf
    for element_of_list in s:
        if element_of_list < x:
            x = element_of_list
    return x






def main():
    l = [5,6,7,8]
    print("Second smallest of", l, " should be 5 is ", is_smallest(l))
    l = [500, 600, 7000, 80000]
    print("Second smallest of", l, " should be 500 is ", is_smallest(l))
    l = [51, 16, 70000, 8999]
    print("Second smallest of", l, " should be 16 is ", is_smallest(l))
    l = [18, 6, 100, 19]
    print("Second smallest of", l, " should be 6 is ", is_smallest(l))
    l = [5, 6, 7, 8]
    print("Second smallest of", l, " should be 5 is ", is_smallest(l))


if __name__ == "__main__":
    main()