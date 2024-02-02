# 1291. Sequential Digits
# Medium
# 2.5K
# 154
# Companies

# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

# Example 1:

# Input: low = 100, high = 300
# Output: [123,234]

# Example 2:

# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]

 

# Constraints:

#     10 <= low <= high <= 10^9

# Accepted
# 160.1K
# Submissions
# 248.9K

from collections import deque

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        q = deque(range(1,9))
        

        ans = []

        while q:

            temp = q.popleft()

            if temp >= low and temp<=high:
                ans.append(temp)

            
            lastdigit = temp%10

            if lastdigit + 1 <= 9 :
                q.append(temp * 10 + (lastdigit + 1))


        return ans

    

