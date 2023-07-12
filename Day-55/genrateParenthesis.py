# 22. Generate Parentheses
# Medium
# 18.7K
# 753
# Companies

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

 

# Constraints:

#     1 <= n <= 8

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        length = n*2
        output = []

        def recsolution(index,leftpar,rightpar,temp):

            if index >= length :
                output.append(temp)
                return
            
            if leftpar > 0 : 
                recsolution(index+1,leftpar-1,rightpar,temp+"(")
            
            if rightpar > 0 and rightpar - leftpar > 0 :

                recsolution(index+1,leftpar,rightpar-1,temp+")")

        recsolution(0,n,n,"")

        return output

