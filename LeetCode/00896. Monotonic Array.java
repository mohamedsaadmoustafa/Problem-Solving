class Solution {
    public boolean isAsc(int[] nums){
        for (int i=1; i<nums.length-1; i++){
            if(nums[i-1] >= nums[i] && nums[i] >= nums[i+1]){
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
    public boolean isDesc(int[] nums){
        for (int i=1; i<nums.length-1; i++){
            if(nums[i-1] <= nums[i] && nums[i] <= nums[i+1]){
                continue;
            }
            else{
                return false;
            }

        }
        return true;
    }
    public boolean isMonotonic(int[] nums) {
        return isAsc(nums) || isDesc(nums);
    }
}



// refactor last solution
class Solution {
    public boolean isMonotonic(int[] nums) {
        boolean isAscending = true;
        boolean isDescending = true;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < nums[i - 1]) isAscending = false;
            if (nums[i] > nums[i - 1]) isDescending = false;
        }
        return isAscending || isDescending;
    }
}
