#include <stdio.h>
int fact(int n){ if (n == 0) return 1; else return n * fact(n - 1); } int main(int argc, char **argv) { printf("%d\n",fact(6)); }
