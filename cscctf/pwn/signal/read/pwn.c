// gcc -fno-stack-protector -no-pie pwn.c -o pwn
#include <stdio.h>
#include <stdlib.h>

int main(){
    char buf[100];
    read(0, &buf, 500);
}
