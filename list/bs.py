
class Solution:
    def search(self, arr: list[int], num: int) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = (l + h) // 2
            if num < arr[m]:
                h = m - 1
            elif num > arr[m]:
                l = m + 1
            else:
                return True
        return False
    
    
    
    
    
    
    
    
    
    # while
    #     i = len(arr)/2
    #     if arr[i] == num:
    #         return True
    #     elif arr[i] < num:
    #         len(arr) = 



def main():
    s = Solution()
    print(s.search([1,2,3,4,5,6,7,8,9,10], 8), "should be true")
    print(s.search([1,2,3,4,5,6,7,8,9,10], 18), "should be false")

if __name__== "__main__":
     main()