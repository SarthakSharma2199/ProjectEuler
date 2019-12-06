#include<stdio.h>
int main(){
    int i, count=0;
    for(i=1; i<1000; i++){
        if(i%3==0&&i%5==0)
        count+=i;
        else if(i%3==0)
        count+=i;
        else if(i%5==0)
        count+=i;
    }
    printf("%d", count);
}