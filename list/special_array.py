
def special_array(l):
    i = 0
    j = 1
    while len(l) > j:
        if l[i]%2 == 0 and l[j]%2 != 0 or l[j]%2 == 0 and l[i]%2 != 0:
            i += 1
            j += 1
        else:
            return False
    return True

def main():
    print(special_array([1, 2, 3, 4]) , "Should be True")
    print(special_array([1, 2, 3, 4, 6]), "Should be False")
    print(special_array([1, 2, 3, 4, 5, 6]) , "Should be True")
    print(special_array([1]) , "Should be True")
    print(special_array([2, 1, 4]) , "Should be True")
    print(special_array([4, 3, 1, 6]), "Should be False")


if __name__ == "__main__":
    main()
