#include <stdio.h>

int auxiliary;

int fib(int n)
{
    auxiliary++;
    if (n < 2)
        return n;
    return fib(n - 1) + fib(n - 2);
}

int main(int argc, char **argv)
{

    int n, size, res;

    scanf("%d", &size);

    while(size--)
    {
        auxiliary = 0;

        scanf("%d", &n);

        res = fib(n);

        printf("fib(%d) = %d calls = %d\n", n, (auxiliary - 1), res);
    }

    return 0;
}