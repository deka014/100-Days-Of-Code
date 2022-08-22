# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

#     0 <= a, b, c, d < n
#     a, b, c, and d are distinct.
#     nums[a] + nums[b] + nums[c] + nums[d] == target

# You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:

# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        # this can be solved using three pointer with binary search which may create duplicates so set
        # needs to be used 
        # or 
        # 2 pointer with left and right --> it will not create duplicate
        
        class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        # this can be solved using three pointer with binary search which may create duplicates so set
        # needs to be used 
        # or 
        # 2 pointer with left and right --> it will not create duplicate
        

        # the below Solution is not handeling duplicates
        def threePointerApproach():
            output = []
            i = 0
            N = len(nums)
            nums.sort()
            
            while i < N :
                j = i+1
                while j < N :
                    k=j+1
                    while k < N :
                        rem = target - (nums[i] + nums[j] + nums[k])
                        l = k+1
                        r = N-1
                        while l <= r :
                            mid = (l+r) // 2
                            if nums[mid] == rem :
                                output.append([nums[i],nums[j],nums[k],nums[mid]])
                                break
                            elif nums[mid] < rem :
                                l = mid + 1
                            else :
                                r = mid - 1
                        
                        k+=1 
                    j+=1
                i+=1 
            return list(set(map(tuple,output) ))
                  
                        
        
        return threePointerApproach()


        # the below Solution is by handeling duplicates

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        # this can be solved using three pointer with binary search which may create duplicates so set
        # needs to be used 
        # or 
        # 2 pointer with left and right --> it will not create duplicate
        
        def threePointerApproach():
            output = []
            i = 0
            N = len(nums)
            nums.sort()
            
            while i < N :
                j = i+1
                while j < N :
                    k=j+1
                    while k < N :
                        rem = target - (nums[i] + nums[j] + nums[k])
                        l = k+1
                        r = N-1
                        while l <= r :
                            mid = (l+r) // 2
                            if nums[mid] == rem :
                                output.append([nums[i],nums[j],nums[k],nums[mid]])
                                break
                            elif nums[mid] < rem :
                                l = mid + 1
                            else :
                                r = mid - 1
                        while k < N-1 and nums[k+1] == nums[k]:
                            k+=1
                        k+=1 
                    while j < N-1 and nums[j+1] == nums[j]:
                            j+=1
                    j+=1
                while i < N-1 and nums[i+1] == nums[i]:
                            i+=1
                i+=1 
            return output
                  
                        
        
        return threePointerApproach()