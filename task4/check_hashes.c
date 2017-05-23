#include <stdio.h>
#include <string.h>
#include "md5_op.h"

int main(int argc, char **argv)
{
  FILE *fp;
  fp = fopen("data.txt", "r");
  if (fp == NULL)
  {
    perror("Error opeining file");
    return(-1);
  }

  const size_t line_size = 80;
  const size_t key_size = 35;
  char line[line_size], *id, *name, *hash, key[key_size];
  os_md5 filesum;

  while (fgets(line, line_size, fp) != NULL)
  {
    id = strtok(line, " ");
    name = strtok(NULL, " ");
    hash = strtok(NULL, " \n");

    if (id != NULL && name != NULL && hash != NULL)
    {
      strcpy(key, id);
      strcat(key, name);

      OS_MD5_Str(key, filesum);
      
      if (strcmp(hash, filesum) == 0)
      {
        printf("%s OK\n", id);
      }
      else
      {
        printf("%s KO\n", id);
      }
    }
    else
    {
      printf("Error in line format\n");
    }
  }

  fclose(fp);

  return(0);
}
