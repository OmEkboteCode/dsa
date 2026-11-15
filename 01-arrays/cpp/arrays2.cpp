#include <climits>
#include <iostream>

using namespace std;

void printSubarrays(int *arr, int n) {
  for (int start = 0; start < n; start++) {
    for (int end = start; end < n; end++) {
      // cout<<"("<< start<<","<<end<<") ";
      for (int i = start; i <= end; i++) {
        cout << arr[i];
      }
      cout << ", ";
    }
    cout << endl;
  }
}

void maxSubarraySum1(int *arr, int n) {
  int maxSum = INT_MIN;
  for (int start = 0; start < n; start++) {
    for (int end = start; end < n; end++) {
      int currSum = 0;
      for (int i = start; i <= end; i++) {
        currSum += arr[i];
      }
      cout << currSum << ", ";
      maxSum = max(maxSum, currSum);
    }
    cout << endl;
  }
  cout << "Max Subarray Sum = " << maxSum << endl;
}

void maxSubarraySum2(int *arr, int n) {
  int maxSum = INT_MIN;
  for (int start = 0; start < n; start++) {
    int currSum = 0;
    for (int end = start; end < n; end++) {
      currSum += arr[end];
      maxSum = max(maxSum, currSum);
    }
  }
  cout << "Max Subarray Sum = " << maxSum << endl;
}

void maxSubarraySum3(int *arr, int n) {
  int maxSum = INT_MIN;
  int currSum = 0;
  for (int i = 0; i < n; i++) {
    currSum += arr[i];
    maxSum = max(currSum, maxSum);
    if (currSum < 0) {
      currSum = 0;
    }
  }
  cout << maxSum << endl;
}

void maxProfit(int *arr, int n) {
  int bestBuy[100000];
  bestBuy[0] = INT_MAX;
  for (int i = 1; i < n; i++) {
    bestBuy[i] = min(bestBuy[i - 1], arr[i - 1]);
  }

  int maxProfit = 0;
  for (int i = 0; i < n; i++) {
    int currProfit = arr[i] - bestBuy[i];
    maxProfit = max(maxProfit, currProfit);
  }
  cout << "Max Profit = " << maxProfit << endl;
}

int trap(int *heights, int n) {
  int leftMax[20000], rightMax[20000];
  leftMax[0] = heights[0];
  rightMax[n - 1] = heights[n - 1];
  for (int i = 1; i < n; i++) {
    leftMax[i] = max(leftMax[i - 1], heights[i - 1]);
  }
  for (int i = n - 2; i >= 0; i--) {
    rightMax[i] = max(rightMax[i + 1], heights[i + 1]);
  }

  int waterTrapped = 0;
  for (int i = 0; i < n; i++) {
    int currWater = min(leftMax[i], rightMax[i]) - heights[i];
    if (currWater > 0) {
      waterTrapped += currWater;
    }
  }

  return waterTrapped;
}

bool containsDuplicate(int *arr, int n) {
  for (int start = 0; start < n; start++) {
    int key = arr[start];
    for (int end = start + 1; end < n; end++) {
      if (arr[end] == key) {
        return true;
      }
    }
  }
  return false;
}

int searchInRotatedArray(int *arr, int n, int key) {
  int start = 0;
  int end = n - 1;
  while (start <= end) {
    int mid = start + (end - start) / 2; // No Overflow
    if (arr[mid] == key) {
      return mid;
    }
    if (arr[start] <= arr[mid]) {
      if (arr[start] <= key && arr[mid] >= key) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    } else {
      if (arr[mid] <= key && arr[end] >= key) {
        start = mid + 1;
      } else {
        end = mid - 1;
      }
    }
  }
  return -1;
}

int main() {
  int arr[7] = {6, 7, 0, 1, 2, 4, 5};
  int n = 7;

  cout << searchInRotatedArray(arr, n, 7);
  return 0;
}