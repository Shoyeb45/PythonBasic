/*
Submission Link: https://leetcode.com/submissions/detail/1280495545/
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class StockSpanner {
public:
    vector<int> a;
    StockSpanner() {
        
    }
    
    int next(int price) {
        a.push_back(price);
        int ans = 0;
        for(int i = a.size() - 1; i >= 0; i--) {
            if(price >= a[i]) 
                ans++;
            else
                break;
        }
        return ans;
    }
};



int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    StockSpanner *s = new StockSpanner();
    cout << s->next(100) << '\n';
    cout << s->next(42) << '\n';
    cout << s->next(230) << '\n';
    cout << s->next(12) << '\n';
    cout << s->next(109) << '\n';
    cout << s->next(79) << '\n';
    return 0;
}
