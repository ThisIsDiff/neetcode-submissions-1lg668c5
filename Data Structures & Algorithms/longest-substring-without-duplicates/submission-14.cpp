class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> charMap;
        int res = 0, l = 0;
        for (int r=0; r<s.size(); r++) {
            if (charMap.find(s[r]) != charMap.end()) {
                l = max(l, charMap[s[r]] + 1);
            }
            charMap[s[r]] = r;
            res = max(res, r-l+1);
        }
        return res;
    }
};
