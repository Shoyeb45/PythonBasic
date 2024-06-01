/*
Submission Link : https://leetcode.com/problems/implement-stack-using-queues/submissions/1274382506
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class MyStack {
public:
    queue<int> q;
    MyStack() {
        q;
    }
    
    void push(int x) {
        q.push(x);
    }
    
    int pop() {
        if(q.size() == 1) {
            int temp = q.front();
            q.pop();
            return temp;
        }
        queue<int> temp;
        int n = q.size();
        for(int i = 1; i <= n - 1 ; i++) {
            int x = q.front();
            q.pop();
            temp.push(x);
        };
        int top = q.front();
        q.pop();
        while(!temp.empty()) {
            int x = temp.front();
            temp.pop();
            q.push(x);
        }
        return top;
    }
    
    int top() {
        if(q.size() == 1) {
            return q.front();
        }
        queue<int> temp;
        int n = q.size();
        for(int i = 1; i <= n - 1 ; i++) {
            int x = q.front();
            q.pop();
            temp.push(x);
        }
        int top = q.front();
        q.pop();
        temp.push(top);
        while(!temp.empty()) {
            int x = temp.front();
            temp.pop();
            q.push(x);
        }
        return top;
    }
    
    bool empty() {
        return q.empty();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    MyStack *st = new MyStack();
    st->push(3);
    st->push(5);
    cout << st->top() << '\n';
    cout << st->pop() << '\n';
    cout << (st->empty() ? "True\n": "False\n");
    
    return 0;
}
