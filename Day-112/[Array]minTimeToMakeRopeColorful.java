class Solution {
    public int minCost(String colors, int[] neededTime) {
        int ans = neededTime[0];
        char prev = colors.charAt(0);
        int maxtime = neededTime[0];

        for (int i = 1;i<colors.length();i++){
            
            ans+=neededTime[i];

            if (colors.charAt(i) == prev){
                maxtime = Math.max(maxtime,neededTime[i]);

            }
            else {
                ans-=maxtime;
                prev = colors.charAt(i);
                maxtime = neededTime[i];
            }
        }

        ans-=maxtime;
        return ans;
    }
}