class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;

        int s1counter[26] = {};
        int s2counter[26] = {};
        for (int i = 0; i < s1.size(); i++) {
            s1counter[s1[i]-'a']++;
            s2counter[s2[i]-'a']++;
        }

        int match = 0;
        for (int i = 0; i < 26; i++) {
            if (s1counter[i] == s2counter[i]) {
                match++;
            }
        }

        int l = 0;
        for (int r = s1.size(); r < s2.size(); r++) {
            if (match == 26) return true;

            int index = s2[r] - 'a';
            s2counter[index]++;
            if (s2counter[index] == s1counter[index]) {
                match++;
            } else if (s2counter[index] -1 == s1counter[index]) {
                match--;
            }

            index = s2[l] - 'a';
            s2counter[index]--;
            if (s2counter[index] == s1counter[index]) {
                match++;
            } else if (s2counter[index] +1 == s1counter[index]) {
                match--;
            }

            l++;
        }
        return (match==26);
    }
};
