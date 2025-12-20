import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        // 입력
        int N = fs.nextInt();
        int M = fs.nextInt();

        List<Integer>[] graph = new ArrayList[N + 1];

        for(int i = 0; i < N + 1; i++)
            graph[i] = new ArrayList<>();

        int[] isDegree = new int[N + 1];
        List<Integer> answer = new ArrayList<>();

        for(int i = 0; i < M; i++){
            int u = fs.nextInt();
            int v = fs.nextInt();

            graph[u].add(v);    // 그래프 간선 추가
            isDegree[v]++;      // 위상 추가
        }

        // 큐 초기화
        PriorityQueue<Integer> q = new PriorityQueue<>();

        for(int i = 1; i < N + 1; i++){
            if(isDegree[i] == 0){
                q.add(i);
            }
        }

        while(!q.isEmpty()){
            int cur = q.poll();
            answer.add(cur);

            for(int next : graph[cur]){

                isDegree[next]--;
                if(isDegree[next] == 0) {
                    q.add(next);
                }
            }
        }

        if(answer.size() != N){        // 순회하는 케이스
            System.out.println(0);
            return;
        }

        for(int a : answer)
            System.out.print(a + " ");
        System.out.println();
    }
}