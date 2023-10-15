class Solution {
    public int maxLengthTwoArrays(int len1, int len2) {
        return (len1 > len2) ? len1 : len2;
    }

    public String mergeAlternately(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int max = maxLengthTwoArrays(len1, len2);
        StringBuilder output = new StringBuilder();

        for(int i=0; i<max;i++){
            if(i<len1) output.append(word1.charAt(i));
            if(i<len2) output.append(word2.charAt(i));
        }
        
        return output.toString();
    }
}
