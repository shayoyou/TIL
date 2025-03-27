// 공 바꾸기
#include <stdio.h>

int main()
{
    int n, m;
    scanf("%d %d", &n, &m);
    
    int* n_arr = new int[n];
    for (int i = 0; i < n; i++)
        n_arr[i] = i + 1;

    for (int i = 0; i < m; i++)
    {
        int n1, n2;
        scanf("%d %d", &n1, &n2);
        int tmp = n_arr[n1 - 1];
        n_arr[n1 - 1] = n_arr[n2 - 1];
        n_arr[n2 - 1] = tmp;
    }

    for (int i = 0; i < n; i++)
        printf("%d ", n_arr[i]);

    delete[] n_arr;

    return 0;
}