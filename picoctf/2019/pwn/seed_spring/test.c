#include <stdio.h>
#include <stdlib.h>

int main(){
	int seed = time(0);
	srand(seed);
	printf("%d", rand() & 0xF);
}
