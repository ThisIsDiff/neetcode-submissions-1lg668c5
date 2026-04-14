class Solution {
public:
    int characterReplacement(string s, int k) {
        unordered_map<char, int> map;
        int l = 0, res = 0, maxf = 0;
        for (int i = 0; i < s.size(); i++) {
            map[s[i]]++;
            maxf = max(maxf, map[s[i]]);
            while ((i-l+1)-maxf > k) {
                map[s[l]]--;
                l++;
            }
            res = max(res, i-l+1);
        }

        return res;
    }
};
