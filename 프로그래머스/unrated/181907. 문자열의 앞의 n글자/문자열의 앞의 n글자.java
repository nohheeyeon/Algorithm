class Solution {
    public String solution(String my_string, int n) {
        if (my_string.length() >= n) {
            return my_string.substring(0, n);
        } else {
            return my_string;
        }
    }
}