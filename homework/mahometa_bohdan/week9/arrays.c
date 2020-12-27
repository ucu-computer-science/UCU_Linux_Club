#include <stdio.h>
#include <string.h>

#define max(a,b) (a>b?a:b)

int main() {

	printf("Input the length of the first array: ");
	int len1;
	scanf("%d", &len1);
	printf("Input the numbers: ");
	int num_nums1;
	scanf("%d", &num_nums1);
	int array1[1000] = {0};
	for (int i = 0; i < num_nums1; i++) {
		scanf("%d", array1 + i);
	}


	printf("\nInput the length of the second array: ");
	int len2;
	scanf("%d", &len2);
	printf("Input the numbers: ");
	int num_nums2;
	scanf("%d", &num_nums2);
	int array2[100] = {0};
	for (int i = 0; i < num_nums2; i++) {
		scanf("%d", array2 + i);
	}

	int i = 0;
	int newArray[1000];
	for (; i < len2 && i < len1; i++) {
		newArray[i] = array1[i] + array2[i];
	}
	for (; i < num_nums1; i++) {
		newArray[i] = array1[i];
	}
	for (; i < num_nums2; i++) {
		newArray[i] = array2[i];
	}

	printf("\nThe output array:\n");
	for (i = 0; i < max(num_nums1, num_nums2); i++) {
		char str[11];
		sprintf(str, "%d", newArray[i]);
		for (int j = 0; j < strlen(str); j++) {
			printf("%c ", str[j]);
		}
	}
	printf("\n");

	return 0;
}
