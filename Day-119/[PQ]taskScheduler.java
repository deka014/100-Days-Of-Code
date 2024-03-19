// 621. Task Scheduler
// Solved
// Medium
// Topics
// Companies

// You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

// ​Return the minimum number of intervals required to complete all tasks.

 

// Example 1:

// Input: tasks = ["A","A","A","B","B","B"], n = 2

// Output: 8

// Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

// After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

// Example 2:

// Input: tasks = ["A","C","A","B","D","B"], n = 1

// Output: 6

// Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

// With a cooling interval of 1, you can repeat a task after just one other task.

// Example 3:

// Input: tasks = ["A","A","A", "B","B","B"], n = 3

// Output: 10

// Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

// There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.

 

// Constraints:

//     1 <= tasks.length <= 104
//     tasks[i] is an uppercase English letter.
//     0 <= n <= 100

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;

class Solution {

    class Pair {
        char letter;
        int count;
        public Pair(char letter , int count){
            this.letter = letter;
            this.count = count;
        }
    }
    
    public int leastInterval(char[] tasks, int n) {
        Queue<Pair> pq = new PriorityQueue<>((a,b)->Integer.compare(b.count,a.count));
        Map<Character,Integer> mpcount = new HashMap<>();
        int ans = 0;
        for (char l : tasks){
            mpcount.put(l,mpcount.getOrDefault(l,0)+1);
        }

        for (char c : mpcount.keySet()){
            pq.offer(new Pair(c,mpcount.get(c)));
        }

        while (!pq.isEmpty()){
            List<Pair> arrStore = new ArrayList<>();
            int taskcount = 0;
            int cycle = n+1;

            while(cycle>0 && !pq.isEmpty()){
                Pair pair = pq.poll();
                pair.count-=1;
                arrStore.add(pair);
                taskcount+=1;
                cycle-=1;
            }

            for (Pair pair : arrStore){
                if (pair.count>0){
                    pq.offer(pair);
                }
            }

            if (!pq.isEmpty() && cycle>0){
                ans+=taskcount+cycle;
            }
            else {
                ans+=taskcount;
            }

        }

        return ans;
    }
}