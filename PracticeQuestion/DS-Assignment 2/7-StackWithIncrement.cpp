/*
Submission Link: https://leetcode.com/submissions/detail/1280477863/
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class CustomStack {
public:
    int max_size;
    int size;
    stack<int> s;
    CustomStack(int maxSize) {
        max_size = maxSize;
        size = 0;
    }
    
    void push(int x) {
        if(size == max_size) {
            return;
        }
        s.push(x);
        size++;
    }
    
    int pop() {
        if(s.empty())
            return -1;
        int temp = s.top();
        s.pop();
        size--;
        return temp;
    }
    
    void increment(int k, int val) {
        int it = k;
        if(k >= s.size()) {
            it = s.size();
        }
        stack<int> temp;
        while(!s.empty()) {
            temp.push(s.top());
            s.pop();
        }   

        while(it -- && !temp.empty()) {
            s.push(temp.top() + val);
            temp.pop();
        }
        while(!temp.empty()) {
            s.push(temp.top());
            temp.pop();
        }

    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    CustomStack *cs = new CustomStack(3);
    cs->push(12);
    cs->push(56);
    cs->increment(2, 100);
    cs->push(87);
    cout << cs->pop() << '\n';
    cs->push(13);
    return 0;
}
