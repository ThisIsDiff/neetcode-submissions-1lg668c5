class Solution {
    public String minWindow(String s, String t) {
        if (s.length() < t.length()) return "";
        int l = 0, have = 0;
        Map<Character, Integer> tcount = new HashMap<>();
        Map<Character, Integer> window = new HashMap<>();
        for (char c: t.toCharArray()) {
            tcount.put(c,tcount.getOrDefault(c,0) + 1);
        }
        int need = tcount.size();
        int lenres = Integer.MAX_VALUE;
        int[] res = {-1,-1};
        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            window.put(c, window.getOrDefault(c, 0) + 1);
            if (tcount.containsKey(c) && tcount.get(c) == window.get(c)) {
                have++;
            }

            while (have == need) {
                if((r-l+1) < lenres) {
                    res[0] = l;
                    res[1] = r;
                    lenres = r-l+1;
                }

                char lc = s.charAt(l);
                window.put(lc, window.get(lc)-1);
                if (tcount.containsKey(lc) && window.get(lc) < tcount.get(lc)) {
                    have--;
                }
                l++;
            }
        }
        if (lenres == Integer.MAX_VALUE) {
            return "";
        }
        return s.substring(res[0], res[1]+1);
    }
}

