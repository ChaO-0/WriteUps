#include <stdio.h>
#include <stdlib.h>

int main(){
    int v8;

    srand(1);
    for(int i = 0; i <= 99; ++i){
        v8 = rand() % 100000 + 1;
        printf("%d\n", v8);
    }
    return 0;
}