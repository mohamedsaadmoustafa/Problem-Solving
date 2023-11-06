class Solution {
    public String defangIPaddr(String address) {
        StringBuilder sb = new StringBuilder();

        for (int index = 0; index < address.length(); index++) {
            if (address.charAt(index) == '.'){
                sb.append("[.]");
            } else {
                sb.append(address.charAt(index));
            }
        }
        return sb.toString();
    }
}
