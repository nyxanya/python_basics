from num2array import num_array


def num_array(l):
    list = []
    while l > 0:
        k = l % 10
        l = l // 10
        list.append(k)
    return list


def is_palindrome(l):
    if l < 0:
        return False
    l = num_array(l)
    i = 0
    j = len(l) - 1
    while i <= j:
        print("i =", i, "j=", j, "l =", l)
        if l[i] != l[j]:
            return False
        i += 1
        j -= 1
    return True

        
def main():
    print(is_palindrome(121), "should be True")
    print(is_palindrome(-121), "should be False")
    print(is_palindrome(345), "should be False")
    print(is_palindrome(1000021), "should be False")
    print(is_palindrome(1234321), "should be True")

if __name__ == "__main__":
    main()