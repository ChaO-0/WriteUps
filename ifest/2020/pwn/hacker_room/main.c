// gcc -no-pie -z relro -z now -o main main.c && strip main
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <signal.h>

int readline(char* buf, int len) {
	int n;
	n = read(0, buf, len);
	if (n < 0) {
		printf("Read Error\n");
		exit(1);
	}
	if(buf[n-1] == '\n') {
		buf[n-1] = '\0';
	}
	return n;
}

int read_int() {
	char buf[16];
	int n;
	readline(buf, 16);
	n = atoi(buf);
	return n;
}

void timeout(int n) {
	printf("Timeout!\n");
	exit(1);
}

void init_prog(void) {
	setvbuf(stdin,(char *)0x0,2,0);
	setvbuf(stdout,(char *)0x0,2,0);
	setvbuf(stderr,(char *)0x0,2,0);
	alarm(60);
	signal(SIGALRM, timeout);
}

char buf[512];

struct st1 {
	unsigned short password1;
	unsigned int password2;
	char *message;
	unsigned long password3;
	void (*funcptr)(unsigned int, unsigned short, unsigned int, unsigned long, char*);
	char *yourname;
};

struct st1* my_profile;

void truehackerroom(unsigned int not_used, unsigned short p1, unsigned int p2, unsigned long p3, char* sec) {
	char cmd[80];
	memset(cmd, '\0', 80);
	if(p1 == 37) {
		strcat(cmd, "/b");
		if(p2 == 1337) {
			strcat(cmd, "in");
			if(p3 == 0x3373371) {
				strcat(cmd, "/sh");
				if(strcmp(sec, "HACKME") == 0) {
					system(cmd);
				}
			}
		}
	}
	printf("Are you trying to hackme? failed huh? :(\n");
}

void yourprofile(unsigned int not_used, unsigned short p1, unsigned int p2, unsigned long p3, char* sec) {
	printf("Hello hackers! this is mine\n");
	printf("Secret 1: %hd\n", p1);
	printf("Secret 2: %d\n", p2);
	printf("Secret 3: %ld\n", p3);
	printf("Message : %s\n", sec);
	return;
}

void display_profile() {
	my_profile->funcptr(1337, my_profile->password1,
			my_profile->password2,
			my_profile->password3,
			my_profile->message);
}

void edit_name() {
	printf("Enter your new name: ");
	readline(buf, 512);
	sprintf(my_profile->yourname, "%s", buf);
	printf("Edit done\n");
}

int main(void) {
	init_prog();
	char* name;
	int p1, p2;
	unsigned long p3;
	printf("Welcome to hacker room\n");
	printf("What's your name? ");
	readline(buf, 512);
	name = strdup(buf);
	my_profile = malloc(sizeof(struct st1));
	printf("For security reason, please provide your three secret code\n");
	printf("Secret 1: ");
	scanf("%hd", &(my_profile->password1));
	printf("Secret 2: ");
	scanf("%d", &(my_profile->password2));
	printf("Secret 3: ");
	scanf("%ld", &(my_profile->password3));
	printf("Enter your message: ");
	readline(buf, 512);
	my_profile->message = strdup(buf);
	my_profile->yourname = name;
	my_profile->funcptr = yourprofile;
	while(1) {
		printf("*** HACKER ROOM ***\n");
		printf("[1] Tell your secret and message to other hackers\n");
		printf("[2] Change yourname (in case if you're wanted by the police)\n");
		printf("[3] Get out of the room (you feel noob?)\n");
		printf("Your choice: ");
		int ch = read_int();
		switch(ch) {
			case 1:
				display_profile();
				break;
			case 2:
				edit_name();
				break;
			case 3:
				printf("Bye\n");
				exit(1);
			default:
				printf("What do you want?\n");
		}
	}
}
