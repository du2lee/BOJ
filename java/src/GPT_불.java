import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int R = fs.nextInt();
        int C = fs.nextInt();

        char[][] graph = new char[R][C];
        int[][] fireTime = new int[R][C];
        boolean[][] visited = new boolean[R][C];

        Queue<Integer[]> fire = new ArrayDeque<>();
        Queue<Integer[]> person = new ArrayDeque<>();

        for(int i = 0; i < R; i++) {
            Arrays.fill(fireTime[i], -1);
        }

        for(int i = 0; i < R; i++){
            String line = fs.next();
            for(int j = 0; j < C; j++){
                char value = line.charAt(j);
                if(value =='F'){
                    fire.add(new Integer[]{i, j, 0});
                    fireTime[i][j] = 0;
                } else if(value == 'J'){
                    person.add(new Integer[]{i, j, 0});
                    visited[i][j] = true;
                }
                graph[i][j] = value;
            }
        }

        // firetime 을 다 구한다
        while(!fire.isEmpty()){
            Integer[] f = fire.poll();

            for(int i = 0; i < 4; i++){
                int nx = dx[i] + f[0];
                int ny = dy[i] + f[1];

                if(nx < 0|| ny < 0 || nx >= R || ny >= C)
                    continue;

                if(fireTime[nx][ny] != -1)  // 불이 지나간 자리
                    continue;

                if(graph[nx][ny] == '#')    // 벽
                    continue;

                fireTime[nx][ny] = f[2] + 1;
                fire.add(new Integer[]{nx, ny, f[2] + 1});
            }
        }

        // 사람이 움직인다
        while(!person.isEmpty()){
            Integer[] p = person.poll();

            for(int i = 0; i < 4; i++){
                int nx = dx[i] + p[0];
                int ny = dy[i] + p[1];
                int time = p[2] + 1;

                if(nx < 0 || ny < 0 || nx >= R || ny >= C){
                    // 탈출 완료
                    System.out.println(time);
                    return;
                }

                if(graph[nx][ny] != '.')        // 벽
                    continue;

                if(fireTime[nx][ny] <= time && fireTime[nx][ny] != -1)
                    continue;

                if(visited[nx][ny])
                    continue;

                visited[nx][ny] = true;
                person.add(new Integer[]{nx, ny, time});
            }
        }
        System.out.println("IMPOSSIBLE");
    }

}
