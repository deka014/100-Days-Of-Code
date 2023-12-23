import java.util.*;
class Solution {

    public class Pair<T,M> {
        T x;
        M y;
        public Pair(T x , M y){
            this.x = x;
            this.y = y;
        }
    }
    public boolean isPathCrossing(String path) {
        HashSet<Pair<Integer,Integer>>  visited = new HashSet<>();
        visited.add(new Pair<>(0,0));
        int x = 0;
        int y = 0;
        for (char c : path.toCharArray()){
            
            if (c == 'N'){
                y+=1;
            }
            else if (c == 'E'){
                x+=1;
            }
            else if (c == 'S'){
                y-=1;
            }
            else {
                x-=1;
            }

            Pair<Integer,Integer> newPair = new Pair(x,y);
            if (visited.contains(newPair)){
                return true;
            }
            visited.add(newPair);
        }

        return false;

    }
}
