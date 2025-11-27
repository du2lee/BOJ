class Solution {
    public int solution(int n, int w, int num) {
        int answer = 0;

        int N = n - 1;
        int num2 = num - 1;

        int H = num2 / w;   // 높이
        int W;              // 가로
        int mod = num2 % w;

        if(H % 2 == 1){   // 홀수
            W = w - 1 - mod;
        } else {    // 짝수
            W = mod;
        }

        while(true){
            int cache = 0;

            if(H % 2 == 1){
                cache = H * w + (w - 1 - W);
            }else{
                cache = H * w + W;
            }
            if(cache > N)
                break;
            H += 1;
            answer += 1;
        }

        return answer;
    }
}