class TimeMap {

private:
    unordered_map<string, vector<pair<int, string>>> dictionary;
public:
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        dictionary[key].emplace_back(pair(timestamp, value));
    }
    
    string get(string key, int timestamp) {
        auto& ls = dictionary[key];
        int left = 0, right = ls.size() - 1;
        string res = "";
        while (left <= right) {
            int mid = left + (right - left)/2;

            if (timestamp < ls[mid].first) {
                right = mid - 1;
            } else {
                res = ls[mid].second;
                left = mid + 1;
            }
        }
        return res;
    }
};
