// 과제 안 내신 분..?
#include <stdio.h>

int main()
{
    char check[30] = { 0 };
    for (int i = 0; i < 28; i++)
    {
        int n;
        scanf("%d", &n);
        check[n - 1] = 1;
    }

    for (int i = 0; i < 30; i++)
    {
        if (check[i] == 0)
            printf("%d ", i + 1);
    }

    return 0;
}