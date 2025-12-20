import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static long INF = Long.MAX_VALUE / 4;   // 무한대 큰 수로 가정

    static class Edge{
        long v;
        long w;

        public Edge(long v, long w){
            this.v = v;
            this.w = w;
        }
    }

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();

        List<Edge>[] graph = new ArrayList[N + 1];
        long[] dist = new long[N + 1];

        for(int i = 0; i < N + 1; i++)
            graph[i] = new ArrayList<>();

        for(int i = 0; i < M; i++){
            int u = fs.nextInt();
            int v = fs.nextInt();
            int w = fs.nextInt();

            graph[u].add(new Edge(v, w));
        }

        Arrays.fill(dist, INF);

        // v, w(cost)
        PriorityQueue<long[]> dq = new PriorityQueue<>((x, y) -> {return Long.compare(x[1], y[1]);});
        dist[1] = 0;
        dq.add(new long[]{1, dist[1]});

        while(!dq.isEmpty()){
            long[] cur = dq.poll();
            int v = (int)cur[0];
            long cost = cur[1];

            if(dist[v] != cost) continue;       // 구버전 체크

            for(Edge next : graph[v]){
                long nv = next.v;
                long nw = next.w;

                if(dist[(int)nv] <= dist[v] + nw)
                    continue;

                dq.add(new long[]{nv, cost + nw});
                dist[(int)nv] = cost + nw;
            }
        }

        if(dist[N] == INF)
            System.out.println(-1);
        else
            System.out.println(dist[N]);
    }
}