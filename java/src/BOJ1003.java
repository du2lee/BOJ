import java.util.*;

public class BOJ1003 {

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        List<Integer> arr0 = new ArrayList<Integer>();
        List<Integer> arr1 = new ArrayList<Integer>();
        arr0.add(1);
        arr0.add(0);
        arr1.add(0);
        arr1.add(1);

        for(int i = 2; i < 41; i++){
            arr0.add(arr0.get(i - 1) + arr0.get(i - 2));
            arr1.add(arr1.get(i - 1) + arr1.get(i - 2));
        }

        int T = sc.nextInt();

        for (int i = 0; i < T; i++){
            int num = sc.nextInt();
            System.out.println(arr0.get(num).toString() + " " + arr1.get(num).toString());
        }
    }

}
