class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;

        int X = wallet[0];
        int Y = wallet[1];

        int x = bill[0];
        int y = bill[1];

        while(true){
            if((X >= x && Y >= y) || (X >= y && Y >= x)){
                break;
            }

            if(x >= y)
                x = x / 2;
            else
                y = y / 2;

            answer += 1;
        }


        return answer;
    }
}