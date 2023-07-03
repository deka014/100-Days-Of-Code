class Solution:
    def topKFrequent(self, nums, k) :
        output = []
        mapNums = {}
        for num in nums:
            if num in mapNums:
                mapNums[num] += 1
            else :
                mapNums[num] = 1

        
        freq = [[] for i in range(len(nums) + 1)]
        
        for key in mapNums : 
            freq[mapNums[key]].append(key)

        for i in range(len(freq) -1 , -1 , -1):
            
            for j in freq[i]:
                
                if len(output) == k :
                    return output
                
                output.append(j)
        
        return output
                








        


            
                    