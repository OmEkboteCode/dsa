#include <iostream>

using namespace std;

// void changeA(int a){
//     a = 20 ;
//     cout << a<< endl;
// }

// Pass by reference using Pointer
//  void changeA(int *ptr){
//      *ptr = 20 ;
//      cout << *ptr<< endl;
//  }
// Pass by reference using Reference Variable
// void changeA(int &param) {
//   param = 20;
//   cout << param << endl;
// }

// void swap(int *p1, int *p2) {
//   int temp = *p1;
//   *p1 = *p2;
//   *p2 = temp;
//   cout << *p1 << " " << *p2 << endl;
// }

void modifyValue(int a) { a = a + 5; }

void modifyByReference(int &b) { b = b + 5; }

void swapByReference(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

void increaseValue(int *ptr, int amount){
    if(ptr == nullptr){
        cout<< "Pointer is not pointing any object";
    } else{
        *ptr+=amount;
        cout<<*ptr<<endl;
    }
}

int main() {

    //53
    int x = 5;
    cout<<x<<endl;
    increaseValue(&x, 10);
    //52
    // int a = 5, b = 10;
    // cout<< a<< " " << b<< endl;
    // swapByReference(a, b);
    // cout<< a<< " " << b<< endl;
  // Q51
  //  int a = 5;
  //  cout<< a<< endl;
  //  modifyValue(a);
  //  cout<< a<< endl;
  //  modifyByReference(a);
  //  cout<<a<< endl;
  //   int a = 10;
  //   int *ptr = &a;
  //   float pi = 3.14;
  //   float *ptr2 = &pi;
  // cout<< &a<< " = "<< ptr<< endl;
  // cout<< "Pi"<< ptr2;

  //   int **pptr = &ptr;

  //   cout << sizeof(ptr)<< endl;
  //   cout << sizeof(ptr2)<< endl;
  // *ptr = 20;
  // cout<< *ptr << " = " << *(&a) << endl;

  // int *ptr = nullptr;
  // cout<< ptr << endl;
  // cout<< &ptr<< endl;
  // cout<< *ptr<< endl;

  // int a = 10;
  // // int &b = a;
  // // b = 25;
  // // cout<< b << endl;
  // // cout<< a << endl;
  // int *ptr = &a;
  // cout<< ptr;
  // // changeA(a);

  // cout<< a << endl;

  // int x = 10, y = 15;
  // int *ptr1 = &x, *ptr2 = &y;

  // ptr2=ptr1;
  // float* a, b;
  // // cout<< ptr2<< " = "<< ptr1;
  // int *ptr = 0;
  // cout<< &ptr;

  // Q40
  // int x;
  // int *ptr;
  // x=7;
  // ptr = &x;
  // cout<<ptr;

  // Q48
  // int a = 10;
  // int *ptr = &a;

  // *ptr = 20;

  // cout<< *ptr<< endl;
  // cout<< a<< endl;

  // Q49
  //   int a = 10;
  //   int b = 20;
  //   cout << a << " " << b << endl;
  //   swap(&a, &b);
  //   cout << a << " " << b << endl;

  //   int *ptr = nullptr;

  //   if(ptr == nullptr){
  //     cout<< "Pointer is not pointing to any object";
  //   } else{
  //     cout<<*ptr<<endl;
  //   }

  return 0;
}