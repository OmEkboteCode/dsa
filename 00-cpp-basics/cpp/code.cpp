#include <iostream>
#include <iomanip>
#include <cmath>
using namespace std;

int main(){
    int n = 5;
    
    for(int i=1; i<=n; i++){
        for(int j=1; j<=n-i; j++){
            cout<<" ";
        }
        int val=i;
        while(val>=2) {
            cout<<val;
            val--;
        }
        while(val<=i){
            cout<<val;
            val++;
        }
        cout<<endl;
    }
    

    return 0;
}