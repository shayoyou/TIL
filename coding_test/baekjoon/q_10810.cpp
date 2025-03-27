#include <stdio.h>

int main()
{
	int n, m;
	scanf("%d %d", &n, &m);
	int answer[100] = { 0 };

	for (int i = 0; i < m; i++)
	{
		int s, e, n;
		scanf("%d %d %d", &s, &e, &n);
		for (int j = s - 1; j < e; j++)
		{
			answer[j] = n;
		}
	}

	for (int i = 0; i < n; i++)
	{
		printf("%d ", answer[i]);
	}

	return 0;
}