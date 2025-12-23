import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int[] costs = {10, 20, 15, 25, 10, 20};

        System.out.println(s.solution(costs));
    }
}

class Solution {
    public int solution(int[] score) {
        int N = score.length;
        
        int[][] dp = new int[N][3];

        dp[0][1] = score[0];
        dp[0][2] = Integer.MAX_VALUE / 5;

        dp[1][1] = score[1] + score[2];
        dp[1][2] = score[1];

        for(int i = 2; i < N; i++){
            dp[i][1] = dp[i -1][2] + score[i];
            dp[i][2] = Math.max(dp[i - 2][1], dp[i - 2][2]) + score[i];
        }
        
        return Math.max(dp[N - 1][1], dp[N - 1][2]);
    }
}


