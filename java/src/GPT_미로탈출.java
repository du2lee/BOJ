import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();
        int[][] graph = new int[N][M];

        for(int i = 0; i < N; i++){
            String line = fs.next();
            for(int j = 0; j < M; j++)
                graph[i][j] = line.charAt(j) - '0';
        }

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        int answer = -1;

        // bfs
        Queue<Integer[]> q = new ArrayDeque<>();

        if(graph[0][0] == 1)
            q.add(new Integer[]{0, 0, 1});

        while(!q.isEmpty()){
            Integer[] arr = q.poll();

            for(int i = 0; i < 4 ; i++){
                int nx = dx[i] + arr[0];
                int ny = dy[i] + arr[1];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;

                if(graph[nx][ny] != 1)
                    continue;

                q.add(new Integer[]{nx, ny, arr[2] + 1});
                graph[nx][ny] = arr[2] + 1;

                if(nx == N - 1 && ny == M - 1)
                    answer = arr[2] + 1;

            }
        }

        if(N == 1 && M == 1 && graph[0][0] == 1)
            System.out.println(1);
        else
            System.out.println(answer);
    }
}
