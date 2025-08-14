// Rotate an array to left side

#include <iostream>
#include <numeric>
using namespace std;

void rotateArray(int *, int, int);
// int* rotateAnArray(int* arr, int n, int d) {
//     int* temp = new int[n];
//     d = d%n;

//     for (int i=0; i<n; i++) {
//         temp[i] = arr[(i+d)%n];
//     }
//     return temp;
// }

void rotateAnArrayByReversal(int *arr, int n, int d)
{
    rotateArray(arr, 0, n-1);
    rotateArray(arr, 0, n-d-1);
    rotateArray(arr, n-d, n-1);
}

void rotateArray(int *arr, int left, int right)
{
    int temp;

    while (left < right)
    {
        temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
}

int main()
{
    int n, d;
    cout << "Enter the number of elements and times to rotate: ";
    cin >> n >> d;

    int arr[n];
    cout << "Enter the elements: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }

    // int* temp = rotateAnArray(arr, n, d);
    rotateAnArrayByReversal(arr, n, d);

    cout << "Elements after rotation: ";
    // for (int i=0; i<n; i++) {
    //     cout << temp[i] << " ";
    // }
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
