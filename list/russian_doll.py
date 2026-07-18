import math

[3, 2, 1]
def rds(l, t):
    i = 0
    min = math.inf
    while len(l) > i:
        j = i + 1
        while len(l) > j:
            sum = abs(l[i] + l[j] - t)
            if sum < min:
                min = sum
                Ri = i 
                Rj = j
                print(sum)
            print(l[i] + l[j], i , j)
            j += 1
        i += 1 
    return [Ri, Rj]



def main():
    print(rds(l =[12, 18, 22, 14, 5], t = 32) , "Should be [1, 3]")
    print(rds(l =[4, 9, 1, 15], t = 13), "Should be [0, 1]")
    print(rds(l = [2, 5, 11, 20], t = 14) , "Should be [0, 2]")
    


if __name__ == "__main__":
    main()