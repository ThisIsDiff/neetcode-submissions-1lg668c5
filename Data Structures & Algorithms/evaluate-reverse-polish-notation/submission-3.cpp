class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (string t: tokens) {
            int temp;
            if (t == "+") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                temp = a + b;
            } else if (t == "-") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                temp = a - b;
            } else if (t == "*") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                temp = a * b;
            } else if (t == "/") {
                int b = st.top(); st.pop();
                int a = st.top(); st.pop();
                temp = a / b;
            } else {
                temp = stoi(t);
            }
            st.push(temp);
        }
        return st.top();
    }
};
