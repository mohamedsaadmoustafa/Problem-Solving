// using hashset
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
      List<Integer> output = new ArrayList<>();
      Set<Integer> set = new HashSet<>();
      
      for (int num : nums) {
        set.add(num);
      }
      
      int n = nums.length;
      for (int i = 1; i <= n; i++) {
        if (!set.contains(i)) {
          output.add(i);
        }
      }
        return output;
    }
}


// another solution using set
class Solution {
  public List<Integer> findDisappearedNumbers(int[] nums) {
    Set<Integer> expectedNumbers = new HashSet<>(range(1, nums.length));
    for (int num : nums) expectedNumbers.remove(num);
    return new ArrayList<>(expectedNumbers);
  }

  private static List<Integer> range(int start, int end) {
    List<Integer> list = new ArrayList<>();
    for (int i = start; i <= end; i++) list.add(i);
    return list;
  }
}
