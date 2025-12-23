import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        
        int[] arr = {10, -4, 3, 1, 5, 6, -35, 12, 21, -1};

        System.out.println(s.solution(arr));
    }
}

class Solution {
    public int solution(int[] arr) {
        int N = arr.length;

        int[][] dp = new int[N][2]; // [][0] 삭제안함, [][1] 삭제함

        dp[0][0] = arr[0];
        dp[0][1] = -10000000;

        int answer = arr[0];

        for(int i = 1; i < N; i++){
            dp[i][0] = Math.max(dp[i - 1][0] + arr[i], arr[i]); // 음수도 있기 때문에 비교함
            dp[i][1] = Math.max(dp[i - 1][1] + arr[i], dp[i - 1][0]);

            answer = Math.max(answer, Math.max(dp[i][0], dp[i][1]));
        }

        return answer;
    }
}
