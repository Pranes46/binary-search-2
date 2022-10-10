class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums)-1
        
        
        if nums[low]<=nums[high]:   #to check whether the list is purely sorted or not, if it is sorted return nums[low]
            return nums[low]
        
        
        while low<=high:    #if the low pointyer crosses the high pointer the loop will break
            mid = low+(high-low)//2  #to avoid integer overflow we are calculating mid by this method
            
            if nums[mid]>nums[mid+1]:   #we are checking whether the mid element is gretaer than mid's next element if so we are returning mid+1 element
                return nums[mid+1]
            
            elif nums[low]<=nums[mid]:  #if the low is less than mid we are moving the low pointer to mid+1
                low = mid+1
                
            else:   #if the high is less than mid we are moving the high pointer to mid-1
                high = mid-1
                
        return 23112
        
        
        