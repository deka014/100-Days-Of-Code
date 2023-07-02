class Solution:
    def groupAnagrams(self, strs):

        result = {}

        for word in strs:

            sortedword = ''.join(sorted(word))

            if sortedword in result:

                result[sortedword].append(word)
            else :
                
                result[sortedword] = [word]


        return list(result.values())
        