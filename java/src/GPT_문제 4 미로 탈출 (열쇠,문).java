import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, -1, 0, 1};

    public static void main(String[] args) throws Exception {

        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int M = fs.nextInt();

        char[][] graph = new char[N][M];

        Integer[] start = {-1, -1};
        Integer[] end = {-1, -1};

        for(int i = 0; i < N; i++){
            String line = fs.next();
            for(int j = 0; j < M; j++){
                char v = line.charAt(j);
                graph[i][j] = v;

                if(v == '0') {start = new Integer[]{i, j}; continue;}
                if(v == '1') {end = new Integer[]{i, j}; continue;}
            }
        }

        boolean visited[][][] = new boolean[N][M][64];

        Queue<Integer[]> q = new ArrayDeque<>();
        q.add(new Integer[]{start[0], start[1], 0, 0}); // x, y, mask, dist
        visited[start[0]][start[1]][0] = true;

        while(!q.isEmpty()){
            Integer[] cur = q.poll();

            int x = cur[0], y = cur[1], mask = cur[2], dist = cur[3];

            if(x == end[0] && y == end[1]){
                System.out.println(dist);
                return;
            }

            for(int i = 0; i < 4; i++){
                int nx = dx[i] + x;
                int ny = dy[i] + y;

                int nextMask = mask;

                if(nx < 0 || ny < 0 || nx >= N || ny >=M)
                    continue;

                // 벽인경우
                if(graph[nx][ny] == '#')
                    continue;

                char cell = graph[nx][ny];

                // 문일 경우 열쇠 체크
                if('A' <= cell && cell <= 'F'){
                    if((nextMask &  1 << cell - 'A') == 0)
                        continue;
                }

                //열쇠일때
                if('a' <= cell && cell <= 'f'){
                    nextMask |= 1 << cell - 'a';
                }

                if(visited[nx][ny][nextMask])
                    continue;

                q.add(new Integer[]{nx, ny, nextMask, dist + 1});
                visited[nx][ny][nextMask] = true;
            }
        }
        System.out.println(-1);
    }
}