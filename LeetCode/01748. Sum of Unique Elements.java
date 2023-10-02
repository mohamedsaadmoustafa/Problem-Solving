class Solution {
  public int sumOfUnique(int[] nums) {
    Map<Integer, Integer> counts = new HashMap<>();
    for (int num : nums) {
        counts.put(num, counts.getOrDefault(num, 0) + 1);
    }

    return counts.keySet().stream()
            .filter(key -> counts.get(key) == 1)
            .mapToInt(Integer::intValue)
            .sum();
    }
}

// another solution
class Solution {
    public int sumOfUnique(int[] nums) {
        Set<Integer> numsSet = new HashSet<Integer>();
        List<Integer> duplicates = new ArrayList<Integer>();
        int sum = 0;
        for (int num : nums) {
            if (!numsSet.add(num)) {
                duplicates.add(num);
            } 
        }

        for (int num : numsSet) {
            if (!duplicates.contains(num)) {
                sum += num;
            } 
        }
        return sum;
    }
}
