#include <stdio.h>

int main(){
	int v1, v2, v7;
	srand(1);
	v1 = rand();
	v2 = rand() + v1;
	v7 = v2 - rand();
	printf("%d", v7);
}
