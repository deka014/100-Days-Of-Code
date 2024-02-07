import java.util.ArrayList;
import java.util.HashMap;

// 451. Sort Characters By Frequency
// Medium
// 7.9K
// 271
// Companies

// Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

// Return the sorted string. If there are multiple answers, return any of them.

 

// Example 1:

// Input: s = "tree"
// Output: "eert"
// Explanation: 'e' appears twice while 'r' and 't' both appear once.
// So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

// Example 2:

// Input: s = "cccaaa"
// Output: "aaaccc"
// Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
// Note that "cacaca" is incorrect, as the same characters must be together.

// Example 3:

// Input: s = "Aabb"
// Output: "bbAa"
// Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
// Note that 'A' and 'a' are treated as two different characters.

 

// Constraints:

//     1 <= s.length <= 5 * 105
//     s consists of uppercase and lowercase English letters and digits.

// Accepted
// 675.2K
// S

class Solution {
    public String frequencySort(String s) {

        HashMap<Character,Integer> count = new HashMap<>();
        HashMap<Integer,ArrayList<Character>> grouping = new HashMap<>();
        StringBuilder ans = new StringBuilder();
        for (char c : s.toCharArray()){
            count.put(c,count.getOrDefault(c,0)+1);
        }

        count.forEach((c,num)->{
            if (grouping.containsKey(num)){
                grouping.get(num).add(c);
            }
            else {
                ArrayList<Character> toadd = new ArrayList<>();
                toadd.add(c);
                grouping.put(num,toadd);
            }
        });
        
        for (int i = s.length(); i>=1;i--){
            final int countint = i;
            if (grouping.containsKey(i)){
                grouping.get(i).forEach(val->{
                    
                    for (int j = 0 ; j<countint ; j++){
                        ans.append(val);
                }
                });
                
            }
        }


        return ans.toString();


        
    }
}