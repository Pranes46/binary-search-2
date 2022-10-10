class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        if len(nums) == 1:  #if the length of num is 1 we are returning 0
            return 0
        low = 0   #setting our low pointer on index 0
        high = len(nums)-1  #setting my high pointer on last index
        
        while (low<=high):  #the loop will run untill the low pointer crosses the high pointer
            
            mid = low+(high-low)//2  #to avoid integer overflow we are calculating mid in this way
            
            if (mid == 0 or nums[mid-1] < nums[mid]) and (mid==len(nums)-1 or nums[mid+1] < nums[mid] ):  # to avoid the index over bound we are checking the mid is == 0 and mid is == last index after that we are checking whtehr the mid value is greater than the mid+1 and mid-1 if it is greater then that element is the poptential peak element so we are returning the index  
                return mid
            
            elif (mid > 0 and nums[mid-1]> nums[mid]):  #if the mid-1 is greater we are moving our high to mid -1
                high = mid-1
                
            else:
                low = mid+1  # else we are moving our low pointer to mid +1
                
        return 99
        
        
        
        
            
            
        