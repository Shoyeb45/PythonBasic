/*
Submission Link: https://leetcode.com/submissions/detail/1279304564/
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class BrowserHistory {
public:
    stack<string> s1;
    stack<string> s2;
    BrowserHistory(string homepage) {
        s1.push(homepage);
    }
    
    void visit(string url) {
        while(!s2.empty()) {
            s2.pop();
        }
        s1.push(url);
    }
    
    string back(int steps) {
        int k = steps;
        int n = s1.size();
        if(steps >= s1.size()) {
            k = s1.size() - 1;
        }
        while(!s1.empty() && k--) {
            s2.push(s1.top());
            s1.pop();
        }
        
        return s1.top();
    }
    
    string forward(int steps) {
        int k = steps;
        if(steps >= s2.size()) {
            k = s2.size();
        }
        while(k-- && !s2.empty()) {
            s1.push(s2.top());
            s2.pop();
        }
        return s1.top();
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    BrowserHistory *bh = new BrowserHistory("leetcode.com");
    bh->visit("google.com");
    bh->visit("facebook.com");
    bh->visit("linkedin.com");
    cout << bh->back(2);
    bh->visit("kaggle.com");
    
    return 0;
}
