#include <bits/stdc++.h>

using namespace std;

void tenFirst(int n){
    int i = 1;
    do {
        printf("%d x %d = %d\n", n, i, n*i);
        i++;
    } while (i <= 10);
}

int main(){
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    tenFirst(n);
    return 0;
}
