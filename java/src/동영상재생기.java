class Solution {

    // 시간을 초로 변환하기
    public int convertSeconds(String time){
        String[] a = time.split(":");
        return Integer.parseInt(a[0]) * 60 + Integer.parseInt(a[1]);
    }

    // retrun 타입으로 변환
    public String convertReturn(int time){
        int mm = time / 60;
        int ss = time % 60;

        return String.format("%02d:%02d", mm, ss);
    }


    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {

        int now = convertSeconds(pos);
        int len = convertSeconds(video_len);
        int opS = convertSeconds(op_start);
        int opE = convertSeconds(op_end);

        // 오프닝 스킵 확인
        if(opS <= now && now < opE){
            now = opE;
        }

        for(String command : commands){
            if(command.equals("prev"))
                now -= 10;
            else if(command.equals("next"))
                now += 10;

            if(now < 0){
                now = 0;
            }

            if(now > len){
                now = len;
            }

            // 오프닝 스킵 확인
            if(opS <= now && now < opE){
                now = opE;
            }
        }

        return convertReturn(now);
    }
}