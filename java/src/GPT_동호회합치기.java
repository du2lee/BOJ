import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();

        int n = 5;
        int[][] queries = {{0,1,2},{0,3,4},{1,1,3},{0,2,3},{1,4,1}};

        for(String answer : s.solution(n , queries)){
            System.out.println(answer);
        }
    }
}

class Solution {
    static int[] parents;
    static int[] size;

    public String[] solution(int n, int[][] queries) {

        parents = new int[n + 1];
        size = new int[n + 1];

        for(int i = 0; i < n + 1; i++)
            parents[i] = i;

        Arrays.fill(size, 1);

        List<String> answer = new ArrayList<>();

        for(int[] query : queries){
            int a = query[0];
            int x = query[1];
            int y = query[2];

            if(a == 0)
                union(x, y);
            else{
                if(find(x) == find(y))
                    answer.add("YES");
                else
                    answer.add("NO");
            }
        }

        
        return answer.toArray(new String[0]);

    }

    int find(int x){
        if(parents[x] == x) return x;
        parents[x] = find(parents[x]);
        return parents[x];
    }

    void union(int x, int y){

        int sx = find(x);
        int sy = find(y);

        if(sx == sy) return;

        if(size[sx] < size[sy]){    // sx가 더 큰 집합이 되게, 사이즈가 큰게 상위노드
            int tmp = sx;
            sx = sy;
            sy = tmp;
        }

        parents[sy] = sx;
        size[sx] += size[sy];
    }
}

