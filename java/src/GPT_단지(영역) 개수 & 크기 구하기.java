import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        FastScanner fs = new FastScanner();

        int N = fs.nextInt();
        int[][] graph = new int[N][N];
        boolean[][] visited = new boolean[N][N];

        for(int i = 0; i < N; i++){
            String row = fs.next();
            for(int j = 0; j < N; j++){
                graph[i][j] = row.charAt(j) - '0';
            }
        }

        int count = 0;
        List<Integer> list = new ArrayList<>();

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};

        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(!visited[i][j] && graph[i][j] == 1){
                    count++;
                    int value = 0;

                    // bfs
                    Queue<Integer[]> q = new ArrayDeque<>();
                    q.add(new Integer[]{i, j});
                    visited[i][j] = true;

                    while(!q.isEmpty()){
                        Integer[] arr = q.poll();
                        value++;
                        
                        for(int idx = 0; idx < 4; idx++){
                            int nx = dx[idx] + arr[0];
                            int ny = dy[idx] + arr[1];
                            
                            if(nx < 0 || ny < 0 || nx >= N || ny >= N)
                                continue;

                            if(graph[nx][ny] == 0)
                                continue;

                            if(visited[nx][ny])
                                continue;

                            q.add(new Integer[]{nx, ny});
                            visited[nx][ny] = true;
                        }
                    }
                    list.add(value);


                    
                }
            }
        }

        list.sort((x,y) -> {return Integer.compare(x, y);});

        System.out.println(count);
        for(int value : list)
            System.out.println(value);
    }
}
