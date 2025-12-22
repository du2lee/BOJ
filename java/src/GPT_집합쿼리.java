import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        Solution s = new Solution();

        int n = 5;
        int[][] queries = {{0,1,2},{0,2,3},{1,1,3}, {2,2,0}, {1,4,5}, {0,4,5},{2,4,0}};

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
            int no = query[0];
            int x = query[1];
            int y = query[2];

            if(no == 0)
                union(x, y);
            else if(no == 1){
                if(find(x) == find(y))
                    answer.add("YES");
                else
                    answer.add("NO");
            } else {
                answer.add(String.valueOf(size[find(x)]));
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
        int px = find(x);
        int py = find(y);

        if(px == py) return;

        if(size[px] < size[py]){
            int tmp = px;
            px = py;
            py = tmp;
        }

        parents[py] = px;
        size[px] += size[py];
    }
}

