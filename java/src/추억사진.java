import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for(int i = 0; i < name.length; i ++){
            map.put(name[i], yearning[i]);
        }
        
        int[] answer = new int[photo.length];
        
        for(int i = 0; i < photo.length; i++){
            
            String[] p = photo[i];
            int score = 0;
            
            for(String people : p){
                if(map.get(people) != null)
                    score += map.get(people);
            }
            
            answer[i] = score;
            
        }
        
        
        return answer;
    }
}