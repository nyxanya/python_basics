
def num_array(l):
    list = []
    while l > 0:
        k = l % 10
        l = l // 10
        list.append(k)
    return list


    


# def main():
#     print(num_array2(121), "should be [1, 2, 1]")
#     print(num_array2(234), "should be [2, 3, 4]")
#     print(num_array2(345), "should be [3, 4, 5]")
#     print(num_array2(10), "should be [1, 0]")
#     print(num_array2(1234), "should be [1, 2, 3, 4]")

def main():
    print(num_array(121), "should be [1, 2, 1]")
    print(num_array(234), "should be [4, 3, 2]")
    print(num_array(345), "should be [5, 4, 3]")
    print(num_array(10), "should be [0, 1]")
    print(num_array(1234), "should be [4, 3, 2, 1]")

if __name__ == "__main__":
    main()