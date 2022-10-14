#include <stdio.h>
void main()
{
    int a = 10;
    int *p = &a;
    a = 30;
    printf("%d%d\n", a, *p);
}