#include <stdio.h>
#include <stdlib.h>

void hidden_function(int arg1, long long arg2)
{
	if (arg1 != 0x14B4DA55 || arg2 != 0xF00DB4BE)
	{
		puts("Ayo bang semangat.");
		exit(1);
	}

	printf("Naisu !\n");
	char buf[256];
	FILE* f = fopen("./flag.txt", "r");
	if (f == NULL)
	{
		puts("flag.txt not found - Harap lapor admin ^^\n");
	}
	else
	{
		fgets(buf, sizeof(buf), f);
		printf("flag: %s\n", buf);
	}
}

void vuln()
{
	char buf[16];
	printf("Whats ur name? >");
	gets(buf);
	printf("Welcome %s!\n", buf);
}

int main()
{
	/* Disable buffering on stdout */
	setvbuf(stdout, NULL, _IONBF, 0);

	vuln();
	return 0;
}
