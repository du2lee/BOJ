import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer[] = new int[friends.length];

        // 이름 - 인덱스 매칭
        HashMap<String, Integer> idx = new HashMap<>();

        // 선물 주고 받는 이력
        int[][] board = new int[friends.length][friends.length];

        for(int i = 0; i < friends.length; i++) {
            idx.put(friends[i], i);
            answer[i] = 0;
            for(int j = 0; j < friends.length; j++) {
                board[i][j] = 0;
            }
        }

        // gift 조회해서 카운팅하기
        for(String gift : gifts){
            String[] names = gift.split(" ");
            int giver = idx.get(names[0]);
            int getter = idx.get(names[1]);

            board[getter][giver] += 1;
            board[giver][getter] -= 1;
        }

        // 계산
        for(int i = 0; i < friends.length; i++) {
            for(int j = i + 1; j < friends.length; j++) {
                if(board[i][j] < 0)
                    answer[i] += 1;
                else if(board[i][j] > 0)
                    answer[j] += 1;
                else{
                    // 선물 지수비교
                    int a = sum(board[i]);
                    int b = sum(board[j]);
                    if(a < b)
                        answer[i] += 1;
                    else if(a > b)
                        answer[j] += 1;

                }
            }
        }

        return max(answer);
    }

    int sum(int[] A){
        int v = 0;
        for(int a : A)
            v += a;
        return v;
    }

    int max(int[] A){
        int v = 0;
        for(int a : A){
            if(v < a)
                v = a;
        }
        return v;
    }
}