class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;

        for(int i = 0; i < schedules.length; i++){
            int M = schedules[i] % 100 + 10;
            int H = schedules[i] / 100 + M / 60;
            M %= 60;
            Boolean flag = true;

            int st = startday - 1;

            for(int j = 0; j < timelogs[i].length; j++){
                st += 1;
                st %= 7;
                if(st == 0 || st == 6)  // 주말제외
                    continue;

                int m = timelogs[i][j] % 100;
                int h = timelogs[i][j] / 100;

                if(h > H || (h == H && m > M)){
                    flag = false;
                    break;
                }
            }

            if(flag)
                answer += 1;
        }

        return answer;
    }
}