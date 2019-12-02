#include <stdio.h>
#include <stdlib.h>

void vuln(char* flag)
{
	char buf[64];
	printf("kuy >");
	fgets(buf, sizeof(buf), stdin);
	printf("Hmmmm ");
	printf(buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	char flag[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found \n");
		exit(1);
	}
	else
	{
		fgets(flag, sizeof(flag), f);
	}
	vuln(flag);

	return 0;
}
