import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();
        int K = fs.nextInt();

        int[][] graph = new int[N][M];

        for(int i = 0; i < N; i++){
            String line = fs.next();
            for(int j = 0; j < M; j++){
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        int[][][] visited = new int[N][M][K + 1];

        Queue<Integer[]> q = new ArrayDeque<>();
        q.add(new Integer[]{0, 0, 1, 0});       // x, y, 거리, 벽뿌여부
        visited[0][0][0] = 1;

        while(!q.isEmpty()){
            Integer[] arr = q.poll();

            if(arr[0] == N - 1 && arr[1] == M - 1){
                System.out.println(arr[2]);
                return;
            }

            for(int i = 0; i < 4; i++){
                int nx = arr[0] + dx[i];
                int ny = arr[1] + dy[i];

                int dist = arr[2] + 1;
                int broken = arr[3];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;

                if(graph[nx][ny] == 0){
                    if(visited[nx][ny][broken] == 1) continue;
                    q.add(new Integer[]{nx, ny, dist, broken});
                    visited[nx][ny][broken] = 1;
                } else {
                    if(broken == K) continue;
                    broken++;
                    if(visited[nx][ny][broken] == 1) {
                        broken--;
                        continue;
                    }
                    q.add(new Integer[]{nx, ny, dist, broken});
                    visited[nx][ny][broken] = 1;
                }
            }
        }
        System.out.println(-1);
    }
}
