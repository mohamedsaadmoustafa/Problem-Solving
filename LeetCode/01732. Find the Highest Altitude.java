class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        int[] altitudes = new int[n+1]; 
        int maxAltitudes=0;

        for (int index=0; index<n; index++) {
            altitudes[index+1] = altitudes[index] + gain[index];;
            maxAltitudes = Math.max(maxAltitudes, altitudes[index+1]);
        }
        return maxAltitudes;
    }
}
