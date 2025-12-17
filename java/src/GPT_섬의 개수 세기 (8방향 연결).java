import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {

        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

        FastScanner fs = new FastScanner();

        while(true){
            int w = fs.nextInt();
            int h = fs.nextInt();

            if(w == 0 && h == 0)
                break;

            int[][] graph = new int[h][w];
            boolean[][] visited = new boolean[h][w];

            for(int i = 0; i < h; i++){
                for(int j = 0; j < w; j++){
                    graph[i][j] = fs.nextInt();
                }
            }

            int island = 0;

            for(int i = 0; i < h; i++){
                for(int j = 0; j < w; j++){
                    if(!visited[i][j] && graph[i][j] == 1){
                        island++;

                        Queue<Integer[]> q = new ArrayDeque<>();
                        q.add(new Integer[]{i, j});
                        visited[i][j] = true;

                        while(!q.isEmpty()){
                            Integer[] arr = q.poll();

                            for(int idx = 0; idx < 8; idx++){
                                int nx = arr[0] + dx[idx];
                                int ny = arr[1] + dy[idx];

                                if(nx < 0 || ny < 0 || nx >= h || ny >= w)
                                    continue;

                                if(graph[nx][ny] == 0)
                                    continue;

                                if(visited[nx][ny])
                                    continue;

                                q.add(new Integer[]{nx, ny});
                                visited[nx][ny] = true;
                            }
                        }
                    }
                }
            }
            System.out.println(island);
        }
    }
}
