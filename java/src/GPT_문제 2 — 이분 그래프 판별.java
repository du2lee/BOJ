import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();

        List<Integer>[] graph = new ArrayList[N + 1];
        String[] color = new String[N + 1];

        for(int i = 1; i <= N; i++)
            graph[i] = new ArrayList<>();
        Arrays.fill(color, "N");

        for(int i = 0; i < M; i++){
            int u = fs.nextInt();
            int v = fs.nextInt();

            graph[u].add(v);
            graph[v].add(u);
        }

        String answer = "YES";

        boolean bigFlag = false;

        for(int i = 1; i <= N ; i++){
            if(!color[i].equals("N"))
                continue;

            Queue<Integer> q = new ArrayDeque<>();
            q.add(i);
            color[i] = "R";

            while(!q.isEmpty() && !bigFlag){
                int value = q.poll();
                String flag = "R";
                if(color[value].equals("R")) flag = "B";

                for(int nv : graph[value]){
                    if(!color[nv].equals("N")){
                        if(color[nv].equals(flag))
                            continue;
                        else{
                            bigFlag = true;
                            answer = "NO";
                            break;
                        }
                    }
                    q.add(nv);
                    color[nv] = flag;
                }
            }
            if(bigFlag)
                break;
        }
        System.out.println(answer);
    }
}