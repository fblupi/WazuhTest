#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  FILE *fp;
  fp = fopen("data.txt", "r");
  if (fp == NULL)
  {
    perror("Error opeining file");
    return(-1);
  }

  const size_t line_size = 100;
  char line[line_size], *id, *name, *hash;

  while (fgets(line, line_size, fp) != NULL)
  {
    id = strtok(line, " ");
    name = strtok(NULL, " ");
    hash = strtok(NULL, " \n");

    if (id != NULL && name != NULL && hash != NULL)
    {

    }
    else
    {
      printf("Error in line format\n");
    }
  }

  fclose(fp);

  return(0);
}
