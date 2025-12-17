import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        int[] dx = {1,0,-1,0};
        int[] dy = {0,1,0,-1};

        FastScanner fs = new FastScanner();

        int M = fs.nextInt();
        int N = fs.nextInt();

        int[][] graph = new int[N][M];
        boolean[][] visited = new boolean[N][M];

        List<Integer[]> tomatos = new ArrayList<>();

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                int tomato = fs.nextInt();
                graph[i][j] = tomato;
                if(tomato == 1)
                    tomatos.add(new Integer[]{i, j});
            }
        }

        Queue<Integer[]> q = new ArrayDeque<>();

        for(Integer[] tomato : tomatos){
            visited[tomato[0]][tomato[1]] = true;
            q.add(new Integer[]{ tomato[0], tomato[1], 0});
        }

        int answer = 0;

        while(!q.isEmpty()){
            Integer[] arr = q.poll();
            answer = Math.max(answer, arr[2]);

            for(int idx = 0; idx < 4; idx++){
                int nx = dx[idx] + arr[0];
                int ny = dy[idx] + arr[1];

                if(nx < 0 || ny < 0 || nx >= N || ny >= M)
                    continue;

                if(visited[nx][ny] || graph[nx][ny] != 0)
                    continue;

                graph[nx][ny] = 1;
                visited[nx][ny] = true;
                q.add(new Integer[]{nx, ny, arr[2] + 1});
            }
        }

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(graph[i][j] == 0){
                    System.out.println(-1);
                    return;
                }
            }
        }

        System.out.println(answer);
    }
}
