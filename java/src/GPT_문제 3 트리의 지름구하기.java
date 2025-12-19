import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();

        List<Integer[]>[] graph = new ArrayList[N + 1];

        for(int i = 1; i <= N; i++)
            graph[i] = new ArrayList();

        for(int i = 0; i < N - 1; i++){
            int u = fs.nextInt();
            int v = fs.nextInt();
            int w = fs.nextInt();

            graph[u].add(new Integer[]{v, w});
            graph[v].add(new Integer[]{u, w});
        }

        int[] visited = new int[N + 1];

        Arrays.fill(visited, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.add(1);
        visited[1] = 0;

        while(!q.isEmpty()){
            int value = q.poll();

            for(Integer[] v : graph[value]){
                int nv = v[0];
                int nw = v[1];

                if(visited[nv] >= 0)
                    continue;

                visited[nv] = visited[value] + nw;
                q.add(nv);
            }
        }

        int edge = -1;
        int check = 0;

        for(int i = 1; i<= N; i++){
            if(check < visited[i]){
                edge = i;
                check = visited[i];
            }           
        }

        Arrays.fill(visited, -1);

        q.add(edge);
        visited[edge] = 0;

        while(!q.isEmpty()){
            int value = q.poll();

            for(Integer[] v : graph[value]){
                int nv = v[0];
                int nw = v[1];

                if(visited[nv] >= 0)
                    continue;

                visited[nv] = visited[value] + nw;
                q.add(nv);
            }
        }

        edge = -1;
        check = 0;

        for(int i = 1; i<= N; i++){
            if(check < visited[i]){
                edge = i;
                check = visited[i];
            }           
        }

        System.out.println(check); 
    }
}