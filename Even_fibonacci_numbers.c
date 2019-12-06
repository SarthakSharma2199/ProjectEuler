#include<stdio.h>
int main(){
    long int i, a=1, b=2, count=0;
    //printf("%d ",a);
    while(b<4000000){
        if(b%2==0)
        count+=b;
        a=b-a;
        b=b+a;
    }
    printf("%ld", count);
    
}