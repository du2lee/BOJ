import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int MAX = 100000;

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int K = fs.nextInt();

        int[] prev = new int[MAX + 1];
        boolean[] visited = new boolean[MAX + 1];


        Arrays.fill(prev, -1);

        Queue<Integer> q = new ArrayDeque<>();
        q.add(N);
        visited[N] = true;

        while(!q.isEmpty()){

            int v = q.poll();
            int[] nexts = {v * 2, v + 1, v - 1};

            if(v == K){
                break;
            }

            for(int next: nexts){
                if(next > MAX || next < 0) continue;
                if(visited[next]) continue;

                q.add(next);
                prev[next] = v;
                visited[next] = true;
            }
        }

        ArrayDeque<Integer> answer = new ArrayDeque<>();

        while(K != -1){
            answer.addFirst(K);
            K = prev[K];
        }

        System.out.println(answer.size() - 1);

        for(Integer a : answer)
            System.out.print(a + " ");
        
    }
}