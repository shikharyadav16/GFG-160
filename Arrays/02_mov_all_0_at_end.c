// Move all zero element at end of the array

#include<stdio.h>
void moveElement(int*, int);
int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    moveElement(arr, n);
    printf("After moving:\n");
    for (int i=0; i<n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}

void moveElement(int* arr, int n) {
    int count = 0;
    int temp;
    for (int i=0; i<n; i++) {
        if (arr[i] != 0) {
            temp = arr[count];
            arr[count++] = arr[i];
            arr[i] = temp;
        }
    }
}
