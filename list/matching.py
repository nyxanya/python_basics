
def find_matching(l):
    i = 0
    while i < len(l):
        k = i + 1
        while k < len(l):
            if l[i] == l[k]:
                return [i, k]
            k += 1
        i += 1


def main():
    print(find_matching(l =[2, 7, 11, 15, 11]) , "Should be [2, 4]")
    print(find_matching(l =[3, 2, 2, 4]), "Should be [1, 2]")
    print(find_matching(l = [3, 3]) , "Should be [0, 1]")
    print(find_matching(l = [3, 5, 6, 2, 7, 3, 8]) , "Should be [0, 5]")
    


if __name__ == "__main__":
    main()