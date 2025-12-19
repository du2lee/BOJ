import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int K = fs.nextInt();

        Map<Integer, ArrayList<Integer>> map = new HashMap<>();

        for(int i = 1; i <= N; i++){
            map.put(i, new ArrayList<>());
        }

        for(int i = 1; i <= K; i++){
            int a = fs.nextInt();
            int b = fs.nextInt();

            ArrayList<Integer> list = map.get(a);
            list.add(b);

            ArrayList<Integer> list2 = map.get(b);
            list2.add(a);
        }

        boolean[] visited = new boolean[N + 1];

        ArrayList<Integer> answer = new ArrayList<>();

        for(int i = 1; i <= N; i++){
            if(visited[i])
                continue;

            int cache = 1;

            Queue<Integer> q = new ArrayDeque<>();
            q.add(i);
            visited[i] = true;

            while(!q.isEmpty()){
                int v = q.poll();

                ArrayList<Integer> list = map.get(v);

                for(int n: list) {
                    if (visited[n])
                        continue;

                    q.add(n);
                    visited[n] = true;
                    cache++;
                }
            }
            answer.add(cache);
        }

        answer.sort((x, y) -> {return Integer.compare(x, y);});

        System.out.println(answer.size());

        for(int value : answer)
            System.out.print(value + " ");

    }
}