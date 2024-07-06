class Solution {
    public int passThePillow(int n, int time) {
        int cycleLength = 2 * (n - 1);
        time = time % cycleLength;
        int current = 1;
        boolean forward = true;

        for (int i = 0; i < time; i++) {
            if (forward) {
                current++;
                if (current == n) forward = false;
            } else {
                current--;
                if (current == 1) forward = true;
            }
        }
        return current;
    }
}
