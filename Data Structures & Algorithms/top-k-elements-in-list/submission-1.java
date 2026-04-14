class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> counter = new HashMap<>();
        List<Integer>[] freq = new List[nums.length + 1];

        for (int i=0; i<freq.length; i++) {
            freq[i] = new ArrayList<>();
        }

        for (int num: nums) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }

        for (Map.Entry<Integer, Integer> entry: counter.entrySet()) {
            int val = entry.getKey();
            int frequency = entry.getValue();
            freq[frequency].add(val);
        }
        
       int[] res = new int[k];
        int index = 0;
        for (int i=freq.length-1; i>=0; i--) {
            for (int val: freq[i]) {
                if (index == k) {
                    return res;
                }
                res[index]=val;
                index++;
            }
        }
        return res;
    }
}
