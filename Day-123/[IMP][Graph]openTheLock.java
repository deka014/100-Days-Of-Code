// . Open the Lock
// Solved
// Medium
// Topics
// Companies
// Hint

// You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

// The lock initially starts at '0000', a string representing the state of the 4 wheels.

// You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

// Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 

// Example 1:

// Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
// Output: 6
// Explanation: 
// A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
// Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
// because the wheels of the lock become stuck after the display becomes the dead end "0102".

// Example 2:

// Input: deadends = ["8888"], target = "0009"
// Output: 1
// Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".

// Example 3:

// Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
// Output: -1
// Explanation: We cannot reach the target without getting stuck.

 

// Constraints:

//     1 <= deadends.length <= 500
//     deadends[i].length == 4
//     target.length == 4
//     target will not be in the list deadends.
//     target and deadends[i] consist of digits only.

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    record Pair(int moves , String currentState){};
    public int openLock(String[] deadends, String target) {

        Queue<Pair> pq = new ArrayDeque<>();
        pq.offer(new Pair(0,"0000"));
        Set<String> deadStateSet = new HashSet<>();
        
        for(String ds : deadends){
            if (ds.equals("0000")) return -1;
            deadStateSet.add(ds);
        }


          deadStateSet.add("0000");

        while (!pq.isEmpty()){
            
            Pair currPair = pq.poll();

            if(currPair.currentState().equals(target)){
                return currPair.moves();
            }

            for (int offset = 0 ; offset < 4 ; offset++){
                StringBuilder currStateSB = new StringBuilder(currPair.currentState());
                
                int oldDigitInt = currStateSB.charAt(offset) - '0';
                int newDigitInt = (oldDigitInt+1) % 10;
                int newPrevDigitInt = ((oldDigitInt-1) + 10 ) % 10;
                char newDigitCharNext = (char) (newDigitInt + '0');
                char newDigitCharPrev = (char) (newPrevDigitInt + '0');
                currStateSB.setCharAt(offset,newDigitCharNext);

                if(!deadStateSet.contains(currStateSB.toString())){
                    deadStateSet.add(currStateSB.toString());
                    pq.offer(new Pair(currPair.moves()+1,currStateSB.toString()));
                }

                currStateSB.setCharAt(offset,newDigitCharPrev);

                if(!deadStateSet.contains(currStateSB.toString())){
                    deadStateSet.add(currStateSB.toString());
                     pq.offer(new Pair(currPair.moves()+1,currStateSB.toString()));
                }

            } 

        }   
        return -1;

    }
}


// 0202    deadend = 4  0000 0100 0101 0201 0202 

//             00                          suppose 10 is deadend
//         01      10
//     11                 20
//                             21
// 21        


// x+ & 10 


        
