class Solution {
    public static Set<Integer> intArrayToSet(int[] array) {
        Set<Integer> set = new HashSet<>();
        for (int element : array) set.add(element);
        return set;
    }

    public static List<Integer> setDifference(Set<Integer> nums1Set, Set<Integer> nums2Set) {
        List<Integer> difference = new ArrayList<>();
        for (int num : nums1Set) {
            if (!nums2Set.contains(num)) {
                difference.add(num);
            }
        }
        return difference;
    }

    public static List findDifference(int[] nums1, int[] nums2) {
        Set<Integer> nums1Set = intArrayToSet(nums1);
        Set<Integer> nums2Set = intArrayToSet(nums2);

        return List.of(new List[]{setDifference(nums1Set, nums2Set), setDifference(nums2Set, nums1Set)});
    }
}
