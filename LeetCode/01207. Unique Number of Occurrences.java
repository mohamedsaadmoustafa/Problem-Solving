class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> occurrences = new HashMap<>();
        for (int number : arr)
            occurrences.merge(number, 1, Integer::sum);

        Set<Integer> occurrencesSet = new HashSet<>(occurrences.values());
        return occurrencesSet.size() == occurrences.size();
    }
}
