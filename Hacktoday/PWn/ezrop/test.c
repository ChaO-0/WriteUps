#include <stdio.h>
#include <stdlib.h>

//compile with gcc -o oob oob.c
//this binary is for learning about out of bound vuln to get a shell

int vuln(){
 char junk[10];
 char pil = 'y';
 int index;
 printf("x for quit\ni for isi\nr for read\n");
 char newline;
 while(pil != 'x'){

  scanf("%c", &pil);

  if(pil == 'i'){
   //filling
   scanf("%c", &newline);
   scanf("%d", &index);
   scanf("%c", &newline);
   scanf("%c", &junk[index]);
   printf("Index %d filled\n", index);
  }
  else if (pil == 'r'){
   scanf("%d", &index);
   printf("Your char on index %d is %d\n", index, junk[index]);
  }
 }
}

int main()
{
 vuln();
 return 0;
}
