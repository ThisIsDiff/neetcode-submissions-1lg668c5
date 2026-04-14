class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if (s1.length() > s2.length()) return false;

        int[] s1counter = new int[26];
        int[] s2counter = new int[26];
        for (int i=0; i<s1.length(); i++) {
            s1counter[s1.charAt(i) - 'a']++;
            s2counter[s2.charAt(i) - 'a']++;
        }

        int match = 0;
        for (int i=0; i<26; i++) {
            if (s1counter[i] == s2counter[i]) {
                match++;
            }
        }

        int l = 0;
        for (int r=s1.length(); r<s2.length(); r++) {
            if (match == 26) return true;

            int index = s2.charAt(r) - 'a';
            s2counter[index]++;
            if (s2counter[index] == s1counter[index]) {
                match++;
            } else if (s2counter[index] - 1 == s1counter[index]) {
                match--;
            }

            index = s2.charAt(l) - 'a';
            s2counter[index]--;
            if (s2counter[index] == s1counter[index]) {
                match++;
            } else if (s2counter[index] + 1 == s1counter[index]) {
                match--;
            }
            l++;
        }
        return (match == 26);
    }
}
