import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int k = 15;
        int[] coins = {1, 5, 12};

        System.out.println(s.solution(k, coins));
    }
}

class Solution {
    public int solution(int k, int[] coins) {

        int[] dp = new int[k + 1];
        Arrays.fill(dp, k+1);
        dp[0] = 0;
    
        for(int coin : coins){

            for(int i = coin; i <= k; i++){
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }

        if(dp[k] == k + 1)
            dp[k] = -1;

        return dp[k];
    }
}