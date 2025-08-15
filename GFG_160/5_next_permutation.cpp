// Next Permutation

#include <iostream>
using namespace std;

void sortTheElements(int* arr, int n, int k) {
    int temp;
    for (int i=k+1; i<n; i++) {
        for (int j=k+1; j<n; j++) {
            if (arr[i] < arr[j]) {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
}

int findPivot(int* arr, int n) {
    for (int i = n - 2; i >= 0; i--) {
        if (arr[i] < arr[i + 1]) {
            return i;
        }
    }
    return -1;
}

void findLargerThanPivot(int* arr, int n, int k) {
    int temp;
    int num = arr[n-1];
    for (int i=n-1; i>k; i--) {
        if (arr[i] > arr[k]) {
            temp = arr[i];
            arr[i] = arr[k];
            arr[k] = temp;
            sortTheElements(arr, n, k);
            return;
        }
    }
}

int nextPermutation(int* arr, int n) {
    int k = findPivot(arr, n);
    if (k == -1) {
        cout << "Cannot find next prmutation.";
        return 0;
    }
    findLargerThanPivot(arr, n, k);
}





int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter the numbers: ";
    for (int i=0; i<n; i++) {
        cin >> arr[i];
    }
    if (!nextPermutation(arr ,n)) {
        return 0;
    }
    cout << "Next permutation is: ";
    for (int i=0; i<n; i++) {
        cout << arr[i] << "  ";
    }
    return 0;
}
