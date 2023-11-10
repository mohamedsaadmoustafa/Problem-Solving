public class Solution {
    public static int hammingWeight(int n) {
        int output = 0;
        String binaryString = Integer.toBinaryString(n);

        for (int index = 0; index < binaryString.length(); index++) {
            if (binaryString.charAt(index) == '1') {
                output++;
            }
        }
        return output;
    }

    public static void main(String[] args) {
        int unsignedValue = -3; // Replace this with the desired unsigned input value
        int weight = hammingWeight(unsignedValue);
        System.out.println("Hamming weight of " + unsignedValue + " is: " + weight);
    }
}
