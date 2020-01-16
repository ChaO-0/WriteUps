#include <stdio.h>

int main(){
	char input[48];

	scanf("%31[^,]s", input);
	printf("%s\n", input);

	return 0;
}
