// Major Element Second

#include <iostream>
using namespace std;

int* majorElementSecond(int *arr, int n){
    int cand1 = -1, cand2 = -1;
    int count1 = 0, count2 = 0;

    for (int i=0; i<n; i++) {
        if (cand1 == arr[i]) {
            count1 += 1;
        } else if (cand2 == arr[i]) {
            count2 += 1;
        } else if (count1 == 0) {
            cand1 = arr[i];
            count1 = 1;
        } else if (count2 == 0) {
            cand2 = arr[i];
            count2 = 1;
        } else {
            count1 -= 1;
            count2 -= 1;
        }
    }

    count1 = 0;
    count2 = 0;

    for (int i=0; i<n; i++) {
        if (cand1 == arr[i]) {
            count1++;
        } else if (cand2 == arr[i]) {
            count2 ++;
        }
    }
    
    static int result[2];
    int temp;
    if (count1 > n/3 && count2 > n/3) {
        result[0] = cand1;
        result[1] = cand2;
    } else if (count1 > n/3) {
        result[0] = cand1;
        result[1] = 99999;
    } else if (count2 > n/3) {
        result[0] = cand2;
        result[1] = 99999;
    } else {
        result[0] = 99999;
        result[1] = 99999;
    }
    if (result[0] > result[1]) {
        temp = result[0];
        result[0] = result[1];
        result[1] = temp;
    }

    return result;
}



int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    int arr[n];
    cout << "Enter the numbers: ";
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    int* result = majorElementSecond(arr, n);
    int temp;

    for (int i=0; i<2; i++) {
        if (result[i] != 99999) {
            cout << result[i] << " ";
        }
    }
    return 0;
}
