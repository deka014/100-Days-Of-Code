# 1160. Find Words That Can Be Formed by Characters
# Easy
# 1.7K
# 163
# Companies

# You are given an array of strings words and a string chars.

# A string is good if it can be formed by characters from chars (each character can only be used once).

# Return the sum of lengths of all good strings in words.

 

# Example 1:

# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:

# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

 

# Constraints:

#     1 <= words.length <= 1000
#     1 <= words[i].length, chars.length <= 100
#     words[i] and chars consist of lowercase English letters.

# Accepted
# 182.3K
# Submissions
# 264.6K
# Acceptance Rate
# 68.9%

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        carray = [0 for _ in range(0,26)]       
        ans = 0
        for c in chars :
            carray[ord("a") - ord(c)] += 1
        temp = carray[:]

        for word in words :
            canadd = True
            for c in word:
                index = ord("a") - ord(c)
                if temp[index] <= 0 :
                    canadd = False
                    break
                else :
                    temp[index] -= 1
            

            if canadd :
                ans+=len(word)
            temp = carray[:]

        return ans



