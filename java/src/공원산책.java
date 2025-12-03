class Solution {

    public Boolean checkBoard(String[][] park, int mat, int X, int Y){
        Boolean flag = true;

        for(int x = 0; x < mat; x++){
            for(int y = 0; y < mat; y++){
                if(!park[x + X][y + Y].equals("-1")){
                    flag = false;
                    break;
                }
            }
            if(!flag)
                break;
        }
        return flag;
    }

    public int solution(int[] mats, String[][] park) {
        int answer = -1;

        for(int mat: mats){
            Boolean flag = false;

            for(int x = 0; x <= park.length - mat; x++){
                for(int y = 0; y <= park[x].length - mat; y++){

                    if(checkBoard(park, mat, x, y)){
                        flag = true;
                        break;
                    }
                }
                if(flag)
                    break;
            }


            if(flag){
                if(answer < mat)
                    answer = mat;
            }
        }

        return answer;
    }
}