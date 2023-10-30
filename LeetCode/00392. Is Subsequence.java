class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.isEmpty())
            return true;
        if (t.isEmpty())
            return false;
      
        int s_length = s.length(); int t_length = t.length();
        int s_start = 0; int t_start = 0;
      
        while (s_start < s_length && t_start < t_length) {
            if (s.charAt(s_start) == t.charAt(t_start)) {
                s_start++;
            }
            t_start++;
        }

        return s_start == s_length;
    }
}


