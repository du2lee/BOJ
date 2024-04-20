import java.util.*;

public class BOJ1005 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();

        for(int i=0;i<T;i++){
            int N = sc.nextInt();
            int K = sc.nextInt();

            List<Integer> times = new ArrayList<Integer>();
            Map<Integer, ArrayList<Integer>> dict = new HashMap<Integer, ArrayList<Integer>>();
            ArrayList<Integer> buildTimes = new ArrayList<Integer>();
            ArrayList<Integer> check = new ArrayList<Integer>();
            Map<Integer, ArrayList<Integer>> dict2 = new HashMap<Integer, ArrayList<Integer>>();
            Map<Integer, Integer> dict3 = new HashMap<Integer, Integer>(); // 1 시작가능 0 아무런 -1 앞에 건물 필요

            times.add(0);
            buildTimes.add(0);
            check.add(0);

            for(int j = 1; j <= N; j++){
                int time = sc.nextInt();
                times.add(time);
                buildTimes.add(0);
                check.add(0);
                dict.put(j, new ArrayList<Integer>());
                dict2.put(j, new ArrayList<Integer>());
                dict3.put(j, 0);
            }

            for(int j = 0; j < K; j++){
                int s = sc.nextInt();
                int e = sc.nextInt();

                ArrayList<Integer> cache = dict.get(s);
                cache.add(e);
                dict.put(s, cache);
                check.set(e, check.get(e) + 1);
                dict3.put(e, -1);

                if(dict3.get(s) == -1){
                    continue;
                }

                dict3.put(s, 1);

            }

            int W = sc.nextInt();

            Queue<Integer> q = new LinkedList<Integer>();

            for(int k = 1; k <= N; k++){
                int cache = dict3.get(k);
                if(cache == 1){
                    q.add(k);
                    buildTimes.set(k, times.get(k));
                }
                else if(cache == 0){
                    buildTimes.set(k, times.get(k));
                }
            }

            while(!q.isEmpty()){
                int building = q.poll();

                List<Integer> nextBuildings = dict.get(building);

                for(int k = 0; k < nextBuildings.size(); k++){
                    int nextBuilding = nextBuildings.get(k);

                    if(buildTimes.get(nextBuilding) != 0){
                        continue;
                    }

                    check.set(nextBuilding, check.get(nextBuilding) - 1);

                    ArrayList<Integer> cache = dict2.get(nextBuilding);
                    cache.add(buildTimes.get(building));
                    dict2.put(nextBuilding, cache);

                    if(check.get(nextBuilding) == 0) {
                        q.add(nextBuilding);
                        buildTimes.set(nextBuilding, Collections.max(cache) + times.get(nextBuilding));
                    }
                }
            }
            System.out.println(buildTimes.get(W));
        }
    }
}
