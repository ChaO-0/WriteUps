#include <stdio.h>

#define MAXN 128
void service() {
  FILE *fp;
  char path[MAXN];
  char lang[MAXN];
  char menu[MAXN];
  int choice;

  printf("Choose language (id/en/it): ");
  fgets(lang, sizeof(lang), stdin);
  strtok(lang, "\n");

  snprintf(path, MAXN, "languages/%s.lang", lang);
  printf("%s", path);

}

int main(){
    service();
}
