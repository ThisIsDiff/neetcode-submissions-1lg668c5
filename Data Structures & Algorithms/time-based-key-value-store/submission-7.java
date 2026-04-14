class TimeMap {
    private Map<String, List<Pair<Integer, String>>> dictionary;
    public TimeMap() {
        dictionary = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        dictionary.computeIfAbsent(key, k -> new ArrayList<>()).add(new Pair<>(timestamp, value));
    }
    
    public String get(String key, int timestamp) {
        List<Pair<Integer, String>> ls = dictionary.getOrDefault(key, new ArrayList<>());
        int left = 0, right = ls.size() - 1;
        String res = "";
        while (left <= right) {
            int mid = left + (right - left)/2;
            
            if (timestamp < ls.get(mid).getKey()) {
                right = mid - 1;
            } else {
                res = ls.get(mid).getValue();
                left = mid + 1;
            }
        }
        return res;
    }
}
