class Solution {
    private static Map<Character, Integer> generateCharValues() {
        Map<Character, Integer> map = new HashMap<>();
        char currentChar = 'A';
        for (int index = 1; index <= 26; index++)
            map.put(currentChar++, index);
        return map;
    }
    public int titleToNumber(String columnTitle) {
        Map<Character, Integer> charValues = generateCharValues();
        int result = 0;
        for (char ch : columnTitle.toCharArray())
            result = charValues.get(ch) + result * 26;
        return result;
    }
}


// Better Solution using ASCII
class Solution {
    public int titleToNumber(String columnTitle) {
        int result = 0;
        for (char c : columnTitle.toCharArray())
            result = c -'@' + result * 26;
        return result;
    }
}
