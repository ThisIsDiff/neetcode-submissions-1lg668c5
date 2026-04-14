class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character, Integer> map = new HashMap<>();
        int l = 0, res = 0, maxf = 0;

        for (int i=0; i < s.length(); i++) {
            char c = s.charAt(i);
            map.put(c, map.getOrDefault(c, 0)+1);
            maxf = Math.max(maxf, map.get(c));
            while ((i-l+1)-maxf > k){
                char lchar = s.charAt(l);
                map.put(lchar, map.get(lchar)-1);
                l++;
            }
            res = Math.max(res, i-l+1);
        }
        return res;
    }
}
