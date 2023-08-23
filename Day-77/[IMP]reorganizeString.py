# 767. Reorganize String
# Medium
# 7.6K
# 226
# Companies

# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

# Return any possible rearrangement of s or return "" if not possible.

 

# Example 1:

# Input: s = "aab"
# Output: "aba"

# Example 2:

# Input: s = "aaab"
# Output: ""

 

# Constraints:

#     1 <= s.length <= 500
#     s consists of lowercase English letters.

# Accepted
# 320.5K
# Submissions
# 592.8K
# Acceptance Rate
# 54.1%


import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        heap = []
        freq = {}

        for letter in s : 
            if letter in freq :
                freq[letter] += 1 
            else :
                freq[letter] = 1 

        for key in freq :
            heapq.heappush(heap,(-freq[key],key))

        ans = []

        if max(list(freq.values())) > (len(s) + 1) // 2 :
            return ""
        
        while len(heap) >= 2 :

            f1 , letter1 = heapq.heappop(heap)
            f2 , letter2 = heapq.heappop(heap)

            ans.append(letter1)
            ans.append(letter2)

            if f1 + 1 < 0 :
                heapq.heappush(heap,(f1+1,letter1))

            if f2 + 1 < 0 :
                heapq.heappush(heap,(f2+1,letter2))
            
        if heap:
            f1,letter = heapq.heappop(heap)
            ans.append(letter)
        
        return "".join(ans)



            