// 85. Maximal Rectangle
// Solved
// Hard
// Topics
// Companies

// Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

// Example 1:

// Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
// Output: 6
// Explanation: The maximal rectangle is shown in the above picture.

// Example 2:

// Input: matrix = [["0"]]
// Output: 0

// Example 3:

// Input: matrix = [["1"]]
// Output: 1

 

// Constraints:

//     rows == matrix.length
//     cols == matrix[i].length
//     1 <= row, cols <= 200
//     matrix[i][j] is '0' or '1'.

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maximalRectangle(char[][] matrix) {
        int n = matrix.length;
        int m = matrix[0].length;
        int ans = 0;
        int[] cumHistogram = new int[m];

        for (int i = 0 ; i<n ; i++){
            for (int j = 0 ; j<m ; j++){
                char val = matrix[i][j];
                if (val == '0'){
                    cumHistogram[j] = 0 ;
                }else {
                    cumHistogram[j] += 1 ;
                }
            }

            ans = Math.max(ans,findAns(cumHistogram,m));
        }
        return ans;
    }

    public int findAns(int[] cumHistogram , int n){
        int ans = 0;
        // right smaller element- index (NSR)
        int [] nsr = new int[n];
        //left smaller element - index  (NSL)
        int [] nsl = new int[n];
        Deque<Integer> stack = new ArrayDeque<>();

        //creating nsr first

        for (int i = n-1 ; i >= 0 ; i--){
            int val = cumHistogram[i];
            
            while(!stack.isEmpty() && val <= cumHistogram[stack.peek()]){
                stack.pop();
            }
            if (stack.isEmpty()){
                nsr[i] = n;
             }else {
                nsr[i] = stack.peek(); //                      
             }

             stack.push(i);
        }

        stack.clear();
        //creating nsl 

        for (int i = 0 ; i < n ; i++){
            int val = cumHistogram[i];
            
            while(!stack.isEmpty() && val <= cumHistogram[stack.peek()]){
                stack.pop();
            }
            if (stack.isEmpty()){
                nsl[i] = -1;
             }else {
                nsl[i] = stack.peek(); //                      
             }

             stack.push(i);
        }

        for (int i = 0 ; i <n ; i++ ){
            ans = Math.max(ans,(nsr[i] - nsl[i] - 1)*cumHistogram[i]);
        }

        return ans;

    }
}
