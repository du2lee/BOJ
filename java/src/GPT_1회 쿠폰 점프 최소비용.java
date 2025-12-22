import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int[] n = {5, 2, 4, 7, 3, 4, 1};

        System.out.println(s.solution(n));
    }
}

class Solution {
    public long solution(int[] cost) {
        int n = cost.length;

        long[] dp = new long[n + 1];
        dp[1] = cost[0];

        long[] dp1 = new long[n + 1]; // 쿠폰을 썼을 때 최소 값
        dp1[0] = Long.MAX_VALUE / 4; 
        dp1[1] = 0;

        for(int i = 2; i <= n; i++){
            dp[i] += dp[i - 1] + cost[i - 1];
            dp[i] = Math.min(dp[i], dp[i - 2] + cost[i - 1]);

            long tmp = Math.min(dp[i] - cost[i - 1], dp1[i - 1] + cost[i - 1]);

            dp1[i] = Math.min(tmp, dp1[i - 2] + cost[i - 1]);
        }
        return dp1[n];
    }
}