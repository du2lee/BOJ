import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int[] costs = {6, 10, 13, 9, 8, 1};

        System.out.println(s.solution(costs));
    }
}

class Solution {
    public long solution(int[] reward) {

        int N = reward.length;  // n

        long[][] dp = new long[N + 1][3];

        dp[1][1] = reward[0];
        dp[1][2] = reward[0];
        
        for(int i = 2; i <= N ; i++){
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][0] = Math.max(dp[i - 1][2], dp[i][0]);

            dp[i][1] = dp[i - 1][0] + reward[i - 1];

            dp[i][2] = dp[i - 1][1] + reward[i - 1];
        }

        long answer = Math.max(dp[N][0], dp[N][1]);
        answer = Math.max(dp[N][2], answer);
        
        return answer;
    }
}

