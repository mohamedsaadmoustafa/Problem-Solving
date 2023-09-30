class Solution {
    public int diagonalSum(int[][] mat) {
        int output = 0;
        int first = 0;
        int last = mat[0].length-1;

        for (int index=0; index < mat.length; index++){
            output += mat[index][last-index];
            if (first+index != last-index){
                output += mat[index][first+index];
            }
        }
        return output;
    }
}
