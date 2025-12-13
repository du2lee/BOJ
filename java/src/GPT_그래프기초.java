import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();

        List<Integer>[] graph = new ArrayList[N + 1];

        for(int i = 0 ; i < N; i++){
            graph[i] = new ArrayList<>();
        }


    }


    static List<Integer>[] graph;
    static boolean[] visited;

    static void dfs(int x){
        visited[x] = true;

        for(int next : graph[x]){
            if(!visited[next]){
                dfs(next);
            }
        }
    }

    static void bfs(int start){
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] visited = new boolean[graph.length];

        visited[start] = true;
        q.add(start);

        while(!q.isEmpty()){
            int x = q.poll();

            for(int next : graph[x]){
                if(!visited[next]){
                    visited[next] = true;
                    q.add(next);
                }
                    
            }
        }
    }
}