#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
	char text[1000];

	printf("Input your text: ");

	fgets(text, sizeof(text), stdin);
	int j = 0;
	for (int i = 0; i < strlen(text); i++) {
		if (text[i] != 32) {
			text[j] = text[i];
			j++;
		}
	}
	text[j] = 0;

	int len = strlen(text);

	printf("\nCharacters total: %d\n", len);

	
	int num_cols = ceil(sqrt(len));
	int num_rows = ceil(len/(float)(num_cols));
	
	printf("Rows: %d\n", num_rows);
	printf("Columns: %d\n\n", num_cols);

	int num_printed = 0;
	for (int i = 0; i < len; i++) {
		if (text[i] != 32) {
			printf("%c", text[i]);
			num_printed++;
			if (num_printed % num_cols == 0) {
				printf("\n");
			}
		}
	}

	return 0;
}

