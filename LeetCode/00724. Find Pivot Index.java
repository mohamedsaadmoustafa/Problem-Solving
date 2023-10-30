class Solution {
    public int pivotIndex(int[] nums) {
        int left = 0, right = Arrays.stream(nums).sum();
        
        for (int index=0; index < n = nums.length; index++) {
            right -= nums[index];
            if (left == right) return index;
            left += nums[index]; 
        }
        return -1;
    }
}
