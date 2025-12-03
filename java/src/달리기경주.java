import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        
        int N = players.length;
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < N; i++){
            map.put(players[i], i);
        }
        
        for(String call : callings){
            int idx = map.get(call);
            int preIdx = idx - 1;
            
            map.put(call, preIdx);
            map.put(players[preIdx], idx);
            players[idx] = players[preIdx];
            players[preIdx] = call;
        }

        return players;
    }
}