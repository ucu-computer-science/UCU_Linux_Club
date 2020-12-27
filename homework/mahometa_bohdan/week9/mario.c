#include <stdio.h>

int main()
{
	int height;

	printf("Height: ");
	scanf("%d", &height);

	for (int i = 1; i <= height; i++) {
		for (int j = 1; j <= height; j++) {
			if (i + j > height) {
				printf("#");
			} else {
				printf(" ");
			}
		}
		printf("\n");
	}
	return 0;
}

