class Solution {

    int[] dx = {0,1,0,-1};
    int[] dy = {1,0,-1,0};

    public int solution(String[][] board, int h, int w) {
        int answer = 0;

        for(int i = 0; i < 4; i++){
            int nx = dx[i] + h;
            int ny = dy[i] + w;

            if(nx < 0 || nx >= board.length || ny < 0 || ny >= board[0].length)
                continue;

            if(board[h][w].equals(board[nx][ny]))
                answer += 1;
        }
        return answer;
    }
}