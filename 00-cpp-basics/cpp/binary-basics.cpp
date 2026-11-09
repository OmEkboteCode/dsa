#include <cmath>
#include <iostream>
#include <limits>

using namespace std;

// Binary to Decimal
void binToDec(int bin) {
  int n = bin;
  int result = 0;
  int power = 1;
  while (n > 0) {
    int last = n % 10;
    if (last == 1) {
      result += last * power;
    }
    power *= 2;
    n /= 10;
  }
  cout << result << endl;
}

// Decimal To Binary

void decToBin(int dec) {
  int n = dec;
  int result = 0;
  int pow = 1;
  while (n > 0) {
    int rem = n % 2;
    result += rem * pow;
    n /= 2;
    pow *= 10;
  }
  cout << result;
}

// Number is power of 2

bool isPowerOfTwo(int n) {
  if (n <= 0)
    return false;
  while (n % 2 == 0) {
    n /= 2;
  }
  return n == 1;
}

// Number of 1s in binary

int countOnes(long long n) {
  int count = 0;
  while (n > 0) {
    int last = n % 10;
    if (last == 1) {
      count++;
    }
    n /= 10;
  }
  return count;
}

// Binary Addition
long long addBinary(long long a, long long b) {
  long long result = 0;
  long long place = 1;
  int carry = 0;

  while (a > 0 || b > 0 || carry > 0) {
    int digitA = a % 10;
    int digitB = b % 10;
    if (digitA > 1 || digitB > 1) {
      return -1;
    }

    int sum = digitA + digitB + carry;

    int bit = sum % 2;
    carry = sum / 2;

    result += bit * place;

    place *= 10;
    a /= 10;
    b /= 10;
  }
  return result;
}

int main() {
  cout << addBinary(10, 01);
  return 0;
}
