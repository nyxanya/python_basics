

def find_difference(l1, l2):
    i = 0
    d1 = set()
    while len(l1) > i:
        if l1[i] not in l2:
            d1.add(l1[i])
        i += 1

    i = 0
    d2 = set()
    while len(l2) > i:
        if l2[i] not in l1:
            d2.add(l2[i])
        i += 1
    return list(d1), list(d2)



def main():
    print(find_difference(l1 =[1, 2, 3], l2 =[2, 4, 6]) , "Should be [[1,3],[4,6]]")
    print(find_difference(l1 =[1, 2, 3, 3], l2 =[1, 1, 2, 2]), "Should be [[3],[]]")
    print(find_difference([1, 2, 3, 4], [1, 2, 3, 4]) , "Should be [[][]]")
    print(find_difference(l1 =[1, 3, 4], l2 =[6, 4]) , "Should be [[1, 3], [6]]")
    print(find_difference(l1 =[1, 2, 3, 4], l2 =[4, 3, 2, 1 ]) , "Should be [[][]]")



if __name__ == "__main__":
    main()