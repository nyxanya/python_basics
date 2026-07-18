
# def is_mountain(l):
#     # l = [1, 2, 3, 4]
#     i = 0
#     k = 1
#     while len(l) > k:
#         # l[i] -> pervious number
#         # l[k] [0,2,3,4,5,4,2,1,0]
#         if l[i] > l[k] and k < len(l):
#             i = i + 1
#             k = k + 1
#             print(i, k, len(l)) 
#             if l[k] > l[i]:
#                 return False
#         elif l[i] == l[k]:
#             return False
#         else:
#             i = i + 1
#             k = k + 1
        
#     return True

def is_mountain(l):
    # l = [1, 2, 3, 4]
    i = 0
    k = 1
    # print(l)
    if l[0] >= l[1]:
        return False
    while len(l) > k:
        # print(i,k)
        # if k < len(l): 0, 2, 3, 3, 4, 5, 2, 1, 0
        #////
        if l[i] > l[k]:
            break
        elif l[i] == l[k]:
            return False
        i = i + 1
        k = k + 1
    print("exit: i=", i, "k=", k, "length", len(l))
    if len(l) == k:
        return False
    while len(l) > k:
        # print(i,k)
        # if k < len(l):
        if l[i] < l[k]:
            return False
        elif l[i] == l[k]:
            return False
        i = i + 1
        k = k + 1
    return True




def main():
    print(is_mountain([0,3,2,1]), "should be True")
    print(is_mountain([2,1]), "should be False")
    print(is_mountain([3,5,5]), "should be False")
    print(is_mountain([0,2,3,4,5,2,1,0]), "should be True")
    print(is_mountain([0,2,3,3,4,5,2,1,0]), "should be False")
    print(is_mountain([0,1,2,3,4,5,6,7,8,9]), "should be False")


if __name__ == "__main__":
    main()