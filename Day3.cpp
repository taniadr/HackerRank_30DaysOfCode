#include <bits/stdc++.h>
using namespace std;

int main()
{
    int N;
    cin >> N;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    int n = N;
    if (n%2 != 0)
        printf("Weird");
    else{
        if (n > 20)
            printf("Not Weird");
        else{
            if (n > 5) 
                printf("Weird");
            else{
                if (n > 1)
                    printf("Not Weird");
            }
        }
    } 
    return 0;
}
