import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for(int i = 0; i < T; i++){
            int x1= sc.nextInt();
            int y1= sc.nextInt();
            int r1= sc.nextInt();
            int x2= sc.nextInt();
            int y2= sc.nextInt();
            int r2= sc.nextInt();

            int big = 0;
            int small = 0;
            int answer = -1;

            int xx = (x1 - x2) * (x1 - x2);
            int yy = (y1 - y2) * (y1 - y2);

            double both = Math.sqrt(xx + yy);

            if(r1 > r2){
                big = r1;
                small = r2;
            }else{
                big = r2;
                small = r1;
            }

            if(x1 == x2 && y1 == y2 && r1 == r2){
                answer = -1;
            }
            else if(both > big + small || big > both + small){
                answer = 0;
            }
            else if(big == both + small || both == big + small){
                answer = 1;
            }else{
                answer = 2;
            }

            System.out.println(answer);
        }

    }
}
