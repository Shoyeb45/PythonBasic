/*
Submission Link : https://leetcode.com/submissions/detail/1282510962/
*/


#include<bits/stdc++.h>

using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

auto init = []() { 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();

class RandomizedCollection {
    vector<pair<int, int>> nums;
    unordered_map<int, vector<int>> ms; 
public:
    RandomizedCollection() {
        ios::sync_with_stdio(false);
        cin.tie(0);
        cout.tie(0);
    }
    
    bool insert(int val) {
        auto ans = (ms.find(val) == ms.end());
        ms[val].push_back(nums.size());
        nums.push_back({val, ms[val].size() - 1});
        return ans;
    }
    
    bool remove(int val) {
        bool ans = (ms.find(val) != ms.end());
        if(!ans)
            return false;
        
        auto last = nums.back();
        ms[last.first][last.second] = ms[val].back();
        nums[ms[val].back()] = last;
        ms[val].pop_back();

        if(ms[val].empty())
            ms.erase(val);
        
        nums.pop_back();
        return true;
    }
    
    int getRandom() {
        return nums[rand() % nums.size()].first;
    }
};

int main() {
    RandomizedCollection rd;
    rd.insert(1);
    rd.insert(1);
    rd.insert(2);
    rd.insert(3);
    rd.insert(4);
    cout << rd.insert(5) << '\n';
    rd.insert(4);
    rd.insert(2);
    rd.insert(6);
    rd.insert(7);
    cout << rd.insert(6) << '\n';
    
    cout << rd.getRandom() << '\n';
    cout << rd.remove(1) << '\n';
    cout << rd.remove(10) << '\n';
    cout << rd.remove(0) << '\n';
    cout << rd.remove(2) << '\n';
    cout << rd.remove(4) << '\n';
    cout << rd.getRandom() << '\n';
    cout << rd.getRandom() << '\n';
    cout << rd.getRandom() << '\n';
    cout << rd.getRandom() << '\n';
    return 0;
}
