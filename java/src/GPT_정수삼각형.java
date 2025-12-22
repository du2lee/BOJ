import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {

        int[][] triangle = { {7}, {3, 8}, {8, 1, 0}, {2, 7, 4, 4}, {4, 5, 2, 6, 5} };

        Solution c = new Solution();

        System.out.println(c.solution(triangle));

    }
}

class Solution {
    public int solution(int[][] triangle) {

        int N = triangle.length;

        int[] dp = new int[N];

        dp[0] = triangle[0][0];

        for(int i = 1; i < N; i++){
            for(int j = i; j >= 0; j--){
                if (j == 0)    // 시작 부분
                    dp[j] = dp[j] + triangle[i][j];
                else if(i == j)  // 끝 부분
                    dp[j] = dp[j - 1] + triangle[i][j]; 
                else
                    dp[j] = Math.max(dp[j - 1], dp[j]) + triangle[i][j];
            }
        }

        int answer = 0;

        for(int v : dp){
            answer = Math.max(answer, v);
        }

        return answer;
    }
}