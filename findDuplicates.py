class Solution:
    def findDuplicates(self, nums):
        duplicateNumbers = []
        i=0
        while(i<len(nums)):
            j=nums[i]-1
            if(nums[i]!=nums[j]):
                nums[i],nums[j] = nums[j],nums[i]
            else:
                i+=1
        for i in range(len(nums)):
            if(nums[i]!=i+1):
                duplicateNumbers.append(nums[i])
        return duplicateNumbers
      
      
# Time complexity - O(N)
# Space complexity - O(1)
