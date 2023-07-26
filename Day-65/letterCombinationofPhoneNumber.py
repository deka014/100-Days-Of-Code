# 17. Letter Combinations of a Phone Number
# Medium
# 15.8K
# 860
# Companies

# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

 

# Example 1:

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:

# Input: digits = ""
# Output: []

# Example 3:

# Input: digits = "2"
# Output: ["a","b","c"]

 

# Constraints:

#     0 <= digits.length <= 4
#     digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits :
            return []

        lettermap = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],
        ["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        numbers = [1]
        temp = 1
        for i in range(len(digits)-1,-1,-1):
            temp *= len(lettermap[int(digits[i])])
            numbers.append(temp)
        numbers.reverse()

        output = [""] * numbers[0]

        for i in range(len(digits)) : 
            letterindex = 0
            test = 0
            for j in range(numbers[0]):
             
                output[j] += lettermap[int(digits[i])][test//numbers[i+1]]
                if test >= numbers[i] - 1 :
                    test = 0 
                else :
                    test+=1
        
        return output




