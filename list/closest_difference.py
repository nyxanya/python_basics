import math

def closest_difference(l, t):
    # print("l = ", l, "t = ", t)
    min = math.inf
    i = 0
    while i < len(l):
        j = i + 1
        # print(i, j, l[i], l[j])
        while j < len(l):
            sum = l[i] + l[j]
            diff = abs(sum - t)
            # print(i, j, l[i], l[j], sum, diff, min)
            if diff < min:
                min = diff
                Ri = i
                Rj = j
            j += 1
        i += 1
    return [Ri, Rj]




def main():
    print(closest_difference(l =[12, 18, 22, 14, 5], t = 32) , "Should be [1, 3]")
    print(closest_difference(l =[4, 9, 1, 15], t = 13), "Should be [0, 1]")
    print(closest_difference(l = [2, 5, 11, 20], t = 14) , "Should be [0, 2]")
    


if __name__ == "__main__":
    main()