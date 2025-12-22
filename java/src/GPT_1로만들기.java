import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();

        int n = 10;

        System.out.println(s.solution(n));
    }
}

class Solution {
    public int solution(int n) {

        int[] dp = new int[n + 1];

        Queue<Integer> q = new ArrayDeque<>();

        q.add(1);

        while(!q.isEmpty()){
            int cur = q.poll();

            int[] nexts = {cur + 1, cur * 2, cur * 3};

            for(int next : nexts){
                if(next > n)
                    break;

                if(dp[next] != 0)
                    continue;

                dp[next] = dp[cur] + 1;
                q.add(next);
            }
        }
        return dp[n];
    }
}


