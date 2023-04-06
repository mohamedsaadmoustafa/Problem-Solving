class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();
        if (n == 0){
            return 0;
        }
        int start=0, end=0, max_length=0;
        Set<Character> char_set = new HashSet<>();
        while (end < n){
            if(char_set.contains(s.charAt(end))){
                char_set.remove(s.charAt(start));
                start++;
            } else {
                char_set.add(s.charAt(end));
                end++;
                max_length = Math.max(max_length, end-start);
            }
        }
        return max_length;
    }
}
