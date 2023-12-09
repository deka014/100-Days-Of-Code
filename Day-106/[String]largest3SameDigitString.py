# 2264. Largest 3-Same-Digit Number in String
# Easy
# 923
# 41
# Companies

# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

#     It is a substring of num with length 3.
#     It consists of only one unique digit.

# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

#     A substring is a contiguous sequence of characters within a string.
#     There may be leading zeroes in num or a good integer.

 

# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".

# Example 2:

# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.

# Example 3:

# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

 

# Constraints:

#     3 <= num.length <= 1000
#     num only consists of digits.

# Accepted
# 127.9K
# Submissions
# 184.2K
# Acceptance Rate
# 69.5%

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        prev = num[0]
        count = 1
        ans = ""

        for digit in num[1:]:
            if digit == prev:
                count+=1
            else :
                prev = digit
                count = 1
                continue
        
            if count == 3 and prev > ans :
                ans = prev
            
        return ans+ans+ans