import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();

        List<Integer>[] graph = new ArrayList[N + 1];   // 그래프
        boolean[] visited = new boolean[N + 1];

        for(int i = 0; i < N + 1; i++){
            graph[i] = new ArrayList<>();
        }

        for(int i = 0; i < M; i++){
            int u = fs.nextInt();
            int v = fs.nextInt();

            graph[u].add(v);
            graph[v].add(u);
        }


        int answer = 0;

        for(int i = 1; i < N + 1 ; i++){
            if (!visited[i]){
                
                Queue<Integer> q = new ArrayDeque<>();

                q.add(i);
                visited[i] = true;

                while(!q.isEmpty()){
                    int x = q.poll();

                    for(int next : graph[x]){
                        if(!visited[next]){
                            q.add(next);
                            visited[next] = true;
                        }
                    }
                }

                answer += 1;
            }
        }

        System.out.println(answer);
    }
}