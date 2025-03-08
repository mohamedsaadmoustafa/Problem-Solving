import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] sortedNums = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sortedNums);
        int left = 0, right = sortedNums.length - 1;
        
        while (left < right) {
            int sum = sortedNums[left] + sortedNums[right];
            if (sum == target) {
                int index1 = findValueIndex(nums, sortedNums[left], -1);
                int index2 = findValueIndex(nums, sortedNums[right], index1);
                return new int[]{index1, index2};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{};
    }

    private int findValueIndex(int[] nums, int value, int excludeIndex) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == value && i != excludeIndex) {
                return i;
            }
        }
        return -1;
    }
}

// Another Solution
