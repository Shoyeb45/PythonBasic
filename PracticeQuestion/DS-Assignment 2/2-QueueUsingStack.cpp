/*
Submission Link : https://leetcode.com/submissions/detail/1274491763/
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class MyQueue {
public:
    stack<int> st;
    MyQueue() {
        st;
    }
    
    void push(int x) {
        st.push(x);
    }
    
    int pop() {
        stack<int> temp;
        if(st.size() == 1) {
            int x = st.top();
            st.pop();
            return x;
        }
        int n = st.size();
        for(int i = 1; i <= n - 1; i++) {
            int x = st.top();
            st.pop();
            temp.push(x);
        }
        int top = st.top();
        st.pop();
        while(!temp.empty()) {
            int x = temp.top();
            temp.pop();
            st.push(x);
        }
        return top;
    }
    
    int peek() {
        stack<int> temp;
        if(st.size() == 1) {
            return st.top();
        }
        int n = st.size();
        for(int i = 1; i <= n - 1; i++) {
            int x = st.top();
            st.pop();
            temp.push(x);
        }
        int top = st.top();
        st.pop();
        temp.push(top);
        while(!temp.empty()) {
            int x = temp.top();
            temp.pop();
            st.push(x);
        }
        return top;
        
    }
    
    bool empty() {
        return st.empty();
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    MyQueue *q = new MyQueue();
    q->push(1);
    q->push(2);
    cout << q->peek() << '\n';
    cout << q->pop() << '\n';
    cout << q->empty() << '\n';
    return 0;
}
