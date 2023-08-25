# 68. Text Justification
# Hard
# 3.2K
# 4.2K
# Companies

# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

# For the last line of text, it should be left-justified, and no extra space is inserted between words.

# Note:

#     A word is defined as a character sequence consisting of non-space characters only.
#     Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#     The input array words contains at least one word.

 

# Example 1:

# Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:

# Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
# Note that the second line is also left-justified because it contains only one word.

# Example 3:

# Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

 

# Constraints:

#     1 <= words.length <= 300
#     1 <= words[i].length <= 20
#     words[i] consists of only English letters and symbols.
#     1 <= maxWidth <= 100
#     words[i].length <= maxWidth


from math import ceil
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        output = []
        words1 = [[words[i]] for i in range(len(words))]
        prev = 0

        for i in range(len(words)-1,-1,-1):
            textwidth = len(words[i])
            words1[i].append(textwidth)
            words1[i].append(prev)
            prev = textwidth
        
        
        i , j = 0 , 0 
        currwidth = words1[0][1]
        currsentence = ""

        while j < len(words1):
            if currwidth + words1[j][2] + j-i+1 <= maxWidth :
                currwidth += words1[j][2] 
                j+=1
                continue
            
            if j-i == 0 :
                currsentence+=words[i] + " "*(maxWidth-currwidth)
                output.append(currsentence)
                currwidth = words1[j][2]
                currsentence = ""
                i=j+1
                j=j+1
                continue 
            
            extraspaces = (maxWidth - currwidth) % (j-i)
            minspace = (maxWidth - currwidth) // (j-i)

            for k in range(i,j):
                if extraspaces > 0 :
                    currsentence += words[k] + " "*(minspace+1)
                    extraspaces-=1
                else :
                    currsentence += words[k] + " "*(minspace)
                
            currsentence += words[j]

            output.append(currsentence)
            currwidth = words1[j][2]
            currsentence = ""
            i=j+1
            j=j+1

        
        if i == j :
            return output
            
        currsentence = " ".join(words[i:j]) + " "*(maxWidth-currwidth-(j-1-i))
        output.append(currsentence)
        
            
            
        return output
            


        



