#include <stdio.h>

long int bruh(int x, int y){
    if(y == 0 || y == x)
        return 1;
    else
        return bruh(x - 1, y - 1) + bruh(x - 1, y);
}

int main(){
    long int test;
    test = bruh(65, 10);

    printf("%ld", test);
}