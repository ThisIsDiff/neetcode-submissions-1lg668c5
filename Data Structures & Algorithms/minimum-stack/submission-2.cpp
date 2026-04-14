class MinStack {
public:
    stack<int> mstack;
    stack<int> minval;
    MinStack() {
    }
    
    void push(int val) {
        mstack.push(val);
        if (!minval.empty() && minval.top() < val) {
            val = minval.top();
        }
        minval.push(val);
    }
    
    void pop() {
        mstack.pop();
        minval.pop();
    }
    
    int top() {
        return mstack.top();
    }
    
    int getMin() {
        return minval.top();
    }
};
