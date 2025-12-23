import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int n = 4;
        int maxWeight = 7;
        
        int[][] items = {{6,13},{4,8},{3,6},{5,12}};

        System.out.println(s.solution(n, maxWeight, items));
    }
}

class Solution {
    public int solution(int n, int maxWeight, int[][] items) {

        int[] dp = new int[maxWeight + 1];

        for(int[] item : items){
            int weight = item[0];
            int value = item[1];

            for(int i = maxWeight; i >= weight; i--){
                dp[i] = Math.max(dp[i], dp[i - weight] + value);
            }
        }

        return dp[maxWeight];
    }
}