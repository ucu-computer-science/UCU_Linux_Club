#include <stdio.h>
#include <stdlib.h>

int main()
{
	int a;
	int b;

	printf("Input a: ");
	scanf("%d", &a);

	printf("Input b: ");
	scanf("%d", &b);

	printf("\n");

	for (int i = a; i <= b; i++) {	
		if (abs(i) < 10) {
			if (i < 0) {
				printf("negative ");
			}
			if (abs(i) == 0) {
				printf("zero\n");
			} else if (abs(i) == 1) {
				printf("one\n");
			} else if (abs(i) == 2) {
				printf("two\n");
			} else if (abs(i) == 3) {
				printf("three\n");
			} else if (abs(i) == 4) {
				printf("four\n");
			} else if (abs(i) == 5) {
				printf("five\n");
			} else if (abs(i) == 6) {
				printf("six\n");
			} else if (abs(i) == 7) {
				printf("seven\n");
			} else if (abs(i) == 8) {
				printf("eight\n");
			} else {
				printf("nine\n");
			}

		} else if (i % 2 == 0) {
			printf("even\n");
		} else {
			printf("odd\n");
		}
	}
	return 0;
}

