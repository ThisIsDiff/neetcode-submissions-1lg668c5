class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res(temperatures.size(),0);
        stack<pair<int, int>> st;

        for (int i=0; i<temperatures.size(); i++) {
            int temperature = temperatures[i];
            while (!st.empty() && st.top().first < temperature) {
                pair<int,int> temp = st.top(); st.pop();
                res[temp.second] = i - temp.second;
            }
            st.push({temperature, i});
        }
        return res;
    }
};
