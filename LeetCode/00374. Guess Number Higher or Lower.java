/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    private int binarySearch(int low, int high) {
        if (high < low) return -1;
        int mid = low + (high - low) / 2;
        int output = guess(mid);

        if (output == 0) return mid;
        else if (output > 0) return binarySearch(mid+1, high);
        else return binarySearch(low, mid-1);
    }
    public int guessNumber(int n) {
        return binarySearch(1, n);
    }
}
