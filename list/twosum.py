


def find_twosum(l, t):
    i = 0
    while i < len(l):
        k = i + 1
        # print(l[k], l[i])
        while k < len(l):
            if l[i] + l[k] == t:
                return [i, k]
            k += 1
        i += 1



def main():
    print(find_twosum(l =[2, 7, 11, 15], t = 18) , "Should be [1, 2]")
    print(find_twosum(l =[3, 2, 4], t = 6), "Should be [1, 2]")
    print(find_twosum(l = [3, 3], t = 6) , "Should be [0, 1]")
    


if __name__ == "__main__":
    main()