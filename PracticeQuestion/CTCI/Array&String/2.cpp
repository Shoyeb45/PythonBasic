#include<bits/stdc++.h>
using namespace std;
#define loop(i, n) for(int i = 0; i < n; i++)
typedef long long ll;
const ll mod = 1000000007;

bool isPermutation(string orig, string perm) {

    if(orig.size() != perm.size()) 
        return false;
        
    sort(orig.begin(), orig.end());
    sort(perm.begin(), perm.end());

    if(orig == perm)
        return true;
    return false;
    // TC: O(|orig|)
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;

    while (t--) {
        
    }
    
    return 0;
}
