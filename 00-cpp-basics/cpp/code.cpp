#include <cmath>
#include <iomanip>
#include <iostream>

using namespace std;

// string evenOdd(int a) {
//   if (a % 2 == 0) {
//     return "Even";
//   } else {
//     return "Odd";
//   }
// }

int factorial(int a) {
  int fact = 1;
  for (int i = 1; i <= a; i++) {
    fact *= i;
  }
  return fact;
}

int bincofficient(int n, int r) {
  int value1 = factorial(n);
  int value2 = factorial(r);
  int value3 = factorial(n - r);
  int result = value1 / (value2 * value3);
  return result;
}

int sum(int a, int b) {
  cout << a + b << endl;
  return a + b;
}

int sum(int a, int b, int c) {
  cout << a + b + c << endl;
  return a + b + c;
}

// bool isPrime(int n) {
//   for (int i = 2; i <= n - 1; i++) {
//     if (n % i == 0) {
//       return false;
//     }
//   }
//   return true;
// }

// void allPrimes(int n) {
//   // All Primes from 2 to n;
//   for (int i = 2; i <= n; i++) {
//     if (isPrime(i)) {
//       cout << i << " ";
//     }
//   }
// }

int reverse(int n) {
  int res = 0;
  while (n > 0) {
    int lastDig = n % 10;
    res = res * 10 + lastDig;
    n = n / 10;
  }
  return res;
}

bool isPalindrome(int num) {
  int revNum = reverse(num);
  return num = revNum;
}

int digitSum(int n) {
  int result = 0;
  while (n > 0) {
    int last = n % 10;
    result += last;
    n /= 10;
  }
  return result;
}

int algebraIdentity(int a, int b) {
  int result = ((a * a) + (b * b) + 2 * a * b);
  return result;
}

int largest(int a, int b, int c) {
  if (a > b && a > c) {
    return a;
  } else if (b > c) {
    return b;
  } else {
    return c;
  }
}

char nextChar(char ch) {
  if (ch == 'z') {
    return 'a';
  } else {
    return ch + 1;
  }
}

int countDigits(int a) {
  if (a == 0)
    return 1;
  int count = 0;
  while (a > 0) {
    a /= 10;
    count++;
  }
  return count;
}

bool isPrime(int n) {
  int isPrime = false;
  for (int i = 1; i * i <= n; i++) {
    if (n % i == 0) {
      return false;
    }
  }
  return true;
}

// bool isPalindrome(int n) {
//   if (n < 0)
//     return false;
//   int current = n, result = 0;
//   int last = n % 10;
//   while (current > 0) {
//     result = result * 10 + last;
//     current /= 10;
//   }
//   return current == n;
// }

bool isArmstrong(int n) {
  if (n < 0)
    return false;
  int sum = 0;
  int current = n;
  while (current > 0) {
    int last = current % 10;
    sum += last * last * last;
    current /= 10;
  }
  return sum == n;
}

void binToDec(int binNum) {
  int n = binNum;
  int decNum = 0;
  int power = 1; // 2^0 2^1
  while (n > 0) {
    int lastDig = n % 10;
    decNum += lastDig * power;
    power *= 2;
    n = n / 10;
  }
  cout << decNum << endl;
}

void decToBin(int decNum) {
  int n = decNum;
  int pow = 1;
  int binNum = 0;

  while (n > 0) {
    int rem = n % 2;
    binNum += rem * pow;
    n /= 2;
    pow *= 10;
  }
  cout << "Binary of "<<decNum<<": "<<binNum << endl;
}

int strToDec(string bin){
  int n = bin.length();
  int power = 0;
  int result = 0;

  for(int i = n-1; i>=0; i--){
    if(bin[i] == '1'){
      result+= pow(2,power);
    }
    power++;
  }
  return result;
}

int main() {
  int a = 10;
  int *ptr = &a;
  float pi = 3.14;
  float *ptr2 = &pi;
  // cout<< &a<< " = "<< ptr<< endl;
  // cout<< "Pi"<< ptr2;

  cout << sizeof(ptr)<< endl;
  cout << sizeof(ptr2)<< endl;
  return 0;
}
