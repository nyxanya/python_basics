
class Solution:
    def searchInsert(self, arr: list[int], num: int) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = (l + h) // 2
            if num < arr[m]:
                h = m - 1
            elif num > arr[m]:
                l = m + 1
            else:
                return m
        # print(l, h)
        return l
    
    
    
    
    
    
    
    
    
    # while
    #     i = len(arr)/2
    #     if arr[i] == num:
    #         return True
    #     elif arr[i] < num:
    #         len(arr) = 



def main():
    s = Solution()
    print(s.searchInsert([1,3,5,6], 5), "should be 2")
    print(s.searchInsert([1,3,5,6], 2), "should be 1")
    print(s.searchInsert([1,3,5,6], 7), "should be 4")
    
if __name__== "__main__":
     main()