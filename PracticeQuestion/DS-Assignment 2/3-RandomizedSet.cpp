/*
Submission Link : https://leetcode.com/submissions/detail/1277473196/ 
*/

#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

class RandomizedSet {
public:
    unordered_map<int, int> ump;
    RandomizedSet() {
        
    }
    
    bool insert(int val) {
        if(ump.find(val) != ump.end()) {
            return false;
        }
        ump[val] = val;
        return true;
    }
    
    bool remove(int val) {
        if(ump.find(val) == ump.end()) {
            return false;
        }
        auto temp = ump.find(val);
        ump.erase(temp);
        return true;
    }
    
    int getRandom() {
        vector<int> a;
        for(auto i: ump) {
            a.push_back(i.second);
        }
        return a[rand() % ump.size()];
    }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    RandomizedSet *s = new RandomizedSet();
    s->insert(9);
    s->insert(18);
    s->insert(1);
    s->insert(13);
    s->insert(90214);
    cout << s->getRandom() << '\n'; 
    cout << s->getRandom() << '\n'; 
    cout << s->getRandom() << '\n'; 
    cout << s->getRandom() << '\n'; 
    return 0;
}
