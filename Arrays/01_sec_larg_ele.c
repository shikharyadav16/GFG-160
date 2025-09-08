// Second Largest Element

#include<stdio.h>
#include <limits.h>

int secondMaxElement(int* arr, int n);
int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    int arr[n];
    printf("Enter the elements: ");
    for (int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    int res = secondMaxElement(arr, n);
    if (res == INT_MIN) {
        printf("Second largest Element is: -1");

    } else {
        printf("Second largest Element is: %d", res);
    }
    return 0;
}

int secondMaxElement(int* arr, int n) {
    int secondLargest = INT_MIN;
    int firstLargest = arr[0];

    for (int i=1; i<n; i++) {
        if (firstLargest < arr[i]) {
            secondLargest = firstLargest;
            firstLargest = arr[i];
        } else if (firstLargest > arr[i] && arr[i] > secondLargest) {
            secondLargest = arr[i];
        }
    }
    return secondLargest;
}
