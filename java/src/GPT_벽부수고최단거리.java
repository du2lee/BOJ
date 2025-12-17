import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static int N;
    static int M;
    static int[][] graph;
    static int answer;

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        N = fs.nextInt();
        M = fs.nextInt();

        graph = new int[N][M];
        boolean[][][] visited = new boolean[N][M][2];

        for(int i = 0; i < N; i++){
            String line = fs.next();
            for(int j = 0; j < M; j++){
                graph[i][j] = line.charAt(j) - '0';
            }
        }

        Queue<Integer[]> q = new ArrayDeque<>();
        q.add(new Integer[]{0,0,1,0});  // x, y, 거리, 벽뿌여부
        visited[0][0][0] = true;

        while(!q.isEmpty()){
            Integer[] arr = q.poll();

            if(arr[0] == N - 1 && arr[1] == M - 1){
                System.out.println(arr[2]);
                return;
            }

            for(int i = 0; i < 4; i++){
                int nx = dx[i] + arr[0];
                int ny = dy[i] + arr[1];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;


                if(graph[nx][ny] == 0){
                    if(visited[nx][ny][arr[3]]) continue;
                    q.add(new Integer[]{nx, ny, arr[2] + 1, arr[3]});
                    visited[nx][ny][arr[3]] = true;
                }
                else{
                    if(visited[nx][ny][1]) continue;
                    if(arr[3] != 0) continue;
                    q.add(new Integer[]{nx, ny, arr[2] + 1, 1});
                    visited[nx][ny][1] = true;
                }
            }
        }

        System.out.println(-1);
    }
}
