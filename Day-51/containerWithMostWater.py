class Solution:
    def maxArea(self, height) :
        output = 0
        breadth = len(height) - 1
        ptr1 = 0
        ptr2 = len(height) - 1 

        while ptr1 < ptr2 : 

            output = max(breadth*min(height[ptr1],height[ptr2]) , output ) 

            if height[ptr2] < height[ptr1] :
                ptr2-=1
            else :
                ptr1+=1
            
            breadth-=1

        return output   