class Solution {
    private Boolean isVowel(char ch){
        return "aeiouAEIOU".contains(String.valueOf(ch));
    }
    public String reverseVowels(String s) {
        StringBuilder output = new StringBuilder(s);
        int start = 0;
        int last = s.length() - 1;

        while(start < last){
            if (this.isVowel(s.charAt(start)) && this.isVowel(s.charAt(last))) {
                output.setCharAt(start, s.charAt(last));
                output.setCharAt(last, s.charAt(start));
                start++;
                last--;
            } else if (!this.isVowel(s.charAt(start))) {
                start++;
            } else {
                last--;
            }
        }
        return output.toString();
    }
}
