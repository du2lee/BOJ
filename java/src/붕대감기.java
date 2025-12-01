class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health;
        int time = 0;


        // attack으로 순회한다.
        for(int[] attack : attacks){
            int attackTime = attack[0];
            int damage = attack[1];

            // 공격 전 까지 회복 하기
            int healTime = attackTime - time;
            healTime -= 1;
            answer += (healTime * bandage[1]);
            answer += (healTime / bandage[0]) * bandage[2];
            time = attackTime;

            // 최대체력 초과 시 최대로 설정
            if(answer > health)
                answer = health;

            // 공격 시간 피해량 계산하기
            answer -= damage;


            // 만약에 answer이 0 이하면 사망으로 표시
            if(answer <= 0){
                answer = -1;
                break;
            }
        }


        return answer;
    }
}