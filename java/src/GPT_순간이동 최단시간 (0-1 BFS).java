import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int MAX = 100000;

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int K = fs.nextInt();

        int[] dist = new int[MAX + 1];

        Arrays.fill(dist, MAX * 20);

        ArrayDeque<Integer> dq = new ArrayDeque<>();

        dq.add(N);
        dist[N] = 0;

        while(!dq.isEmpty()){
            int v = dq.poll();
            int[] nexts = {2 * v, v + 1, v - 1};
            
            for(int next: nexts){
                if(next > MAX || next < 0) continue;

                if(next == 2 * v && dist[next] > dist[v]){
                    dist[next] = dist[v];
                    dq.addFirst(next);
                } else if(dist[next] > dist[v] + 1) {
                    dist[next] = dist[v] + 1;
                    dq.addLast(next);
                }
            }
        }

        System.out.println(dist[K]);
    }
}