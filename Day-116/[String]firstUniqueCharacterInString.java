import java.util.HashMap;
import java.util.Map;

// # 387. First Unique Character in a String
// # Easy
// # 8.7K
// # 282
// # Companies

// # Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

// # Example 1:

// # Input: s = "leetcode"
// # Output: 0

// # Example 2:

// # Input: s = "loveleetcode"
// # Output: 2

// # Example 3:

// # Input: s = "aabb"
// # Output: -1

 

// # Constraints:

// #     1 <= s.length <= 105
// #     s consists of only lowercase English letters.

// # Accepted
// # 1.6M
// # Submissions
// # 2.6M
// # Acceptance Rate
// # 61.5%

class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer> mp = new HashMap<>();

        for (char c : s.toCharArray()){
            if (mp.containsKey(c)){
                mp.put(c,mp.get(c)+1);
            }else{
                mp.put(c,1);
            }
        }

        for (int i = 0 ; i<s.length();i++){
            if (mp.get(s.charAt(i)) == 1 ){
                return i;
            }
        }

        return -1;
    }
}