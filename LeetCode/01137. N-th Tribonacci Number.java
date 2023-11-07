class Solution {
    private HashMap<Integer, Integer> fb = new HashMap<>();

    public Solution() {
        fb.put(0, 0);
        fb.put(1, 1);
        fb.put(2, 1);
    }

    public int tribonacci(int n) {
        if (fb.containsKey(n))
            return fb.get(n);
        else {
            int result = tribonacci(n - 3) + tribonacci(n - 2) + tribonacci(n - 1);
            fb.put(n, result);
            return result;
        }
    }
}
