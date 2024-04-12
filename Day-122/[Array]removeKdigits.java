// 402. Remove K Digits
// Solved
// Medium
// Topics
// Companies

// Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

 

// Example 1:

// Input: num = "1432219", k = 3
// Output: "1219"
// Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

// Example 2:

// Input: num = "10200", k = 1
// Output: "200"
// Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

// Example 3:

// Input: num = "10", k = 2
// Output: "0"
// Explanation: Remove all the digits from the number and it is left with nothing which is 0.

 

// Constraints:

//     1 <= k <= num.length <= 105
//     num consists of only digits.
//     num does not have any leading zeros except for the zero itself.

// Seen this question in a real interview before?
// 1/5

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public String removeKdigits(String num, int k) {
        Deque<Character> stack = new ArrayDeque<>();
        String ans = "";
       
        int n = num.length();

         int anslen = n-k;
        if (n<=k){
            return "0";
        }

        for (int i = 0 ; i < n ; i++){
            while( k>0 && !stack.isEmpty() && stack.peek()>num.charAt(i)){
                stack.pop();
                k-=1;
            }
            if (!stack.isEmpty() || num.charAt(i) != '0'){
                stack.push(num.charAt(i));
            } 
        }

        while (!stack.isEmpty() && k > 0){
            stack.pop();
            k-=1;
        }

        while (!stack.isEmpty()){
            char toBeAdded = stack.pollLast();
            ans+=toBeAdded;
        }
        return ans.length() > 0 ? ans : "0";
    }
}

