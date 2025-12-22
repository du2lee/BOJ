import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int[] costs = {1,2,3,1};

        System.out.println(s.solution(costs));
    }
}

class Solution {
    public int solution(int[] money) {
        int N = money.length;

        // 처음이 포함되는 케이스
        int[][] dp = new int[N][2];

        dp[0][1] = money[0];

        for(int i = 1; i < N - 1; i++){
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1]);
            dp[i][1] = dp[i - 1][0] + money[i];
        }

        int answer1 = Math.max(dp[N - 2][0], dp[N - 2][1]);


        // 처음이 포함되지 않는 케이스
        int[][] dp1 = new int[N][2];

        dp1[1][1] = money[1];

        for(int i = 2; i < N; i++){
            dp1[i][0] = Math.max(dp1[i - 1][0], dp1[i - 1][1]);
            dp1[i][1] = dp1[i - 1][0] + money[i];
        }

        int answer2 = Math.max(dp1[N - 1][0], dp1[N - 1][1]);

        return Math.max(answer1, answer2);

    }
}

