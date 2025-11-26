import java.util.*;
import java.io.*;
import java.lang.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i = 0; i < T; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            // 무한대
            if(x1 == x2 && y1 == y2 && r1 == r2){
                System.out.println(-1);
                continue;
            }

            // 두 점의 길이
            Double l = Math.sqrt(Math.pow(x2-x1, 2) + Math.pow(y2-y1, 2));


            // 두 원이 안 마주치는 경우 따로 있음
            if(l > Math.abs(r2 + r1)){
                System.out.println(0);
                continue;
            }
            // 두 원이 안 마주치는 경우 안에 있음
            if(l < Math.abs(r1 - r2)){
                System.out.println(0);
                continue;
            }
            // 외접
            if(l == Math.abs(r2 + r1)){
                System.out.println(1);
                continue;
            }
            // 내접
            if(l < Math.abs(r1 - r2)){
                System.out.println(1);
                continue;
            }
            // 나머지
            System.out.println(2);

        }
    }
}