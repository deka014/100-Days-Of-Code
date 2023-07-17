# 38. Count and Say
# Medium
# 3.3K
# 7K
# Companies

# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

#     countAndSay(1) = "1"
#     countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

# To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

# For example, the saying and conversion for digit string "3322251":

# Given a positive integer n, return the nth term of the count-and-say sequence.

 

# Example 1:

# Input: n = 1
# Output: "1"
# Explanation: This is the base case.

# Example 2:

# Input: n = 4
# Output: "1211"
# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = say "1" = one 1 = "11"
# countAndSay(3) = say "11" = two 1's = "21"
# countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1 :
            return "1"
        
        if n == 2 :
            return "11"

        prev = "11"

        for num in range(3,n+1) :
            temp = ""
            count = 1
            i = len(prev) - 2
            while i >= 0:
                if prev[i+1] == prev[i]:
                    count+=1
                else :
                    temp += (prev[i+1] + str(count))
                    count = 1 

                i-=1
            temp += (prev[i+1] + str(count))
            prev = temp[::-1]
        
        return prev



        
        