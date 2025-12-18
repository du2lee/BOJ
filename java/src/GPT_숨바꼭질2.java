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
        int[] cnt = new int[MAX + 1];

        Arrays.fill(dist, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.add(N);
        dist[N] = 0;
        cnt[N] = 1;

        while(!q.isEmpty()){

            int v = q.poll();
            int[] d = {v * 2, v + 1, v - 1};

            for(int i = 0; i < 3; i++){

                int nv = d[i];
                int nDist = dist[v] + 1;

                if(nv > MAX || nv < 0)  // 범위초과
                    continue;

                if(dist[nv] == -1){
                    q.add(nv);
                    dist[nv] = nDist;
                    cnt[nv] = cnt[v];
                } else if (dist[nv] == nDist)
                    cnt[nv] += cnt[v];
            }
        }

        System.out.println(dist[K]);
        System.out.println(cnt[K]);
    }
}