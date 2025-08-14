// Reverse an array

#include<stdio.h>
void reverseArray(int*, int);
int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    reverseArray(arr, n);
    printf("Elements after reversing: ");
    for (int i=0; i<n; i++) {
        printf("%d   ", arr[i]);
    }
    return 0;
}
void reverseArray(int* arr, int n) {
    int left = 0, right = n-1;
    int temp;
    while (left < right) {
        temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}
