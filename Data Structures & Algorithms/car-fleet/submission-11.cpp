class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> collection;
        for (int i=0; i<position.size(); i++) {
            collection.push_back({position[i], speed[i]});
        }
        sort(collection.rbegin(), collection.rend());
        vector<double> stack;
        for (auto& pair: collection) {
            double time = ((double) (target- pair.first)/pair.second);
            if (stack.empty() || stack.back() < time) {
                stack.push_back(time);
            }
        }
        return stack.size();
    }
};
