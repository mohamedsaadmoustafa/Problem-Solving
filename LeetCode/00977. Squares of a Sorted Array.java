// O(nlog(n))
class Solution {
    public int[] sortedSquares(int[] nums) {
        return Arrays.stream(nums)
                    .map(n -> n * n)
                    .sorted()
                    .toArray();
    }
}

// O(n) -> two pointers solution -> for loop
class Solution {
    public int[] sortedSquares(int[] nums) {
        int length_nums = nums.length;
        int[] output = new int[length_nums];
        int start = 0; int end=length_nums-1;

        for (int index=length_nums-1; index>=0; index--){
            if(Math.abs(nums[start]) >= Math.abs(nums[end])){
                output[index] = nums[start] * nums[start];
                start++;
            } else {
                output[index] = nums[end] * nums[end];
                end--;
            }
        }
        return output;
    }
}

