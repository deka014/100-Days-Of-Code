// You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

// For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

// Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

 

// Example 1:

// Input: arr = [1,2,3,5], k = 3
// Output: [2,5]
// Explanation: The fractions to be considered in sorted order are:
// 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
// The third fraction is 2/5.

// Example 2:

// Input: arr = [1,7], k = 1
// Output: [1,7]

 

// Constraints:

//     2 <= arr.length <= 1000
//     1 <= arr[i] <= 3 * 104
//     arr[0] == 1
//     arr[i] is a prime number for i > 0.
//     All the numbers of arr are unique and sorted in strictly increasing order.
//     1 <= k <= arr.length * (arr.length - 1) / 2

 
// Follow up: Can you solve the problem with better than O(n2) complexity?

import java.util.PriorityQueue;
import java.util.Queue;

class Solution {
    public record Data(int num , int den , float frac){}

    public int[] kthSmallestPrimeFraction(int[] arr, int k) {
        
        Queue<Data> pq = new PriorityQueue<>((l,m) -> Float.compare(l.frac,m.frac));
        int n = arr.length;

        for(int i = 0; i<n;i++){
            pq.offer(new Data(i,n-1,(float)arr[i]/arr[n-1]));
        }

        while(!pq.isEmpty()){
            Data currData = pq.poll();
            k-=1;
            if(k==0){
                return new int[]{arr[currData.num],arr[currData.den]};
            }
            int num = currData.num;
            int den = currData.den;

            if(den>num+1){
                pq.offer(new Data(num,den-1,(float)arr[num]/arr[den-1]));
            }
        }

        return new int[]{0,0};
    }
}