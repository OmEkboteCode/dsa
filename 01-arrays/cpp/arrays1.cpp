#include <climits>
#include <iostream>

using namespace std;

// int main() {

//    int n;
//    cin>>n;
//   int marks[n];
//   //   cout << sizeof(marks) << endl;
//   //   cout << sizeof(marks)/sizeof(int) << endl;
// //   int n = sizeof(marks) / sizeof(int);
//   for (int i = 0; i <n; i++) {
//     cin>>marks[i];
//   }
//   for (int i = 0; i <n; i++) {
//     cout << marks[i] << " ";
//   }
//   cout << endl;

// Q1 Max Number

//   int arr[5] = {5, 3, 54, 64, 35};
//   int max = arr[0];
//   int min = arr[0];
//   int n = sizeof(arr) / sizeof(int);

//   for (int i = 0; i < n; i++) {
//     if (arr[i] > max) {
//       max = arr[i];
//     }
//     if (arr[i] < min) {
//       min = arr[i];
//     }
//   }
//   cout << "Max: " << max<<endl;
//   cout << "Min: " << min;

// void function(int arr[]){
//     arr[0] = 1000;
// }

// void printArr(int arr[], int n){
//     for(int i = 0; i<n; i++){
//         cout<< arr[i]<< ",";
//     }
//     cout<<n<< endl;
// }

// int main(){
//   int arr[] = { 1,4,5};
//   int n = sizeof(arr) / sizeof(int);
//   printArr(arr, n);
//   return 0;
// }

// Q2

// int linearSearch(int *arr, int n, int key){
//     for(int i=0; i<n; i++){
//         if(arr[i] == key){
//             return i;
//         }
//     }
//     return -1;
// }

// int main(){
//     int arr[]= {2, 4, 6, 8, 10, 12, 14, 16, 18};
//     int n = sizeof(arr)/sizeof(int);

//     cout<< linearSearch(arr, n, 10)<<endl;
//     cout<< linearSearch(arr, n, 20)<<endl;
//     return 0;
// }

// Q3

// Without Space
void reverseArray(int *arr, int n) {
  int temp = arr[0];
  for (int i = 0; i < n / 2; i++) {
    temp = arr[i];
    arr[i] = arr[n - 1 - i];
    arr[n - 1 - i] = temp;
  }
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

// with Extra Space

void printArr(int *arr, int n) {
  for (int i = 0; i < n; i++) {
    cout << *(arr + i) << ",";
  }
  cout << endl;
}

// int main() {
//   int arr[] = {2, 4, 6, 8, 10, 12, 14, 16, 18};
//   int n = sizeof(arr) / sizeof(int);
//   int copyArr[n];

//   for (int i = 0; i < n; i++) {
//     int j = n - i - 1;
//     copyArr[i] = arr[j];
//   }

//   for (int i = 0; i < n; i++) {
//     arr[i] = copyArr[i];
//   }
//   printArr(arr, n);
//   return 0;
// }

// Witout Extra Space (2 Pointer Approach)

// int main() {
//   int arr[] = {2, 4, 6, 8, 10};
//   int n = sizeof(arr) / sizeof(int);

//   int start = 0, end = n - 1;

//   while (start < end) {
//     // swap;
//     swap(arr[start], arr[end]);
//     // int temp = arr[start];
//     // arr[start] = arr[end];
//     // arr[end] = temp;
//     start++;
//     end--;
//   }

//   printArr(arr, n);
//   return 0;
// }

// Q4 Binary Search

// int binarySearch(int *arr, int n, int key) {
//   int start = 0, end = n - 1;
//   while (start <= end) {
//     int mid = (start + end) / 2;
//     if (arr[mid] == key) {
//       return mid;                // key found
//     } else if (arr[mid] < key) { // 2nd Half
//       start = mid + 1;

//     } else {
//       start = mid - 1; // 1st Half
//     }
//   }
//   return -1;
// }

// int main() {

//   int arr[] = {2, 4, 6, 8, 10};
//   int n = sizeof(arr) / sizeof(int);
//   printArr(arr, n);
// cout<<arr<<endl;
//   cout << binarySearch(arr, n, 8);

// int a = 10;
// int *aptr = &a;
// char ch = 'a';
// char *ptr = &ch;

// cout<< aptr<<endl;
// aptr = aptr+3;
// cout<< aptr-3<<endl;
void increaseValue(int *arr, int n) { arr[0] = 1000; }

// int main() {
// int n;
// cout<<"Array Size: ";
// cin>>n;
// int arr[n] = {};
// // int n = sizeof(arr);
// cout<<n<<endl;
// //Input
// for(int i= 0; i<n; i++){
//     cin>>arr[i];
// }
// for(int i = 0; i<n; i++){
//     cout<<arr[i];
// }
//   int arr[5] = {7, 4, 5, 3, 45};
//     increaseValue(arr, 5);
//     cout<<*arr<<endl;
//     cout<<arr[0]<<endl;
//     cout<<arr[1]<<endl;
//     cout<<*(arr+1)<<endl;

//   printArr(arr, 5);
//   return 0;
// }

// Linear Search

int linearSearch(int *arr, int n, int key) {
  for (int i = 0; i < n; i++) {
    if (arr[i] == key) {
      return i;
    }
  }
  return -1;
}

// Reverse with Extra space

// int main() {
//     int arr[5] = {4, 3, 54, 39, 10};
//     int n = sizeof(arr) / sizeof(int);
//     int copy[n];
//     for(int i = 0; i<n; i++){
//         int j = n-1-i;
//         copy[i] = arr[j];
//     }
//     for(int i = 0; i<n; i++){
//         arr[i] = copy[i];
//     }
//     printArr(arr, n);

// }

// Reverse without Extra space

// int main() {
//     int arr[5] = {4, 3, 54, 39, 10};
//     int n = sizeof(arr) / sizeof(int);

//     int start = 0, end = n-1;

//     while(start<end){
//         int temp = arr[start];
//         arr[start] = arr[end];
//         arr[end] = temp;

//         start++;
//         end--;
//     }
//     printArr(arr, n);

// }

// Binary Search

int binarySearch(int *arr, int n, int key) {
  int start = 0, end = n - 1;

  while (start <= end) {
    int mid = (start + end) / 2;
    if (arr[mid] == key) {
      return mid; // Key Found
    } else if (arr[mid] < key) {
      start = mid + 1; // 2nd Half
    } else {
      end = mid - 1; // 1st Half
    }
  }
  return -1;
}

// int main() {
//   int arr[6] = {2, 4, 6, 8, 10, 12};
//   int n = sizeof(arr) / sizeof(int);
// //   cout<<binarySearch(arr, n, 10);
//     cout<<arr<<endl;
//     cout<<*(arr+1)<<endl;
// }

// int main() {
//     int arr[5] = {10, 20, 30, 40, 50};
//     int n = sizeof(arr) / sizeof(int);
//     int sum = 0;
//     for(int i = 0; i<n; i++){
//         sum += arr[i];
//     }
//     cout<< sum<<endl;
//     return 0;
// }

int countOccurances(int *arr, int n, int key) {
  int count = 0;
  for (int i = 0; i < n; i++) {
    if (arr[i] == key) {
      count++;
    }
  }
  return count;
}

int secondLargest(int *arr, int n) {
  int largest = arr[0];
  int secondLargest = INT_MIN;
  for (int i = 1; i < n; i++) {
    if (largest < arr[i]) {
      secondLargest = largest;
      largest = arr[i];
    } else if (arr[i] > secondLargest && largest > arr[i]) {
      secondLargest = arr[i];
    }
  }
  if (secondLargest == INT_MIN) {
    return -1;
  }
  return secondLargest;
}

// Move All Zeros to end

void moveZeroes(int arr[], int n) {
  int position = 0;
  for (int i = 0; i < n; i++) {
    if (arr[i] != 0) {
      arr[position] = arr[i];
      position++;
    }
  }
  while (position < n) {
    arr[position] = 0;
    position++;
  }
}

int pointerSearch(int *ptr, int n, int target) {
  for (int i = 0; i < n; i++) {
    if (*(ptr + i) == target) {
      return i;
    }
  }
  return -1;
}

bool isSorted(int arr[], int n) {
  for (int i = 1; i < n; i++) {
    if (arr[i] < arr[i - 1]) {
      return false;
    }
  }
  return true;
}

void printReverse(int arr[], int n) {
  for (int i = n - 1; i >= 0; i--) {
    cout << arr[i] << " ";
  }
  cout << endl;
}
void reverseArray(int arr[], int n) {
  int start = 0;
  int end = n - 1;
  while (start < end) {
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }
}

int firstOccurrence(int arr[], int n, int target) {
  int start = 0;
  int end = n - 1;
  int answer = -1;
  while (start <= end) {
    int mid = start + (end - start) / 2;
    if (arr[mid] == target) {
      answer = mid;
      end = mid - 1;
    } else if (arr[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return answer;
}
int lastOccurrence(int arr[], int n, int target) {
  int start = 0;
  int end = n - 1;
  int answer = -1;
  while (start <= end) {
    int mid = start + (end - start) / 2;
    if (arr[mid] == target) {
      answer = mid;
      start = mid + 1;
    } else if (arr[mid] < target) {
      start = mid + 1;
    } else {
      end = mid - 1;
    }
  }
  return answer;
}
int main() {
  int arr[5] = {2, 3, 0, 4, 2};
  int n = sizeof(arr) / sizeof(int);
  moveZeroes(arr, n);
  printArr(arr, n);
}