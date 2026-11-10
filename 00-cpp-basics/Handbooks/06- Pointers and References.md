# Module 12: Introduction to Pointers in C++



Rebuilt with the complete handbook framework

DSA foundation



This is the revised version. We're retaining the four substantial concept chunks, but now What → So What → Now What is an explicit part of every chunk.

The distinction matters:

- What? Builds understanding.
- So What? Establishes why the concept matters.
- Now What? Turns understanding into practical ability.

These are not three more question banks. They're the reasoning thread connecting the explanation, its significance and its application.

# Module overview

[Pointers vs References in C++ - Scaler Topics](https://images.openai.com/static-rsc-4/q8-pvR0ZdK21vLUIetZ0u9M7v0J74OD684_V06M6BoMm1AH1cFziQ7uJ2PayNJrkJeRQMIh1wyqwJfS9Yj2hbWO8kzKOW9zzxaFGyZJZftGb2AM-CX--3yRL3GCkHHSpAnV8lKRiyxSkNfEYwY2EjuWF_Ma4xPJLS-V_EEPjN-o?purpose=inline)

[scaler.com](https://www.scaler.com/topics/pointers-vs-references-in-cplusplus/?utm_source=chatgpt.com)

## Syllabus coverage

Based on your Sigma screenshot:

| Sigma topic                           | Learning chunk           |
| ------------------------------------- | ------------------------ |
| Basic Concepts of Memory              | 1                        |
| Address-of (`&`) Operator             | 1                        |
| What Are Pointers?                    | 2                        |
| Dereference Operator                  | 2                        |
| Null Pointers                         | 3                        |
| Passing Arguments: Value vs Reference | 4                        |
| Reference Variables                   | 4                        |
| Practice Questions                    | Programming and DSA labs |

## Learning objectives

By the end of the module, you should be able to:

- Explain how variables occupy memory and how addresses identify objects.
- Declare, initialise and use pointers.
- Access and modify objects through pointers.
- Recognise null, uninitialised and dangling pointers.
- Distinguish pass-by-value from pass-by-reference.
- Understand reference variables and their differences from pointers.
- Read unfamiliar pointer-based code and explain its behaviour.
- Apply these ideas to foundational data structures.

# Part I: Concept Learning

## Chunk 1: Understanding Memory and Addresses



High priority

Foundation



### Learning prompt

Imagine explaining to someone how a computer stores variables internally. What is memory? How do variables occupy memory? What is a memory address? How does the address-of operator help us obtain that address? Demonstrate the difference between a variable's value and its address using C++ code, and explain why understanding addresses is necessary before learning pointers.

### Model answer

What is memory?

Computer memory is where data and instructions required during program execution are stored.

Consider:

```
int age = 20;
```

When this statement executes, the computer creates an integer object named `age` and initialises it with `20`.

That object occupies space in memory.

Think of memory as a large collection of numbered storage locations. Each addressable byte has an address identifying its location.

A variable occupies one or more bytes, and its address identifies the starting location of that object.

Illustrative memory layout

Memory address

Stored object

`0x1000`

20

`age`

`0x1004`

95

`marks`

`0x1008`

'A'

`grade`

These addresses are illustrative, not guaranteed actual locations or spacing.

A variable has two important aspects:

- Value: The data stored in the object.
- Address: The memory location where the object begins.

Address-of operator

C++ provides the address-of operator `&` to obtain an object's address.

```
#include <iostream>
using namespace std;

int main() {
    int age = 20;

    cout << "Value: " << age << endl;
    cout << "Address: " << &age << endl;

    return 0;
}
```

Possible output:

```
Value: 20
Address: 0x7ffe1234
```

The actual address will vary.

Read the code naturally:

- `int age = 20`: Create an integer object and initialise it.
- `cout << age`: Print the stored value.
- `cout << &age`: Obtain and print its address.

We can also inspect the size of an object:

```
int age = 20;

cout << sizeof(age);
```

On many systems, this prints `4`, meaning the object occupies four bytes. The exact size depends on the implementation.

### Hinglish explanation

Jab hum likhte hain:

```
int age = 20;
```

toh computer memory mein `age` naam ka integer object banata hai aur usmein `20` store karta hai.

Memory ko numbered storage locations ki tarah imagine karo. Har addressable byte ka ek address hota hai.

- `age` se value milti hai.
- `&age` se memory address milta hai.
- `sizeof(age)` se object ka size bytes mein pata chalta hai.

Value aur address alag cheezein hain. Yeh difference pointers samajhne ki foundation hai.

### What → So What → Now What

WHAT?

A variable is an object stored in memory. Its value is the data it contains, and its address identifies its starting memory location.

SO WHAT?

Understanding addresses allows us to work with objects indirectly. Without this idea, pointers would simply look like strange variables containing mysterious numbers.

NOW WHAT?

Practise distinguishing `x` from `&x`. Be able to explain why one represents a value and the other represents a location.

### Smart Notes

- Memory stores data and instructions used during execution.
- A variable occupies one or more bytes.
- An address identifies a memory location.
- `&variable` obtains the address of an object.
- `sizeof()` returns the object's size in bytes.
- Actual addresses depend on the program and system.

### DSA connection

DSA foundation

Addresses provide the foundation for indirect access to data. Later, pointers will connect objects in linked lists, trees and graphs, even when those objects are not stored next to one another.

## Chunk 2: Pointers and Dereferencing



High priority

DSA foundation



### Learning prompt

You understand memory addresses. Now explain how a pointer stores an address, how pointer declarations and initialisation work, and how dereferencing allows us to access or modify the original object. Demonstrate the relationship between a variable, its address, a pointer and the dereference operator. Also explain the two different roles of `*` in pointer declarations and expressions.

### Model answer

What is a pointer?

A pointer is a variable that stores the memory address of another object.

Consider:

```
int age = 20;
int* ptr = &age;
```

Here:

- `age` stores the integer value `20`.
- `&age` obtains the address of `age`.
- `ptr` stores that address.
- Therefore, `ptr` points to `age`.

Pointer: `ptr`

## Address of age

Stores the address of age

Points to

Integer: `age`

# 20

Stores the actual integer value

Pointer declaration

General syntax:

```
dataType* pointerName;
```

Examples:

```
int* ptr;
float* fptr;
char* cptr;
double* dptr;
```

The pointer type indicates the type of object it is intended to point to.

You may also see:

```
int *ptr;
```

Both forms are valid. Spacing does not change the meaning.

A common declaration trap:

```
int* p1, p2;
```

Only `p1` is a pointer. `p2` is an ordinary integer.

Prefer:

```
int* p1;
int p2;
```

Dereferencing

A pointer stores an address. To access the object at that address, we use the dereference operator `*`.

```
int age = 20;
int* ptr = &age;

cout << *ptr;
```

Output:

```
20
```

The expression `*ptr` means:

Access the object located at the address stored inside `ptr`.

Since `ptr` points to `age`, dereferencing it accesses `age`.

We can also modify the object:

```
int age = 20;
int* ptr = &age;

*ptr = 50;

cout << age;
```

Output:

```
50
```

The statement `*ptr = 50` accesses the object pointed to by `ptr` and replaces its value with `50`.

The two roles of `*`

```
int* ptr = &age;
```

Here, `*` is part of the pointer declaration.

```
cout << *ptr;
```

Here, `*` is the dereference operator.

Context determines its role.

Complete demonstration

```
#include <iostream>
using namespace std;

int main() {
    int x = 10;

    int* ptr = &x;

    cout << x << endl;
    cout << &x << endl;
    cout << ptr << endl;
    cout << *ptr << endl;

    *ptr = 100;

    cout << x << endl;

    return 0;
}
```

Possible output:

```
10
0x7ffe1234
0x7ffe1234
10
100
```

The address printed by `&x` and `ptr` is the same because `ptr` stores the address of `x`.

### Hinglish explanation

Pointer ek variable hota hai jo kisi doosre variable ka memory address store karta hai.

```
int x = 10;
int* ptr = &x;
```

`ptr` ke andar `10` nahi hai. Uske andar `x` ka address hai.

Agar humein pointer ke through actual value access karni hai:

```
cout << *ptr;
```

Aur agar modify karni hai:

```
*ptr = 50;
```

Toh original variable `x` ki value `50` ho jayegi.

Yaad rakho:

- `ptr` address deta hai.
- `*ptr` pointed-to object access karta hai.
- `*ptr = value` original object ko modify karta hai.

### What → So What → Now What

WHAT?

A pointer stores an object's address. Dereferencing accesses the object at that address.

SO WHAT?

We can access and modify objects indirectly. This lets different parts of a program work with the same underlying data without needing to know the object's variable name.

NOW WHAT?

Practise reading `ptr`, `&x` and `*ptr` without hesitation. Then learn to distinguish pointer reassignment from modification of the pointed-to object.

### Smart Notes

- A pointer stores an address.
- `int* ptr` declares a pointer to an integer.
- `ptr = &x` stores the address of `x`.
- `*ptr` accesses the pointed-to object.
- `*ptr = value` modifies the pointed-to object.
- `ptr` and `*ptr` are different expressions.
- `*` has different roles in declarations and expressions.

### DSA connection

DSA foundation

Linked lists use pointers to connect nodes. Trees use pointers to connect parent and child nodes. These structures become easier to understand once you can mentally follow where a pointer leads and what object it accesses.

## Chunk 3: Null Pointers and Pointer Safety

High priority

### Learning prompt

What happens when a pointer does not point to a valid object? Explain uninitialised pointers, null pointers, `nullptr`, and null checks. Why is dereferencing a null pointer unsafe? Also distinguish null pointers from dangling pointers, using examples to demonstrate safe and unsafe pointer usage.

### Model answer

What is a null pointer?

A null pointer is a pointer that does not point to an object or function.

Modern C++ uses `nullptr` to represent a null pointer.

```
int* ptr = nullptr;
```

This means `ptr` currently points to no object.

Why do we need this?

Imagine writing a function that may or may not receive an object. A null pointer provides a way to represent the absence of an object.

Uninitialised pointers

Consider:

```
int* ptr;
```

This declares a pointer without initialising it.

For a local pointer, its value is indeterminate. We cannot safely assume that it contains a valid address.

This is unsafe:

```
cout << *ptr;
```

Dereferencing an uninitialised pointer causes undefined behaviour.

A better approach is:

```
int* ptr = nullptr;
```

Now we know its initial state.

Checking for null

Before dereferencing a pointer that may be null, check it:

```
if (ptr != nullptr) {
    cout << *ptr;
}
```

Complete example:

```
#include <iostream>
using namespace std;

int main() {
    int* ptr = nullptr;

    if (ptr == nullptr) {
        cout << "No object is being pointed to";
    }

    return 0;
}
```

Output:

```
No object is being pointed to
```

Why is dereferencing null unsafe?

```
int* ptr = nullptr;

cout << *ptr;
```

The expression `*ptr` attempts to access an object through a pointer that points to no object.

This is undefined behaviour. It may crash, but C++ does not guarantee a particular outcome.

Null pointers versus dangling pointers

A null pointer explicitly represents the absence of an object.

A dangling pointer refers to an object whose lifetime has ended.

Consider:

```
int* getAddress() {
    int x = 10;
    return &x;
}
```

This function is incorrect because `x` is a local object. Its lifetime ends when the function returns.

The returned pointer no longer refers to a living object.

A dangling pointer can still be non-null. This means that checking `ptr != nullptr` is not sufficient to prove that the pointer is valid.

### Hinglish explanation

Pointer safety ka matlab hai ki hum invalid memory ko access na karein.

```
int* ptr = nullptr;
```

Iska matlab pointer kisi object ko point nahi kar raha.

Agar hum likhen:

```
*ptr = 100;
```

toh hum ek invalid object ko modify karne ki koshish kar rahe hain. Yeh undefined behaviour hai.

Isliye nullable pointer ko dereference karne se pehle check karna chahiye.

Lekin ek important baat: non-null pointer bhi invalid ho sakta hai. Dangling pointer iska example hai. Uska address kisi aise object ka hota hai jiska lifetime khatam ho chuka hai.

### What → So What → Now What

WHAT?

`nullptr` represents a pointer that points to no object. An uninitialised pointer has an indeterminate value, while a dangling pointer refers to an object whose lifetime has ended.

SO WHAT?

Pointers give us powerful indirect access, but invalid access can cause undefined behaviour. Understanding pointer states is essential for writing reliable C++ programs.

NOW WHAT?

Initialise pointers deliberately, check nullable pointers before dereferencing, and learn to reason about object lifetimes. Never assume that a non-null address is automatically safe.

### Smart Notes

- `nullptr` represents a null pointer.
- An uninitialised local pointer has an indeterminate value.
- Dereferencing null causes undefined behaviour.
- Check pointers that may be null before dereferencing.
- A non-null pointer can still be invalid.
- A dangling pointer refers to an object whose lifetime has ended.
- Safe pointer usage requires understanding object lifetime.

### DSA connection

DSA foundation

In a singly linked list, the last node commonly has its `next` pointer set to `nullptr`. This represents the absence of another node.

[An Introduction to Linked Lists | Definition | Representation | Types | by Pepcoding | Medium](https://images.openai.com/static-rsc-4/Us0egj4x-mrsxVYdb5ShYe-qVad3u0gSr25sosBK9xsHb7deFCOMIj8IwtIcIAcOjHvwhxowOFgcZ47k12hgHGung4R_qZnxw_Ocn25-hv-PHkDGN7pdPNQtWV2eSzYz8I6g0TQdTWm6lr34bFdJdp23bQ0WESwMXbWy_jUoxOs?purpose=inline)

[medium.com](https://medium.com/%40pepcoding/an-introduction-to-linked-lists-definition-representation-types-a5337b908855?utm_source=chatgpt.com)

When we eventually traverse a linked list, we'll use this condition to recognise when we have reached the end.

## Chunk 4: Function Arguments, Pass-by-Value, Pass-by-Reference and Reference Variables



High priority

Long-term value



### Learning prompt

A function often needs to work with variables created outside it. Explain what happens when arguments are passed by value and by reference. Why does modifying a copied parameter not affect the original variable, while modifying a reference parameter does? Then explain reference variables as aliases, their declaration rules and their differences from pointers. Use a swap function to demonstrate the practical importance of these concepts.

### Model answer

Why does argument passing matter?

Consider:

```
int x = 10;

change(x);
```

When a function receives `x`, how it interacts with the original variable depends on the parameter declaration.

Two important mechanisms are pass-by-value and pass-by-reference.

Pass-by-value

When an argument is passed by value, the function receives a separate parameter object initialised with the argument's value.

```
#include <iostream>
using namespace std;

void change(int x) {
    x = 100;
}

int main() {
    int a = 10;

    change(a);

    cout << a;

    return 0;
}
```

Output:

```
10
```

Why?

The function modifies its own parameter `x`, not the original object `a`.

Imagine giving someone a photocopy of a document. They can modify their copy without changing your original.

Pass-by-reference

When an argument is passed by reference, the parameter becomes another name for the original object.

Syntax:

```
void change(int &x)
```

Example:

```
#include <iostream>
using namespace std;

void change(int &x) {
    x = 100;
}

int main() {
    int a = 10;

    change(a);

    cout << a;

    return 0;
}
```

Output:

```
100
```

Here, `x` is an alias for `a`. Both names refer to the same object.

This means modifying `x` modifies the original `a`.

| Pass-by-value                       | Pass-by-reference                 |
| ----------------------------------- | --------------------------------- |
| Creates a separate parameter object | Parameter aliases original object |
| Changes do not modify original      | Changes modify original           |
| `int x`                             | `int &x`                          |

Practical application: Swapping two numbers

Suppose we want to swap the values of two integers.

A pass-by-value implementation:

```
void swapNumbers(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}
```

This only swaps local copies. The original variables remain unchanged.

We need to modify the original objects, so we use references:

```
void swapNumbers(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}
```

Complete program:

```
#include <iostream>
using namespace std;

void swapNumbers(int &a, int &b) {
    int temp = a;

    a = b;
    b = temp;
}

int main() {
    int x = 10;
    int y = 20;

    swapNumbers(x, y);

    cout << x << " " << y;

    return 0;
}
```

Output:

```
20 10
```

The original objects are swapped because the parameters refer to them.

Reference variables

A reference variable is another name for an existing object.

```
int x = 10;

int &ref = x;
```

Now `x` and `ref` refer to the same object.

```
ref = 50;

cout << x;
```

Output:

```
50
```

There are two important rules.

Rule 1: A reference must be initialised when declared.

Valid:

```
int x = 10;
int &ref = x;
```

Invalid:

```
int &ref;
```

An ordinary reference must be bound to an object at declaration.

Rule 2: A reference cannot be reseated.

Consider:

```
int a = 10;
int b = 20;

int &ref = a;

ref = b;
```

Does `ref` now refer to `b`?

No.

The reference remains bound to `a`. The statement assigns the value of `b` to the object referred to by `ref`.

Final values:

```
a = 20
b = 20
```

Pointers versus references

| Feature                            | Pointer                        | Reference                          |
| ---------------------------------- | ------------------------------ | ---------------------------------- |
| Represents                         | Address stored in a variable   | Alias for an object                |
| Declaration                        | `int* p = &x;`                 | `int &r = x;`                      |
| Can be null                        | Yes                            | Ordinary references cannot be null |
| Can be reseated                    | Yes                            | No                                 |
| Access object                      | `*p`                           | `r`                                |
| Must be initialised at declaration | Not necessarily, but should be | Yes                                |

The central distinction is that a pointer is an object that stores an address, while a reference is another name for an existing object.

### Hinglish explanation

Jab hum function ko variable pass karte hain, toh do important situations hoti hain.

Pass-by-value: Function ko original variable ki copy milti hai.

```
void change(int x) {
    x = 100;
}
```

Original variable `a = 10` ho, toh `x` ko modify karne se `a` change nahi hoga.

Pass-by-reference: Function original variable ko hi access karta hai through another name.

```
void change(int &x) {
    x = 100;
}
```

Ab `x` aur original variable same object ko refer karte hain. Isliye modification original variable mein reflect hota hai.

Reference variable bhi isi concept par based hai:

```
int a = 10;
int &ref = a;
```

Ab `a` aur `ref` same object ke do names hain.

Agar `ref = 50;` likhenge, toh `a` bhi `50` ho jayega.

Lekin reference ko baad mein kisi doosre variable se attach nahi kar sakte.

### What → So What → Now What

WHAT?

Pass-by-value gives a function a separate parameter object. Pass-by-reference gives it an alias for the original object. A reference variable is another name for an existing object.

SO WHAT?

Functions can either work independently on copies or modify existing data. This choice affects correctness, efficiency and the design of reusable functions.

NOW WHAT?

Practise writing swap functions using references and pointers. When reading a function, inspect its parameter declarations before deciding whether the caller's variables can change.

### Smart Notes

- Pass-by-value creates a separate parameter object.
- Pass-by-reference creates an alias for the original object.
- A reference is another name for an existing object.
- References must be initialised at declaration.
- References cannot be reseated.
- A pointer stores an address; a reference is an alias.
- References are useful when a function must work with an existing object.
- Pointers are useful when an interface needs to represent absence or allow pointer reassignment.

### DSA connection

DSA foundation

References and pointers are used throughout data structures and algorithms.

- References allow functions to modify existing objects.
- Pointer parameters allow indirect access to data.
- Linked lists and trees use pointers to connect nodes.
- Sorting algorithms use functions that modify existing collections.

# Part II: Programming Problems

The concept chunks have established the mental models. Now we'll turn them into programming ability.

The progression is:

1. Beginner: fully worked examples.
2. Intermediate: guided reasoning with complete solutions.
3. Advanced: independent-style problems with model solutions.
4. Challenge: design decisions, correctness and complexity.

No exercise is left without an answer.

## Beginner: Fully worked problems

### Problem 1: Print a variable's value and address

Task: Create an integer variable and print its value and memory address.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int num = 25;

    cout << "Value: " << num << endl;
    cout << "Address: " << &num << endl;

    return 0;
}
```

Explanation: `num` accesses the value, while `&num` obtains its address.

### Problem 2: Access a variable using a pointer

Task: Create an integer, store its address in a pointer, and print its value through that pointer.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int num = 40;

    int* ptr = &num;

    cout << *ptr;

    return 0;
}
```

Output:

```
40
```

Explanation: `ptr` stores the address of `num`. Dereferencing it accesses the integer stored there.

### Problem 3: Modify a variable using a pointer

Task: Change an integer's value to `75` using a pointer.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int num = 10;

    int* ptr = &num;

    *ptr = 75;

    cout << num;

    return 0;
}
```

Output:

```
75
```

Explanation: The assignment through `*ptr` modifies the original object.

### Problem 4: Swap two numbers using references

Task: Write a function that swaps two integers using reference parameters.

Solution

```
#include <iostream>
using namespace std;

void swapNumbers(int &a, int &b) {
    int temp = a;

    a = b;
    b = temp;
}

int main() {
    int x = 5;
    int y = 15;

    swapNumbers(x, y);

    cout << x << " " << y;

    return 0;
}
```

Output:

```
15 5
```

Explanation: Both parameters refer to the original variables, so the swap affects the caller's data.

## Intermediate: Guided problems with complete solutions

### Problem 5: Increment a number through a pointer

Task: Write a function that accepts an integer pointer and increments the pointed-to value by one. Handle null pointers safely.

Guided reasoning:

- Accept an `int*` parameter.
- Check whether it is `nullptr`.
- Dereference it and increment the value.
- Call the function with an integer's address.

Complete solution

```
#include <iostream>
using namespace std;

void increment(int* ptr) {
    if (ptr != nullptr) {
        (*ptr)++;
    }
}

int main() {
    int num = 10;

    increment(&num);

    cout << num;

    return 0;
}
```

Output:

```
11
```

Explanation: The function receives the address of `num`. The pointed-to value is incremented, so the original variable changes.

### Problem 6: Calculate the sum using reference parameters

Task: Write a function that accepts two integers by reference and returns their sum.

Solution

```
#include <iostream>
using namespace std;

int calculateSum(int &a, int &b) {
    return a + b;
}

int main() {
    int x = 25;
    int y = 35;

    cout << calculateSum(x, y);

    return 0;
}
```

Output:

```
60
```

Explanation: The function accesses the original integers through reference parameters. It does not need to modify them.

### Problem 7: Reset a variable through a pointer

Task: Create a function that sets the pointed-to integer to zero.

Solution

```
#include <iostream>
using namespace std;

void reset(int* ptr) {
    if (ptr != nullptr) {
        *ptr = 0;
    }
}

int main() {
    int num = 99;

    reset(&num);

    cout << num;

    return 0;
}
```

Output:

```
0
```

### Problem 8: Find the maximum using pointer parameters

Task: Write a function that accepts two integer pointers and returns the larger value. If either pointer is null, return `0` as the chosen fallback.

Solution

```
#include <iostream>
using namespace std;

int maximum(int* p1, int* p2) {
    if (p1 == nullptr || p2 == nullptr) {
        return 0;
    }

    if (*p1 > *p2) {
        return *p1;
    }

    return *p2;
}

int main() {
    int a = 45;
    int b = 30;

    cout << maximum(&a, &b);

    return 0;
}
```

Output:

```
45
```

Explanation: The function receives addresses, dereferences them to compare the values, and returns the larger one.

## Advanced: Independent-style problems with complete solutions

### Problem 9: Rotate three values using references

Task: Transform three values from `a, b, c` into `b, c, a`.

Solution

```
#include <iostream>
using namespace std;

void rotateValues(int &a, int &b, int &c) {
    int temp = a;

    a = b;
    b = c;
    c = temp;
}

int main() {
    int x = 10;
    int y = 20;
    int z = 30;

    rotateValues(x, y, z);

    cout << x << " " << y << " " << z;

    return 0;
}
```

Output:

```
20 30 10
```

Explanation: The temporary variable preserves the original value of `a` while the other values shift.

### Problem 10: Swap two integers using pointers

Task: Write a function that swaps two integers using pointer parameters.

Solution

```
#include <iostream>
using namespace std;

void swapNumbers(int* p1, int* p2) {
    if (p1 != nullptr && p2 != nullptr) {
        int temp = *p1;
        *p1 = *p2;
        *p2 = temp;
    }
}

int main() {
    int a = 100;
    int b = 200;

    swapNumbers(&a, &b);

    cout << a << " " << b;

    return 0;
}
```

Output:

```
200 100
```

Explanation: The pointers contain the addresses of the original variables. Dereferencing them allows the function to exchange the original values.

### Problem 11: Add five to a variable through a pointer

Task: Write a function that adds five to an integer using a pointer.

Solution

```
#include <iostream>
using namespace std;

void addFive(int* ptr) {
    if (ptr != nullptr) {
        *ptr += 5;
    }
}

int main() {
    int num = 25;

    addFive(&num);

    cout << num;

    return 0;
}
```

Output:

```
30
```

### Problem 12: Modify two variables using pointers

Task: Add ten to the first variable and subtract five from the second.

Solution

```
#include <iostream>
using namespace std;

void modify(int* p1, int* p2) {
    if (p1 != nullptr && p2 != nullptr) {
        *p1 += 10;
        *p2 -= 5;
    }
}

int main() {
    int a = 20;
    int b = 30;

    modify(&a, &b);

    cout << a << " " << b;

    return 0;
}
```

Output:

```
30 25
```

## Challenge: Design and correctness

### Problem 13: Check whether a pointer is null

Task: Create a function returning `true` if a pointer is null and `false` otherwise.

Solution

```
#include <iostream>
using namespace std;

bool isNull(int* ptr) {
    return ptr == nullptr;
}

int main() {
    int x = 10;

    int* p1 = &x;
    int* p2 = nullptr;

    cout << isNull(p1) << endl;
    cout << isNull(p2) << endl;

    return 0;
}
```

Output:

```
0
1
```

C++ streams print `false` as `0` and `true` as `1` by default.

### Problem 14: Find and correct the pointer bug

Task: Explain why this program does not change `a`, then correct it.

```
void change(int* p) {
    int x = 100;
    p = &x;
}

int main() {
    int a = 10;
    int* ptr = &a;

    change(ptr);

    cout << a;
}
```

Solution and explanation

Output:

```
10
```

The parameter `p` is a copy of the pointer `ptr`.

Reassigning `p` changes only the local pointer. It doesn't change the original pointer or the integer `a`.

If the intention is to modify `a`, use:

```
void change(int* p) {
    if (p != nullptr) {
        *p = 100;
    }
}
```

Now the function modifies the object through the copied address.

Developer insight: Passing a pointer by value copies the address, not the pointed-to object. Both pointers can still access the same object.

# Part III: Developer's Code Reading Lab

Long-term value

The goal is to understand unfamiliar code, not just predict output.

For each example, practise reading the syntax aloud while reasoning about intent, variable responsibilities, data flow and correctness.

## Reading challenge 1: Multiple pointers to one variable

```
int x = 10;

int* p1 = &x;
int* p2 = &x;

*p1 = 50;

cout << *p2;
```

Developer's narration

Create an integer `x` with value `10`. Create two integer pointers, both storing the address of `x`. Access the object through `p1` and change its value to `50`. Finally, access that same object through `p2` and print the updated value.

Output:

```
50
```

Reasoning: Both pointers refer to the same object. Modifying the object through one pointer is visible through the other.

## Reading challenge 2: Pointer reassignment versus value modification

```
int a = 10;
int b = 20;

int* ptr = &a;

ptr = &b;

cout << a << " " << *ptr;
```

Developer's narration

Create two separate integers. Initially, `ptr` stores the address of `a`. Reassign it so that it stores the address of `b`. The final expression prints the original value of `a` and the value accessed through `ptr`, which is now `b`.

Output:

```
10 20
```

Reasoning: Reassigning a pointer changes which object it points to. It does not automatically modify either object.

## Reading challenge 3: Understand copied pointer parameters

```
void update(int* p) {
    *p = 100;
    p = nullptr;
}

int main() {
    int x = 10;
    int* ptr = &x;

    update(ptr);

    cout << x;
}
```

Developer's narration

The function receives a copy of the pointer's address. It first dereferences that pointer and changes the original integer to `100`. Then it sets its local pointer copy to null. This does not affect the caller's pointer or undo the modification to the integer.

Output:

```
100
```

Reasoning: Modifying the pointed-to object and modifying the pointer variable are two different operations.

## Reading challenge 4: Compare reference and value parameters

```
void process(int a, int &b) {
    a += 10;
    b += 20;
}

int main() {
    int x = 5;
    int y = 5;

    process(x, y);

    cout << x << " " << y;
}
```

Developer's narration

The function receives a separate copy of `x` as `a` and a reference to `y` as `b`. Adding ten changes only the local copy. Adding twenty through the reference changes the original `y`.

Output:

```
5 25
```

Reasoning: Inspect parameter declarations before deciding whether the caller's variables can change.

## Reading challenge 5: Identify an unsafe operation

```
int* getPointer() {
    int num = 50;
    return &num;
}
```

Developer's narration

The function creates a local integer and returns its address. However, the local object's lifetime ends when the function returns. The returned pointer no longer provides valid access to that object.

Correct principle: Never use a pointer to access an object after its lifetime has ended.

## Reading challenge 6: Trace a pointer-based calculation

```
void calculate(int* p) {
    if (p == nullptr) {
        return;
    }

    *p *= 2;

    int temp = *p;

    *p = temp + 10;
}

int main() {
    int num = 5;

    calculate(&num);

    cout << num;
}
```

Developer's narration

The function receives the address of `num`. It checks whether the pointer is null. If it is, the function returns immediately. Otherwise, it doubles the pointed-to value, copies the updated value into `temp`, adds ten and stores the result back in the original object.

Output:

```
20
```

Reasoning: Follow the object being modified, not just the variable names appearing in the expressions.

### Code Reading mastery checklist

- Recognise pointer declarations and dereferencing.
- Explain what an address is being used for.
- Follow pointer reassignment.
- Distinguish modifying a pointer from modifying its target.
- Understand function parameter behaviour.
- Detect invalid lifetime and null-pointer operations.
- Explain code in clear, natural English.

# Part IV: DSA Mastery Lab

Transferable problem-solving skills

The concept chunks taught you how pointers work. This lab develops your ability to reason about them in unfamiliar situations.

## Guided challenge 1: Two pointers, one object

Problem: Two pointers point to the same integer. Modify the integer through the first pointer and print its value through the second.

Reasoning: Both pointers store the same address, so they access the same object.

Complete solution

```
#include <iostream>
using namespace std;

int main() {
    int num = 10;

    int* p1 = &num;
    int* p2 = &num;

    *p1 = 90;

    cout << *p2;

    return 0;
}
```

Output:

```
90
```

## Guided challenge 2: Modify an object conditionally

Problem: Write a function that makes a positive integer negative. Zero and negative values should remain unchanged.

Complete solution

```
void makeNegative(int* ptr) {
    if (ptr != nullptr && *ptr > 0) {
        *ptr = -(*ptr);
    }
}
```

Example:

```
int num = 25;

makeNegative(&num);

cout << num;
```

Output:

```
-25
```

Reasoning: First check the pointer, then inspect the pointed-to value. Modify it only when it is positive.

## Independent challenge 3: Implement the same operation using pointers and references

Problem: Write two functions that double an integer. One must use a pointer, and the other must use a reference.

Complete solution

```
void doubleUsingPointer(int* ptr) {
    if (ptr != nullptr) {
        *ptr *= 2;
    }
}

void doubleUsingReference(int &num) {
    num *= 2;
}
```

Usage:

```
int a = 5;
int b = 10;

doubleUsingPointer(&a);
doubleUsingReference(b);
```

Final values:

```
a = 10
b = 20
```

Reasoning: Both mechanisms can modify the original object. The pointer can represent the absence of an object with `nullptr`, while the reference requires an object.

## Advanced challenge 4: Understand pointer swapping

Problem: What happens when we execute this function?

```
void swapPointers(int* p1, int* p2) {
    int* temp = p1;
    p1 = p2;
    p2 = temp;
}
```

Complete answer

The function swaps its local pointer copies. The caller's pointer variables remain unchanged because pointers are passed by value.

If we want to swap the caller's pointer variables, we can use references to pointers:

```
void swapPointers(int* &p1, int* &p2) {
    int* temp = p1;
    p1 = p2;
    p2 = temp;
}
```

Now the original pointer variables are modified.

Developer insight: There are three different things to track:

1. The pointer variable itself.
2. The address stored in that pointer.
3. The object located at that address.

This distinction becomes increasingly important in advanced C++.

## Advanced challenge 5: Choose between a pointer and a reference

Problem: You are designing a function that updates a student's marks. Should it receive a pointer or a reference?

Complete answer

If the function always requires a valid marks object, a reference is a natural choice:

```
void updateMarks(int &marks) {
    marks += 5;
}
```

If the function must allow the absence of a marks object, a pointer can represent that possibility:

```
void updateMarks(int* marks) {
    if (marks != nullptr) {
        *marks += 5;
    }
}
```

The decision depends on the function's contract, not which syntax looks shorter.

## Advanced challenge 6: Analyse a pointer-based function

Problem: Explain the function's behaviour and calculate its complexity.

```
void process(int* p) {
    if (p == nullptr) {
        return;
    }

    *p *= 2;

    int temp = *p;

    *p = temp + 10;
}
```

Complete reasoning

Suppose the original integer is `5`.

1. Check whether `p` is null.
2. Double the pointed-to value: `5` becomes `10`.
3. Copy `10` into `temp`.
4. Add ten and store the result back: `20`.

Final value:

```
20
```

- Time complexity: \\(O(1)\\)
- Auxiliary space complexity: \\(O(1)\\)

Reasoning: The function performs a fixed number of operations, regardless of the input value.

# Part V: Module Checkpoints

These short checkpoints consolidate the major concepts. Each includes its complete answer.

## Checkpoint A: Memory and pointers

Q1. What does `&x` return?

Answer: The address of `x`.

Q2. What does `int* ptr` declare?

Answer: A pointer variable intended to point to an integer.

Q3. If `ptr` contains the address of `x`, what does `*ptr` access?

Answer: The object `x`.

Q4. Explain the difference between `ptr = &y` and `*ptr = 50`.

Answer: The first changes which object the pointer points to. The second modifies the object currently pointed to.

## Checkpoint B: Pointer safety

Q1. What does `nullptr` represent?

Answer: A pointer that points to no object or function.

Q2. Why is dereferencing an uninitialised pointer dangerous?

Answer: Its value is indeterminate, so it cannot safely be used to access an object.

Q3. Does a non-null pointer always point to a valid object?

Answer: No. It could be dangling or otherwise invalid.

Q4. What is a dangling pointer?

Answer: A pointer referring to an object whose lifetime has ended.

## Checkpoint C: Functions and references

Q1. Why does pass-by-value not change the caller's variable?

Answer: The function modifies a separate parameter object.

Q2. What does `int &x` mean in a function parameter?

Answer: `x` is a reference parameter that aliases the original integer.

Q3. Can an ordinary reference be reseated?

Answer: No. It remains bound to its original object.

Q4. How does passing a pointer by value differ from passing a reference?

Answer: A pointer parameter receives a copy of an address. A reference parameter aliases the original object.

# Part VI: Revision and Active Recall

## Smart Revision Sheet

Quick revision

| Concept                | Syntax              | Meaning                        |
| ---------------------- | ------------------- | ------------------------------ |
| Ordinary variable      | `int x = 10;`       | Stores a value                 |
| Address-of             | `&x`                | Obtains the address            |
| Pointer declaration    | `int* p;`           | Declares an integer pointer    |
| Pointer initialisation | `int* p = &x;`      | Stores x's address             |
| Dereferencing          | `*p`                | Accesses the pointed-to object |
| Modify through pointer | `*p = 50;`          | Changes the pointed-to object  |
| Null pointer           | `int* p = nullptr;` | Points to no object            |
| Null check             | `p == nullptr`      | Tests for null                 |
| Reference              | `int &r = x;`       | Creates another name for x     |
| Pass-by-value          | `void f(int x)`     | Receives a separate object     |
| Pass-by-reference      | `void f(int &x)`    | Receives an alias              |
| Pointer parameter      | `void f(int* p)`    | Receives an address by value   |

### Five critical distinctions

1. Value vs address: What is stored versus where it is stored.
2. Pointer vs pointed-to value: `ptr` versus `*ptr`.
3. Address-of vs dereference: `&x` versus `*ptr`.
4. Pointer reassignment vs object modification: `ptr = &y` versus `*ptr = 50`.
5. Pass-by-value vs pass-by-reference: Separate parameter object versus alias.

## Final Active Recall Test

### Q1. Trace the program.

```
int x = 10;
int* p = &x;

*p = *p + 5;

int y = *p;
y = y + 5;

cout << x << " " << y;
```

Complete solution

```
15 20
```

`x` is modified through the pointer. `y` receives a copy of the updated value and is then modified independently.

### Q2. Identify the behaviour.

```
int* p = nullptr;

if (p != nullptr) {
    cout << *p;
}
else {
    cout << "No valid object";
}
```

Complete solution

```
No valid object
```

The condition is false, so the `else` branch executes. No null dereferencing occurs.

### Q3. Explain the final values.

```
int a = 10;
int b = 20;

int* p = &a;
int &r = b;

*p = 50;
r = 80;

cout << a << " " << b;
```

Complete solution

```
50 80
```

The pointer modifies `a`. The reference modifies `b`.

### Q4. Explain the function's behaviour.

```
void modify(int x, int* p) {
    x = 100;
    *p = 200;
}

int main() {
    int a = 10;
    int b = 20;

    modify(a, &b);

    cout << a << " " << b;
}
```

Complete solution

```
10 200
```

`x` is a separate parameter object, so changing it does not affect `a`. `p` contains the address of `b`, so modifying `*p` changes `b`.

### Q5. Explain the reference trap.

```
int x = 10;
int y = 30;

int &r = x;

r = y;

cout << x << " " << y;
```

Complete solution

```
30 30
```

`r` remains bound to `x`. The assignment copies the value of `y` into `x`.

### Q6. What's wrong with this function?

```
int* create() {
    int value = 50;
    return &value;
}
```

Complete solution

The function returns the address of a local object whose lifetime ends when the function returns. The pointer becomes dangling.

Never return a pointer to a local non-static object.

### Q7. Explain this declaration.

```
int* p1, p2;
```

Complete solution

`p1` is an integer pointer. `p2` is an ordinary integer.

Clearer declarations:

```
int* p1;
int p2;
```

# Part VII: Module Reflection

This is where we bring What → So What → Now What back at the module level.

WHAT DID I LEARN?

You learned how memory stores objects, how addresses identify them, how pointers provide indirect access, how dereferencing works, how to handle null pointers, and how functions interact with original objects through pointers and references.

SO WHAT DOES IT ENABLE?

You can now reason about indirect data access, object modification, pointer safety, and relationships between objects. These ideas are essential building blocks for dynamic data structures.

NOW WHAT CAN I DO?

You can write pointer-based functions, modify existing variables indirectly, swap values, reason about pointer behaviour, and prepare to understand linked lists, trees and dynamic memory.

## Module Mastery Tracker

Module 12 mastery

# 0/11

I can explain memory, variables and addresses.

I can use the address-of operator correctly.

I can declare and initialise pointers.

I understand the difference between ptr and \*ptr.

I can modify an object through a pointer.

I can explain and safely handle nullptr.

I understand dangling pointers and object lifetime.

I can distinguish pass-by-value and pass-by-reference.

I understand reference variables and their limitations.

I can explain unfamiliar pointer-based code.

I can solve pointer and reference problems independently.

Mark a skill complete only when you can demonstrate it without relying on the handbook.

## Final module audit

# Module 12: Introduction to Pointers

Screenshot syllabus topics

Covered

Four integrated concept chunks

Complete

What → So What → Now What

Integrated

English and Hinglish explanations

Included

Programming problems and solutions

Included

Developer's Code Reading Lab

Included

DSA Mastery Lab

Included

Checkpoints and answer keys

Complete

Revision and active recall

Complete

One final thought: Don't rush through this module. The most important milestone is being able to look at `int* ptr = &x;` and immediately understand the relationship between the two variables, the address and the object.

That mental model is going to become one of your most useful tools in C++. 🚀