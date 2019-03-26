#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <iostream>
#include <fstream>
using namespace std;
unsigned long long factorial(unsigned long long x) {
 return (x == 1 ? x : x * factorial(x - 1));
}
int get_rotetion(unsigned long long m,int n){
    m++;
    unsigned long long x=1;
    for (int i=n-1;i>1;i--){
        x=1;
        for(int j=i;j>1;j--){
          x=x*(n+2-j);
        }
        if(m%x==0){
            return i;
        }
    }
    return 1;
}

int main(int argc, char *argv[])
{
    int x;
    char c[]={'0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','g','h'};
    vector<char> lspm;
    int size;
    if(argc>1)
      size=atoi(argv[1]);
    else{
      cout << "give n" << endl;
      cin>>size;
    }
    ofstream outputFile("spm"+to_string(size)+".txt");


    for(int i=0;i<size;i++){
        lspm.push_back(c[i]);
    }

    for(int i=0; i<lspm.size(); i++)
      printf("%c",lspm[i]);
    printf("\n");
    printf("%lld,%i\n", factorial(size),size);
    for(int i=0; i<lspm.size(); i++)
      outputFile << lspm[i];
    for(unsigned long long i=0;i<factorial(size)-1;i++){
      x = get_rotetion(i,size);
      vector<char>head(lspm.begin(),lspm.begin()+x);
      reverse(head.begin(), head.end());
      for(int i=0; i<head.size(); i++)
        outputFile << head[i];
      lspm.erase(lspm.begin(), lspm.begin() + x);
      lspm.insert(lspm.end(), head.begin(), head.end());

    }
    outputFile << endl;
    return 0;
}
