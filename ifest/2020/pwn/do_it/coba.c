#include<stdio.h> 
#include<fcntl.h> 
#include<errno.h> 
extern int errno; 
int main() 
{      
    int fd[2]; 
    // char buf1[12] = "hello world"; 
    char buf2[12]; 
    char *pram;
    FILE *fp;
    
    fp = fopen("flag.txt", "r");
    if( fp == NULL ) {
        perror("Error: ");
        return(-1);
    }
    pram = read(fp, buf2, 100);
    write(1, buf2, 100); 
    fclose(fp);
    // assume foobar.txt is already created 
    // fd[0] = open("flag.txt", O_RDWR);         
    // fd[1] = open("flag.txt", O_RDWR); 
    // printf("%d\n", O_RDWR);
      
    // pram = read(fd[1], buf2, 12);
    // // write(fd[0], buf1, strlen(buf1));          
    return 0; 
} 