public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = Arrays.stream(nums, 0, k).sum();
        double maxAverage = sum / k;
        for (int i = k; i < nums.length; i++) {
            sum += nums[i] - nums[i - k];
            maxAverage = Math.max(maxAverage, sum / k);
        }
        return maxAverage;
    }
}

