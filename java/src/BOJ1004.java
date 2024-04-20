import java.util.*;

public class BOJ1004 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for(int i = 0; i< T;i++){

            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            int answer = 0;
            int n = sc.nextInt();

            for (int j = 0; j < n; j++){
                int cx = sc.nextInt();
                int cy = sc.nextInt();
                int r = sc.nextInt();

                double sr = Math.sqrt((x1 - cx) * (x1 - cx) + (y1 - cy) * (y1 - cy));
                double er = Math.sqrt((x2 - cx) * (x2 - cx) + (y2 - cy) * (y2 - cy));

                if( (r >= sr && r >= er) || (r <= sr && r <= er)){
                    continue;
                }
                answer += 1;
            }

            System.out.println(answer);
        }
    }
}
