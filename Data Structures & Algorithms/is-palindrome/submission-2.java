class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() -1;

        while (l < r) {
            while (l<r && !isalnum(s.charAt(l))) {
                l++;
            }
            while (l<r && !isalnum(s.charAt(r))) {
                r--;
            }

            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }
        return true;
    }

    public boolean isalnum(Character c) {
        return ('a'<=c && c<='z' ||
                'A'<=c && c<='Z' ||
                '0'<=c && c<='9');
    }
}
