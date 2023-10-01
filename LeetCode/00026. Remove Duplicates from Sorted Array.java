class Solution {
    public int removeDuplicates(int[] nums) {
        int[] distinctNums = Arrays.stream(nums).distinct().toArray();
        for (int i = 0; i < distinctNums.length; i++) {
            nums[i] = distinctNums[i];
        }
        return distinctNums.length;
    }
}
