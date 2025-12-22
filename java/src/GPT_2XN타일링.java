import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int n = 5;

        System.out.println(s.solution(n));
    }
}

class Solution {
    public int solution(int n) {
        int[] dp = new int[n + 1];

        dp[1] = 1;
        dp[2] = 2;

        for(int i = 3; i < n + 1; i++)
            dp[i] = dp[i - 1] + dp[i - 2];

        return dp[n] % 1000000007;
    }
}


