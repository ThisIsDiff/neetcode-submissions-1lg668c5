class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] collection = new int[position.length][2];
        for (int i = 0; i<position.length; i++) {
            collection[i][0] = position[i];
            collection[i][1] = speed[i];
        }
        Arrays.sort(collection, (a,b) -> Integer.compare(b[0], a[0]));
        Stack<Double> stack = new Stack<>();

        for (int[] pair: collection) {
            double time = (double) (target-pair[0])/pair[1];
            if (stack.isEmpty() || (stack.peek() < time)) {
                stack.push(time);
            }
        }
        return stack.size();
    }
}
