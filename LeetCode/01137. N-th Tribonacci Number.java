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
// NOTE: using ArrayList instead of HashMap causing a Time Limit Exceeded.

// Another solution
class Solution {
    public int tribonacci(int n) {
        if (n <= 2) return n == 0 ? 0 : 1;
        int[] arr = new int[n + 1];
        arr[0] = 0;
        if (n >= 1) arr[1] = 1;
        if (n >= 2) arr[2] = 1;
        for (int index=3; index<=n; index++)
            arr[index] = arr[index - 3] + arr[index - 2] + arr[index - 1];
        return arr[n];
    }
}

// Another solution
class Solution {
    public int tribonacci(int n) {
        if (n <= 2) return n == 0 ? 0 : 1;
        int x = 0, y = 1, z = 1, result = 0;
        for (int index = 3; index <= n; index++) {
            result = x + y + z;
            x = y; y = z; z = result;
        }
        return result;
    }
}

// Another solution: Time Limit Exceeded 
class Solution {
    public int tribonacci(int n) {
        if (n <= 2) return n == 0 ? 0 : 1;
        return tribonacci(n-3) + tribonacci(n-2) + tribonacci(n-1);
    }
}
