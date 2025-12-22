import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();
        int n = 4;
        int[][] costs = {{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}};

        System.out.println(s.solution(n, costs));
    }
}

class Solution {

    int[] parents;
    int[] size;

    public int solution(int n, int[][] costs) {
        parents = new int[n + 1];
        size = new int[n + 1];

        for(int i = 0; i < n + 1; i++)
            parents[i] = i;

        Arrays.fill(size, 1);
        Arrays.sort(costs, (x, y) ->{return Integer.compare(x[2], y[2]);});

        int answer = 0;

        for(int[] cost : costs){
            int A = cost[0];
            int B = cost[1];
            int value = cost[2];

            if(find(A) != find(B)){
                union(A, B);
                answer += value;
            }
        }

        return answer;
    }

    int find(int x){
        if(parents[x] == x) return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }

    void union(int x, int y){
        int rx = find(x);
        int ry = find(y);

        if(rx == ry)
            return;
        
        if(size[rx] < size[ry]){
            int tmp = rx;
            rx = ry;
            ry = tmp;
        }

        parents[ry] = rx;
        size[rx] += size[ry];
    }
}
