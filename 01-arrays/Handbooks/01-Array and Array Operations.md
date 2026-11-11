# Major Topic 01: Arrays in C++

## Module 1: Arrays (Part I)



New module handbook

DSA foundation



Welcome to Arrays! 🧠 This is a major milestone in your DSA journey.

Pointers taught us how to work with individual objects through memory addresses. Arrays take us one step further: they allow us to store multiple values of the same type in a contiguous sequence of memory.

And here's the exciting part: this module connects several ideas you've already learned:

- Variables and data types
- Loops and conditional statements
- Functions
- Pointers and memory addresses
- Time and space complexity

We'll use those foundations to understand array traversal, searching, reversing, binary search and pointer arithmetic.

Our learning philosophy remains:

Read like a developer. Reason like an algorithm designer. Explain like a teacher.

# 1. Module overview

[Why Array Index starts with 0 and not 1? | by Dipan Chakraborty | Medium](https://images.openai.com/static-rsc-4/FQ9jNKiAtNQbMeDK74QOYQ64Ae-zAE-7VXB3u0Oo8q1VnZztAvmXoXaRbG5lMaef3Dd_-TEqWoFtmYMwpix4QJ7CK3gc8U32eUzEy6FtLhb1M-XNUAVZTvXv3sXarZ5wpfz9vGBVwOSGlLGIWVSYETYQ3rjTZm7ccIx2mPrTRYo?purpose=inline)

[medium.com](https://medium.com/%40dipan2003.dev/why-array-index-starts-with-0-and-not-1-57e9f285e74b?utm_source=chatgpt.com)

## Syllabus coverage from your Sigma screenshot

| #  | Lecture/topic                              | Handbook section |
| -- | ------------------------------------------ | ---------------- |
| 1  | Basics of Array                            | Chunk 1          |
| 2  | Creating an Array                          | Chunk 1          |
| 3  | Output & Input Array                       | Chunk 1          |
| 4  | Find Largest in Array                      | Chunk 2          |
| 5  | Arrays are passed by Reference             | Chunk 3          |
| 6  | Time & Space Complexity (Reading Material) | Chunk 4          |
| 7  | Linear Search                              | Chunk 5          |
| 8  | Reverse an Array                           | Chunk 6          |
| 9  | Binary Search                              | Chunk 7          |
| 10 | Binary Search Code                         | Chunk 7          |
| 11 | Binary Search (Time Complexity)            | Chunk 7          |
| 12 | Array Pointer                              | Chunk 8          |
| 13 | Pointer Arithmetic 1                       | Chunk 8          |
| 14 | Pointer Arithmetic 2                       | Chunk 8          |
| 15 | Pointer Arithmetic 3                       | Chunk 8          |
| 16 | Pointer Arithmetic 4                       | Chunk 8          |

We'll preserve all the topics visible in your screenshot. Related ideas will be taught together rather than split into tiny sections.

## Learning objectives

By the end of this module, you should be able to:

1. Explain what an array is and how it is represented in memory.
2. Declare, initialise, read and modify arrays.
3. Traverse arrays using loops.
4. Find the largest element in an array.
5. Explain how arrays behave when passed to functions.
6. Analyse the time and auxiliary space complexity of array algorithms.
7. Implement linear search and binary search.
8. Reverse an array using the two-pointer technique.
9. Understand the relationship between arrays and pointers.
10. Perform and reason about pointer arithmetic.

## Our eight concept-learning chunks

01

Array fundamentals

Declaration, creation, indexing, memory layout, input and output.

02

Traversing and analysing arrays

Finding the largest element, iteration and state tracking.

03

Arrays and functions

Passing arrays to functions, modifying elements and understanding array parameters.

04

Time and space complexity

Complexity analysis for array operations and algorithms.

05

Linear search

Sequential searching, algorithm design and complexity.

06

Reversing an array

Two-pointer technique, swapping and in-place algorithms.

07

Binary search

Sorted arrays, search space reduction, implementation and complexity.

08

Arrays and pointer arithmetic

Array-pointer relationship, pointer movement and arithmetic operations.

# Part I: Concept Learning

## Chunk 1: Array Fundamentals



High priority

DSA foundation



### Learning prompt

Imagine you need to store the marks of 100 students. Instead of declaring 100 separate variables, how can you store all the values together? Explain what an array is, why its elements are stored in contiguous memory, how indexing works, and how to declare and initialise arrays in C++. Demonstrate how to take input, print elements and modify them using loops. Also explain array indices, valid bounds and common indexing mistakes.

### Model answer

What is an array?

An array is a collection of elements of the same data type stored in contiguous memory locations.

Let's start with a problem.

Suppose we need to store five students' marks.

Without arrays, we might write:

```
int mark1 = 85;
int mark2 = 90;
int mark3 = 78;
int mark4 = 95;
int mark5 = 88;
```

This works, but it becomes inconvenient when the number of values increases.

Imagine doing this for 100 or 1,000 students!

Arrays solve this problem by allowing us to store multiple values under one variable name.

```
int marks[5] = {85, 90, 78, 95, 88};
```

Now all five integers belong to the same array, and we can access each element using its index.

How are arrays organised in memory?

One of the most important properties of an array is that its elements are stored in contiguous memory locations.

Contiguous means that the elements occupy consecutive positions in memory.

Array: `marks[5]`

85

Index 0

90

Index 1

78

Index 2

95

Index 3

88

Index 4

Each element is next to the previous one in the array's memory layout.

This contiguous arrangement makes it possible to access an element directly using its index.

Array declaration

General syntax:

```
dataType arrayName[size];
```

Example:

```
int numbers[5];
```

This declares an integer array with space for five elements.

Other examples:

```
float prices[10];
char grades[5];
double measurements[20];
```

The size specifies how many elements the array can contain.

Initialising arrays

We can initialise an array during declaration:

```
int numbers[5] = {10, 20, 30, 40, 50};
```

We can also let the compiler determine the size:

```
int numbers[] = {10, 20, 30, 40, 50};
```

The compiler determines that the array contains five elements.

For a partially initialised array:

```
int numbers[5] = {10, 20};
```

The remaining elements are value-initialised to zero:

```
10 20 0 0 0
```

Understanding array indexing

C++ arrays use zero-based indexing.

That means the first element has index `0`, not `1`.

For an array of size `5`:

| Element | Index |
| ------- | ----- |
| First   | 0     |
| Second  | 1     |
| Third   | 2     |
| Fourth  | 3     |
| Fifth   | 4     |

The general relationship is:

\\[ \text{Last valid index} = \text{Array size} - 1 \\]

So, for `int numbers[5]`, the valid indices are `0` through `4`.

Accessing an element:

```
cout << numbers[0];
```

Modifying an element:

```
numbers[2] = 100;
```

This changes the third element.

Taking array input

Suppose we want the user to enter five numbers.

We can use a loop:

```
#include <iostream>
using namespace std;

int main() {
    int arr[5];

    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    return 0;
}
```

Let's read this like a developer:

- `int arr[5]` creates an array with five integer positions.
- `int i = 0` starts the index at the first position.
- `i < 5` ensures that the loop processes indices `0` through `4`.
- `cin >> arr[i]` stores the next input in the current position.
- `i++` moves to the next index.

Printing array elements

```
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

The loop accesses each element and prints it.

Complete input and output program

```
#include <iostream>
using namespace std;

int main() {
    int arr[5];

    cout << "Enter five numbers: ";

    for (int i = 0; i < 5; i++) {
        cin >> arr[i];
    }

    cout << "Array elements: ";

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Example input:

```
10 20 30 40 50
```

Output:

```
Array elements: 10 20 30 40 50
```

Common indexing mistakes

Consider:

```
int arr[5];
```

This is incorrect:

```
arr[5] = 100;
```

Why?

The valid indices are `0, 1, 2, 3, 4`. Index `5` is outside the array.

Accessing an element outside its valid bounds results in undefined behaviour in C++.

Also remember:

```
for (int i = 0; i < 5; i++)
```

is correct, while:

```
for (int i = 0; i <= 5; i++)
```

tries to access one extra position.

### Hinglish explanation

Array ek collection hota hai jismein same data type ke multiple elements store kar sakte hain.

Example:

```
int marks[5] = {85, 90, 78, 95, 88};
```

Ab humein five different variables banane ki zaroorat nahi hai. Ek array mein saare marks store ho gaye.

Array ke elements contiguous memory locations mein store hote hain, matlab ek ke baad ek.

Indexing: C++ mein indexing `0` se start hoti hai.

Agar array ka size `5` hai, toh valid indices `0, 1, 2, 3, 4` honge.

```
marks[0]
```

First element access karega.

```
marks[4]
```

Last element access karega.

Array input aur output ke liye hum loops use karte hain, kyunki humein har element ko individually process karna hota hai.

```
for (int i = 0; i < 5; i++) {
    cin >> marks[i];
}
```

Yeh loop har index par input store karega.

### What → So What → Now What

WHAT?

An array stores multiple elements of the same type in contiguous memory. Each element is accessed using an index starting from zero.

SO WHAT?

Arrays let us represent collections of data under one name. Their contiguous layout and indexed access make them fundamental to efficient data processing.

NOW WHAT?

Practise declaring arrays, taking input, printing elements, modifying values and tracing loop indices. Make sure you can identify valid bounds without hesitation.

### Smart Notes

- An array stores elements of the same data type.
- Elements occupy contiguous memory locations.
- Array indexing starts at `0`.
- Last valid index = `size - 1`.
- Declaration: `int arr[5];`
- Initialisation: `int arr[5] = {1, 2, 3, 4, 5};`
- Access: `arr[i]`.
- Input/output commonly uses loops.
- Accessing an invalid index causes undefined behaviour.

### DSA connection

DSA foundation

Arrays are among the most important foundational data structures. They are used in searching, sorting, dynamic programming, matrices, strings and many other algorithms.

Understanding array indexing and traversal is essential before solving larger DSA problems.

## Chunk 2: Traversing and Analysing Arrays



High priority

Problem-solving foundation



### Learning prompt

Suppose you have an array of numbers and need to find its largest element. Explain how to traverse an array, why a loop is useful, how to maintain a running maximum while processing elements, and how to handle edge cases. Demonstrate the algorithm with a complete C++ program and explain how to reason about its correctness.

### Model answer

What is array traversal?

Traversal means visiting the elements of an array one by one, usually to inspect or process them.

Consider:

```
int arr[5] = {12, 45, 7, 89, 23};
```

We can traverse it using a loop:

```
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

The loop visits every valid index, from `0` to `4`.

Traversal is one of the most frequently used operations in array problems.

Finding the largest element

Suppose the array is:

```
12 45 7 89 23
```

We want to find the largest number.

A natural strategy is to maintain a variable that remembers the largest value encountered so far.

Let's call it `largest`.

Initially, we assume the first element is the largest:

```
int largest = arr[0];
```

Then we examine the remaining elements.

For every element:

- If the current element is greater than `largest`, update `largest`.
- Otherwise, keep the existing value.

Let's trace it:

| Current element | Largest before comparison | Largest after comparison |
| --------------- | ------------------------- | ------------------------ |
| 12              | 12                        | 12                       |
| 45              | 12                        | 45                       |
| 7               | 45                        | 45                       |
| 89              | 45                        | 89                       |
| 23              | 89                        | 89                       |

The final answer is `89`.

Complete C++ program

```
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {12, 45, 7, 89, 23};

    int largest = arr[0];

    for (int i = 1; i < 5; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    cout << "Largest element: " << largest;

    return 0;
}
```

Output:

```
Largest element: 89
```

Why start from index 1?

We already used `arr[0]` to initialise `largest`.

There is no need to compare the first element with itself again.

How do we know the algorithm is correct?

We can reason using an invariant:

After processing the first `i + 1` elements, `largest` contains the maximum among those elements.

- Initially, after processing the first element, `largest = arr[0]`. The invariant holds.
- At each iteration, we compare the next element with `largest`.
- If the new element is larger, we update the maximum.
- Otherwise, the previous maximum remains correct.

After the loop, every element has been processed, so `largest` is the maximum of the entire array.

Important edge cases

1. All elements are negative.
2. All elements are equal.
3. The largest element is at the first position.
4. The largest element is at the last position.
5. The array contains only one element.

Initialising `largest` with `arr[0]` handles negative numbers correctly, unlike initialising it with zero.

For an empty array, this algorithm cannot be used as written because `arr[0]` does not exist. We must handle empty input separately.

### Hinglish explanation

Array traversal ka matlab hai array ke elements ko ek-ek karke visit karna.

Largest element find karne ke liye hum ek variable maintain karte hain:

```
int largest = arr[0];
```

Ab loop mein har element compare karenge.

Agar current element `largest` se bada hai, toh `largest` update kar denge.

Example:

```
12 45 7 89 23
```

- Initially largest = 12
- 45 bada hai, toh largest = 45
- 7 chhota hai, toh largest = 45
- 89 bada hai, toh largest = 89
- 23 chhota hai, toh largest = 89

Final answer `89` hai.

Ek important baat: `largest` ko zero se initialise mat karo, kyunki agar saare elements negative hue toh answer galat aa sakta hai.

### What → So What → Now What

WHAT?

Traversal visits elements one by one. A running maximum tracks the largest value encountered so far.

SO WHAT?

This teaches us a reusable algorithmic pattern: process a sequence while maintaining useful state. The same pattern appears in minimum, sum, counting and many other problems.

NOW WHAT?

Practise finding the minimum, sum and second-largest element. Learn to state what your tracking variable represents before writing the loop.

### Smart Notes

- Traversal means visiting array elements sequentially.
- A loop is commonly used for traversal.
- Initialise the maximum using the first element.
- Compare each remaining element and update when necessary.
- Track the meaning of your variables throughout the loop.
- Finding the maximum takes \\(O(n)\\) time and \\(O(1)\\) auxiliary space.
- Handle empty arrays separately.

### DSA connection

DSA foundation

The running-maximum technique is a basic form of state tracking. It develops the same reasoning used in maximum subarray problems, prefix calculations, frequency counting and many algorithmic patterns.

## Chunk 3: Arrays Passed to Functions



High priority

C++ language foundation



### Learning prompt

You have an array in `main()` and want another function to process or modify it. Explain how arrays are passed to functions in C++, why array parameters behave differently from ordinary integer parameters, how a function can modify the original array elements, and why the array's size usually needs to be passed separately. Demonstrate this with complete programs and clarify the relationship between array parameters and pointers.

### Model answer

What happens when we pass an ordinary variable?

Consider:

```
void change(int x) {
    x = 100;
}

int main() {
    int a = 10;

    change(a);

    cout << a;
}
```

The function receives a separate copy of `a`. Therefore, the output is:

```
10
```

Now consider an array:

```
void change(int arr[]) {
    arr[0] = 100;
}
```

When an array is used as a function parameter in this form, the parameter is adjusted to a pointer to its first element.

It does not receive an independent copy of the entire array.

Example: Modify an array inside a function

```
#include <iostream>
using namespace std;

void changeArray(int arr[], int size) {
    arr[0] = 100;

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}

int main() {
    int numbers[5] = {10, 20, 30, 40, 50};

    changeArray(numbers, 5);

    cout << endl << numbers[0];

    return 0;
}
```

Output:

```
100 20 30 40 50
100
```

Why did the original array change?

Because the function parameter provides access to the original array's elements. It does not create a separate array copy.

Array parameter syntax

Both declarations are valid:

```
void display(int arr[], int size);
```

```
void display(int* arr, int size);
```

For an ordinary array parameter, these declarations are adjusted to the same pointer parameter type.

Why must we pass the size separately?

Consider:

```
void display(int arr[]) {
    cout << sizeof(arr);
}
```

Inside the function, `arr` is a pointer parameter, not an array object.

Therefore, `sizeof(arr)` gives the size of the pointer, not the size of the original array.

This is why we commonly pass the array size separately:

```
void display(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
}
```

Complete example: Find the largest element using a function

```
#include <iostream>
using namespace std;

int findLargest(int arr[], int size) {
    int largest = arr[0];

    for (int i = 1; i < size; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    return largest;
}

int main() {
    int arr[5] = {12, 45, 7, 89, 23};

    cout << findLargest(arr, 5);

    return 0;
}
```

Output:

```
89
```

The function receives access to the array elements and returns the largest value.

A crucial distinction

Passing an array to a function allows the function to modify its elements, but reassigning the local pointer parameter does not change the caller's array variable or pointer.

For example:

```
void test(int* p) {
    int another[3] = {1, 2, 3};
    p = another;
}
```

This only changes the local pointer `p`. It does not replace the original array.

Also, this discussion concerns ordinary built-in arrays passed through array parameters. C++ also has `std::array` and `std::vector`, which have different value and reference semantics.

### Hinglish explanation

Jab hum normal integer function ko pass karte hain, toh usually uski copy pass hoti hai.

Lekin jab hum built-in array ko is tarah function mein pass karte hain:

```
void change(int arr[]) {
    arr[0] = 100;
}
```

toh function ko original array ke elements access karne ka access milta hai.

Isliye function ke andar:

```
arr[0] = 100;
```

karne se original array ka first element change ho jata hai.

Ek important baat: function parameter ke andar array pointer ke form mein behave karta hai. Isliye original array ka size automatically available nahi hota.

Isi wajah se hum size separately pass karte hain:

```
display(arr, 5);
```

### What → So What → Now What

WHAT?

A built-in array parameter is adjusted to a pointer parameter. The function can access and modify the original array elements.

SO WHAT?

Functions can process large collections without copying the entire array. This is important for reusable algorithms and efficient data processing.

NOW WHAT?

Practise writing functions that display arrays, calculate sums, find maximum values and modify elements. Always pass the size when using a built-in array parameter.

### Smart Notes

- Built-in array parameters are adjusted to pointer parameters.
- Array elements can be modified inside the function.
- The original array is not copied as a whole.
- `int arr[]` and `int* arr` are equivalent parameter forms here.
- Array size is not automatically available through the parameter.
- Pass the size separately.
- Reassigning the local pointer does not replace the caller's array.

### DSA connection

DSA foundation

Almost every array algorithm will eventually be implemented as a function: searching, sorting, reversing, calculating sums and finding maximum values.

Understanding array parameters is essential for organising your DSA code into reusable functions.

## Chunk 4: Time and Space Complexity



High priority

Long-term value



### Learning prompt

When an array algorithm processes more elements, how does its execution cost grow? Explain time complexity and auxiliary space complexity, why we analyse growth rather than exact execution time, and how common array operations such as accessing, traversing, searching and reversing relate to complexity. Demonstrate how to analyse loops and nested loops, and distinguish total space from auxiliary space.

### Model answer

What is time complexity?

Time complexity describes how an algorithm's running time grows as the input size increases.

Suppose an array contains \\(n\\) elements.

If we visit every element once, the amount of work grows proportionally to \\(n\\).

This is linear time:

\\[ O(n) \\]

We use Big-O notation to describe an upper bound on growth, ignoring constant factors and lower-order terms.

For example:

\\[ 3n + 5 = O(n) \\]

We focus on how the algorithm scales rather than the exact number of seconds it takes on one computer.

Common complexities

| Complexity       | Name         | Example                        |
| ---------------- | ------------ | ------------------------------ |
| \\(O(1)\\)       | Constant     | Access `arr[3]`                |
| \\(O(\log n)\\)  | Logarithmic  | Binary search                  |
| \\(O(n)\\)       | Linear       | Traverse an array              |
| \\(O(n\log n)\\) | Linearithmic | Efficient comparison sorting   |
| \\(O(n^2)\\)     | Quadratic    | Two nested loops over an array |

Analysing array operations

Consider direct access:

```
int value = arr[3];
```

The array index provides direct access to the element.

Time complexity:

\\[ O(1) \\]

Now consider traversal:

```
for (int i = 0; i < n; i++) {
    cout << arr[i];
}
```

The loop runs \\(n\\) times.

Time complexity:

\\[ O(n) \\]

Now consider nested loops:

```
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        cout << arr[i] << " " << arr[j] << endl;
    }
}
```

The outer loop runs \\(n\\) times. For each outer iteration, the inner loop also runs \\(n\\) times.

Total iterations:

\\[ n \times n = n^2 \\]

Time complexity:

\\[ O(n^2) \\]

What is space complexity?

Space complexity describes how memory requirements grow with input size.

For algorithm analysis, we often focus on auxiliary space, which is the extra memory used by the algorithm beyond the input.

Example:

```
int findLargest(int arr[], int n) {
    int largest = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    return largest;
}
```

The function uses only one extra integer variable, regardless of array size.

Auxiliary space:

\\[ O(1) \\]

Time and space complexity of common operations

| Operation        | Time complexity       | Auxiliary space      |
| ---------------- | --------------------- | -------------------- |
| Access by index  | \\(O(1)\\)            | \\(O(1)\\)           |
| Traverse array   | \\(O(n)\\)            | \\(O(1)\\)           |
| Find maximum     | \\(O(n)\\)            | \\(O(1)\\)           |
| Linear search    | \\(O(n)\\) worst case | \\(O(1)\\)           |
| Reverse in place | \\(O(n)\\)            | \\(O(1)\\)           |
| Binary search    | \\(O(\log n)\\)       | \\(O(1)\\) iterative |

These complexities describe the algorithms, not the total memory occupied by the input array.

### Hinglish explanation

Time complexity batati hai ki input size badhne par algorithm ka running time kaise grow karta hai.

Agar array mein `n` elements hain aur hum har element ko ek baar visit karte hain, toh time complexity `O(n)` hogi.

Agar direct index se element access karte hain:

```
arr[3]
```

toh complexity `O(1)` hoti hai.

Agar nested loops mein har element ke liye poora array traverse karte hain, toh complexity `O(n²)` ho sakti hai.

Space complexity batati hai ki algorithm ko extra memory kitni chahiye.

Agar hum sirf ek `largest` variable use karte hain, toh extra space `O(1)` hai, chahe array mein 10 elements ho ya 10 lakh.

### What → So What → Now What

WHAT?

Time complexity describes how running time grows with input size. Auxiliary space describes the extra memory an algorithm uses.

SO WHAT?

Two programs may produce the same answer but have very different scalability. Complexity analysis helps us choose algorithms that remain efficient as input grows.

NOW WHAT?

Whenever you write a loop, count its iterations. Whenever you introduce extra variables or data structures, ask how their memory grows with input size.

### Smart Notes

- Time complexity describes growth in running time.
- Space complexity describes memory requirements.
- Auxiliary space is extra memory beyond the input.
- Direct array access: \\(O(1)\\).
- Single traversal: \\(O(n)\\).
- Two full nested loops: commonly \\(O(n^2)\\).
- Binary search: \\(O(\log n)\\).
- In-place array reversal: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.
- Big-O describes growth, not exact execution seconds.

### DSA connection

Long-term value

Complexity analysis is a universal DSA skill. As you encounter larger problems, you will need to decide whether an algorithm can handle 1,000, 100,000 or 10 million elements.

## Chunk 5: Linear Search



DSA foundation

High priority



### Learning prompt

Suppose you have an unsorted array and need to find a particular value. Explain how linear search works, how it examines elements sequentially, how to return the location of a target, and what happens when the target is absent. Demonstrate the algorithm in C++, trace its execution and analyse its best, worst and average-case time complexity.

### Model answer

What is linear search?

Linear search is an algorithm that searches for a target element by checking array elements one by one.

It starts at the first element and continues until:

- The target is found, or
- The entire array has been checked.

It does not require the array to be sorted.

Consider:

```
Array:  12  45  7  89  23
Target: 89
```

We inspect:

| Index | Element | Comparison |
| ----- | ------- | ---------- |
| 0     | 12      | Not equal  |
| 1     | 45      | Not equal  |
| 2     | 7       | Not equal  |
| 3     | 89      | Found      |

The target is found at index `3`.

Algorithm

1. Start from index `0`.
2. Compare the current element with the target.
3. If they are equal, return the index.
4. Otherwise, move to the next element.
5. If the loop finishes, return `-1` to indicate absence.

Complete C++ program

```
#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}

int main() {
    int arr[5] = {12, 45, 7, 89, 23};

    int target = 89;

    int result = linearSearch(arr, 5, target);

    if (result != -1) {
        cout << "Found at index: " << result;
    }
    else {
        cout << "Element not found";
    }

    return 0;
}
```

Output:

```
Found at index: 3
```

Why return `-1`?

Array indices start from zero. Therefore, `-1` cannot be a valid index of an ordinary array.

We use it as a sentinel value to indicate that the target was not found.

Complexity analysis

Best case: The target is at index `0`.

Only one comparison is needed:

\\[ O(1) \\]

Worst case: The target is at the last position or absent.

We may need to examine all \\(n\\) elements:

\\[ O(n) \\]

Average case: Under a common model where the target is equally likely to occur at any position, the expected number of comparisons is proportional to \\(n\\):

\\[ O(n) \\]

Auxiliary space:

\\[ O(1) \\]

### Hinglish explanation

Linear search mein hum target element ko array ke har element ke saath ek-ek karke compare karte hain.

Agar match mil gaya, toh uska index return kar dete hain.

Agar poora array check karne ke baad bhi match nahi mila, toh `-1` return karte hain.

Iski sabse badi advantage yeh hai ki array sorted hona zaroori nahi hai.

Lekin agar array bahut bada ho, toh worst case mein humein har element check karna padega.

### What → So What → Now What

WHAT?

Linear search examines array elements sequentially until it finds the target or reaches the end.

SO WHAT?

It works even when data is unsorted and teaches the basic pattern of searching a collection. Its limitation is that its worst-case work grows linearly.

NOW WHAT?

Implement linear search, return indices correctly, handle missing targets, and compare the number of comparisons in best and worst cases.

### Smart Notes

- Linear search checks elements sequentially.
- Works on sorted and unsorted arrays.
- Returns the target index when found.
- Returns `-1` when absent.
- Best-case time: \\(O(1)\\).
- Worst-case time: \\(O(n)\\).
- Average-case time: \\(O(n)\\).
- Auxiliary space: \\(O(1)\\).

### DSA connection

DSA foundation

Linear search teaches sequential processing and early termination. It is also a useful baseline against which faster searching algorithms can be compared.

## Chunk 6: Reversing an Array



High priority

DSA foundation



### Learning prompt

Suppose you have an array and want its elements in reverse order. Explain how reversing differs from merely printing elements backwards, how two pointers can work from opposite ends of an array, why swapping is necessary, and how the algorithm terminates. Demonstrate an in-place reversal in C++ and analyse its time and auxiliary space complexity.

### Model answer

What does reversing an array mean?

Reversing an array means changing the order of its elements so that the last element becomes first, the second-last becomes second, and so on.

Original:

```
10 20 30 40 50
```

After reversal:

```
50 40 30 20 10
```

There are two different operations to understand:

- Printing an array backwards only changes the order in which elements are displayed.
- Reversing an array modifies the actual order of elements in memory.

We'll focus on modifying the original array.

The two-pointer technique

We can reverse an array efficiently by using two indices:

- `start` begins at index `0`.
- `end` begins at index `n - 1`.

We swap the elements at these positions, then move both indices towards the centre.

Example: Reversing `[10, 20, 30, 40, 50]`

Initial state

10

0

20

1

30

2

40

3

50

4

start = 0

end = 4

After first swap

50

0

20

1

30

2

40

3

10

4

Move start forward and end backward.

After second swap

50

0

40

1

30

2

20

3

10

4

The pointers meet at the middle. Reversal is complete.

The algorithm

1. Initialise `start = 0`.
2. Initialise `end = n - 1`.
3. Continue while `start < end`.
4. Swap `arr[start]` and `arr[end]`.
5. Increment `start`.
6. Decrement `end`.
7. Stop when the two indices meet or cross.

Complete C++ program

```
#include <iostream>
using namespace std;

void reverseArray(int arr[], int size) {
    int start = 0;
    int end = size - 1;

    while (start < end) {
        int temp = arr[start];

        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    reverseArray(arr, 5);

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Output:

```
50 40 30 20 10
```

Why use `start < end`?

When `start` reaches `end`, the pointers have met at the middle.

There is no need to swap an element with itself.

If they cross, all required swaps have already happened.

Complexity

Each swap handles two elements. Approximately half the array's elements are involved in swaps.

The total number of swaps is approximately \\(n/2\\), which still gives:

\\[ O(n) \\]

The algorithm uses only three extra variables: `start`, `end` and `temp`.

Auxiliary space:

\\[ O(1) \\]

This is called an in-place reversal because we modify the original array without creating another array.

### Hinglish explanation

Array reverse karne ka matlab hai original array ke elements ka order change karna.

Hum do indices use karenge:

- `start` first element par.
- `end` last element par.

Dono positions ke elements swap karenge.

Phir `start++` aur `end--` karenge.

Jab dono indices meet ya cross kar jaate hain, reversal complete ho jata hai.

Is approach ko two-pointer technique kehte hain.

Iska time complexity `O(n)` hai aur extra space `O(1)` hai.

### What → So What → Now What

WHAT?

Array reversal can be performed by swapping elements from opposite ends and moving two indices towards the centre.

SO WHAT?

This introduces the two-pointer technique and in-place modification. These patterns are widely useful in DSA, including palindrome checks, pair problems and partitioning.

NOW WHAT?

Practise reversing arrays of odd and even sizes, trace every swap, and learn to identify when the two indices should stop.

### Smart Notes

- Reversal changes the original order of array elements.
- `start = 0`.
- `end = size - 1`.
- Swap the two elements, then move both indices inward.
- Stop when `start >= end`.
- Time complexity: \\(O(n)\\).
- Auxiliary space: \\(O(1)\\).
- This is an in-place algorithm.
- Two-pointer technique is reusable across many DSA problems.

### DSA connection

DSA foundation

The two-pointer technique is one of the most useful DSA patterns. It will reappear in palindrome checking, pair-sum problems, sorted-array problems and other algorithms.

## Chunk 7: Binary Search



High priority

DSA foundation



### Learning prompt

Suppose you need to find a target element in a sorted array. Explain how binary search repeatedly divides the search space into halves, how the middle index is calculated, and how comparisons determine whether to search the left or right half. Demonstrate the algorithm using a complete iterative C++ implementation. Explain its requirement for sorted input, boundary conditions, correctness, and best, worst and average-case time complexity.

### Model answer

What is binary search?

Binary search is an efficient searching algorithm that repeatedly divides a sorted search space into two halves.

Unlike linear search, it does not need to examine every element.

However, there is one critical requirement:

Required condition

The array must be sorted for ordinary binary search to work correctly.

Consider this sorted array:

```
10 20 30 40 50 60 70 80 90
```

Suppose our target is:

```
70
```

Instead of starting from the first element, binary search examines the middle element.

How binary search works

We maintain two boundaries:

- `start`: beginning of the current search range.
- `end`: end of the current search range.

The middle index is:

\\[ mid = start + \frac{end-start}{2} \\]

Using integer division in C++.

Then compare the middle element with the target.

Three possibilities:

1. If `arr[mid] == target`, the element is found.
2. If `arr[mid] < target`, search the right half.
3. If `arr[mid] > target`, search the left half.

Let's trace the example.

Search for 70

Initial search range: indices 0 to 8

10

0

20

1

30

2

40

3

50

4

60

5

70

6

80

7

90

8

mid = 4, value = 50. Since 70 is greater, discard the left half and middle.

Remaining range: indices 5 to 8

10

0

20

1

30

2

40

3

50

4

60

5

70

6

80

7

90

8

mid = 6, value = 70. Target found!

Found at index 6

Complete iterative C++ implementation

```
#include <iostream>
using namespace std;

int binarySearch(int arr[], int size, int target) {
    int start = 0;
    int end = size - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }

    return -1;
}

int main() {
    int arr[9] = {10, 20, 30, 40, 50, 60, 70, 80, 90};

    int target = 70;

    int result = binarySearch(arr, 9, target);

    if (result != -1) {
        cout << "Found at index: " << result;
    }
    else {
        cout << "Element not found";
    }

    return 0;
}
```

Output:

```
Found at index: 6
```

Why calculate `mid` this way?

You may also see:

```
int mid = (start + end) / 2;
```

This often works, but when `start` and `end` are very large, `start + end` can overflow an integer.

The expression:

```
start + (end - start) / 2
```

avoids that particular overflow risk when the indices are valid nonnegative integer positions.

Why `start <= end`?

We continue while the search range contains at least one element.

If `start == end`, one element remains and must still be checked.

When `start > end`, the range is empty and the target was not found.

Why use `mid + 1` and `mid - 1`?

If the middle element is not the target, we already know it cannot be the answer.

So we exclude it from the next search range.

Why does binary search work?

The array is sorted.

- If the middle element is smaller than the target, all elements to its left are also smaller. Therefore, the target cannot be there.
- If the middle element is larger than the target, all elements to its right are also larger. Therefore, the target cannot be there.

Each comparison safely eliminates half of the remaining search space.

Complexity analysis

Best case: The target is found at the first middle position.

\\[ O(1) \\]

Worst case: The search range keeps getting divided until it becomes empty or one element remains.

\\[ O(\log n) \\]

Average-case time for ordinary binary search is also:

\\[ O(\log n) \\]

Iterative auxiliary space:

\\[ O(1) \\]

Important: Binary search and duplicate elements

If an array contains duplicate values, this implementation returns an occurrence of the target, but does not guarantee the first or last occurrence.

Finding the first or last occurrence requires a modified binary search.

### Hinglish explanation

Binary search ek searching algorithm hai jo sorted array mein search space ko baar-baar half karta hai.

Sabse important condition: Array sorted hona chahiye.

Hum teen variables use karte hain:

- `start`: search range ka beginning.
- `end`: search range ka ending.
- `mid`: middle index.

Agar:

```
arr[mid] == target
```

toh element mil gaya.

Agar:

```
arr[mid] < target
```

toh right side search karenge.

Agar:

```
arr[mid] > target
```

toh left side search karenge.

Har step mein search space approximately half ho jata hai. Isi wajah se binary search ki time complexity `O(log n)` hoti hai.

Linear search ke comparison mein yeh large sorted arrays ke liye kaafi efficient hota hai.

### What → So What → Now What

WHAT?

Binary search repeatedly halves a sorted search range by comparing the target with its middle element.

SO WHAT?

Instead of examining up to \\(n\\) elements, binary search can solve the problem in \\(O(\log n)\\) time. It demonstrates the power of reducing a search space systematically.

NOW WHAT?

Practise tracing `start`, `end` and `mid` by hand. Learn to justify which half can be eliminated, and test targets at the beginning, middle, end and outside the array.

### Smart Notes

- Binary search requires sorted input.
- Initialise `start = 0` and `end = size - 1`.
- Calculate `mid = start + (end - start) / 2`.
- If equal, return the index.
- If middle value is smaller, move `start = mid + 1`.
- If middle value is larger, move `end = mid - 1`.
- Continue while `start <= end`.
- Return `-1` when absent.
- Best-case time: \\(O(1)\\).
- Average and worst-case time: \\(O(\log n)\\).
- Iterative auxiliary space: \\(O(1)\\).

### DSA connection

DSA foundation

Binary search introduces the broader idea of search-space reduction.

This reasoning later appears in binary search on answers, finding boundaries, optimisation problems and many advanced algorithms.

## Chunk 8: Arrays, Pointers and Pointer Arithmetic



High priority

Long-term value



### Learning prompt

You have learned that arrays store elements in contiguous memory and pointers store addresses. Explain how an array name behaves when used in expressions, how it relates to a pointer to the first element, and how pointer arithmetic moves through an array. Cover pointer increment, decrement, addition, subtraction, accessing elements through pointer arithmetic, and the relationship between `arr[i]` and `*(arr + i)`. Also explain the boundaries of valid pointer arithmetic and demonstrate the concepts using C++ programs.

### Model answer

What is the relationship between arrays and pointers?

Consider:

```
int arr[5] = {10, 20, 30, 40, 50};
```

The array elements are stored in contiguous memory.

When an array name is used in most expressions, it converts (decays) into a pointer to its first element.

Therefore:

```
arr
```

in an ordinary expression behaves like:

```
&arr[0]
```

This is why we can write:

```
int* ptr = arr;
```

The pointer now points to the first element of the array.

Array and pointer relationship

Array index

Element value

10

0

20

1

30

2

40

3

50

4

`ptr = arr`

Points to `arr[0]`

Pointer arithmetic moves between elements of the same array.

An important distinction: an array is not itself a pointer. It is an array object. Array-to-pointer conversion happens in most expressions, but there are exceptions, such as `sizeof(arr)` and `&arr`.

Pointer arithmetic

Suppose:

```
int arr[5] = {10, 20, 30, 40, 50};

int* ptr = arr;
```

Initially, `ptr` points to `arr[0]`.

We can move it to the next element:

```
ptr++;
```

Now it points to `arr[1]`.

If we decrement it:

```
ptr--;
```

it moves back to `arr[0]`.

Why does incrementing a pointer move by an entire element instead of just one byte?

Because pointer arithmetic is scaled according to the pointer's type.

If `ptr` is an `int*`, incrementing it moves to the next integer element.

If `ptr` is a `char*`, incrementing it moves to the next character element.

The compiler handles the byte-distance calculation.

For example, if an `int` occupies four bytes on a particular system, incrementing an `int*` advances its address by four bytes. The actual size depends on the implementation.

Pointer arithmetic operation 1: Increment and decrement

```
int arr[3] = {10, 20, 30};

int* ptr = arr;

cout << *ptr << endl;

ptr++;

cout << *ptr << endl;

ptr--;

cout << *ptr << endl;
```

Output:

```
10
20
10
```

The pointer moves between elements. The values themselves are not changed.

Pointer arithmetic operation 2: Addition and subtraction of an integer

We can move a pointer forward or backward by a number of elements.

```
int arr[5] = {10, 20, 30, 40, 50};

int* ptr = arr;

cout << *(ptr + 2) << endl;
cout << *(ptr + 4) << endl;
```

Output:

```
30
50
```

`ptr + 2` points to the third element. Dereferencing it accesses `30`.

Similarly:

```
ptr = ptr + 3;
```

moves the pointer to the fourth element.

Pointer arithmetic operation 3: Subtracting two pointers

When two pointers point into the same array (or one past its end), we can subtract them.

The result is the number of elements between their positions, not the number of bytes.

```
int arr[5] = {10, 20, 30, 40, 50};

int* p1 = &arr[1];
int* p2 = &arr[4];

cout << p2 - p1;
```

Output:

```
3
```

The pointers refer to indices `1` and `4`. There are three element positions between them.

The result type is `std::ptrdiff_t`, a signed integer type.

Pointer arithmetic operation 4: Accessing array elements through pointers

There is a useful relationship:

\\[ arr[i] = \*(arr+i) \\]

This means that array indexing can be expressed through pointer arithmetic and dereferencing.

For example:

```
int arr[5] = {10, 20, 30, 40, 50};

cout << arr[2] << endl;
cout << *(arr + 2) << endl;
```

Both print:

```
30
30
```

Why?

- `arr + 2` points to the third element.
- `*(arr + 2)` accesses the third element.
- Therefore, it is equivalent to `arr[2]`.

This relationship is particularly important because it reveals how array indexing and pointer arithmetic are connected.

Complete demonstration

```
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    int* ptr = arr;

    for (int i = 0; i < 5; i++) {
        cout << *(ptr + i) << " ";
    }

    return 0;
}
```

Output:

```
10 20 30 40 50
```

The pointer stays at the first element. We calculate the address of each subsequent element using `ptr + i`, then dereference it.

Important pointer arithmetic safety rules

Pointer arithmetic is not unrestricted.

- Moving within the same array is valid.
- A pointer may point one position past the final element, but that position must not be dereferenced.
- Moving before the beginning or beyond the one-past-the-end position is undefined behaviour.
- Subtracting pointers is valid when they refer into the same array, including its one-past position.
- Arbitrary addition of two pointers is not supported.

For example:

```
int arr[3] = {10, 20, 30};

int* ptr = arr;

ptr = ptr + 3;  // One past the last element: valid to form

// cout << *ptr;  // Invalid: dereferencing it is undefined behaviour
```

Another important distinction: array name versus pointer variable

Consider:

```
int arr[3] = {10, 20, 30};
int* ptr = arr;
```

We can reassign the pointer:

```
ptr = &arr[1];
```

But we cannot reassign the array name:

```
arr = &arr[1];  // Invalid
```

The array is an actual array object, not a modifiable pointer variable.

### Hinglish explanation

Array aur pointer ka relationship bahut important hai.

```
int arr[5] = {10, 20, 30, 40, 50};

int* ptr = arr;
```

Most expressions mein array name `arr` first element ke address mein convert ho jata hai.

Isliye `ptr` first element ko point karta hai.

Ab pointer arithmetic se hum next elements par move kar sakte hain.

```
ptr++;
```

Agar `ptr` ek integer pointer hai, toh yeh next integer element par move karega.

Yeh sirf ek byte aage nahi jaata. Compiler pointer ke data type ke according correct distance calculate karta hai.

Aur:

```
*(ptr + 2)
```

ka matlab hai pointer se do elements aage jao aur wahan ki value access karo.

Ek important relationship:

```
arr[i] == *(arr + i)
```

Dono same element access karte hain.

Lekin pointer arithmetic carefully use karna hai. Array ke end se aage invalid memory access nahi kar sakte. One-past-the-end pointer form kar sakte hain, lekin usko dereference nahi kar sakte.

### What → So What → Now What

WHAT?

An array name converts to a pointer to its first element in most expressions. Pointer arithmetic moves in units of the pointed-to type, and dereferencing accesses the resulting element.

SO WHAT?

This explains why array indexing and pointer access are connected. It also gives us the foundation for traversing memory-based data structures and understanding low-level C++ behaviour.

NOW WHAT?

Practise `ptr++`, `ptr + n`, pointer subtraction and `*(arr + i)`. Always track which array element a pointer refers to, and respect the array's boundaries.

### Smart Notes

- Array names convert to pointers to their first element in most expressions.
- An array is not itself a pointer.
- `int* ptr = arr` points to the first element.
- `ptr++` moves to the next element.
- Pointer movement is scaled by the pointed-to type.
- `ptr + n` moves forward by `n` elements.
- `ptr2 - ptr1` gives the element distance when both belong to the same array.
- `arr[i]` is equivalent to `*(arr + i)`.
- One-past-the-end pointers may be formed but not dereferenced.
- Array names cannot be reassigned.

### DSA connection

Long-term value

Pointer arithmetic helps explain how arrays are traversed internally and prepares you for dynamic memory, iterators, linked structures and low-level memory operations.

# Part II: Programming Problems

The concept chunks have established the foundations. Now we'll use them to build programming ability.

The progression is:

1. Beginner: fully worked examples.
2. Intermediate: guided problems with complete solutions.
3. Advanced: independent-style problems with model solutions.
4. Challenge: design, correctness and complexity reasoning.

Every problem has its complete solution.

## Beginner: Fully worked problems

### Problem 1: Create an array and print its elements

Task: Create an integer array of five elements and print all its elements.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Output:

```
10 20 30 40 50
```

Explanation: The loop visits indices `0` through `4` and prints each element.

### Problem 2: Find the sum of array elements

Task: Calculate the sum of all elements in an array.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    int sum = 0;

    for (int i = 0; i < 5; i++) {
        sum += arr[i];
    }

    cout << sum;

    return 0;
}
```

Output:

```
150
```

Explanation: `sum` accumulates the value of every element.

### Problem 3: Find the largest element

Task: Find the maximum value in an array.

Solution

```
#include <iostream>
using namespace std;

int main() {
    int arr[5] = {12, 45, 7, 89, 23};

    int largest = arr[0];

    for (int i = 1; i < 5; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }

    cout << largest;

    return 0;
}
```

Output:

```
89
```

Explanation: Maintain the largest value encountered so far and update it whenever a larger element appears.

### Problem 4: Search for an element using linear search

Task: Find the index of a target value.

Solution

```
#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}

int main() {
    int arr[5] = {12, 45, 7, 89, 23};

    cout << linearSearch(arr, 5, 89);

    return 0;
}
```

Output:

```
3
```

Explanation: The function checks elements sequentially and returns the index of the first matching element.

## Intermediate: Guided problems with complete solutions

### Problem 5: Reverse an array using two pointers

Task: Reverse an array in place without creating another array.

Guided reasoning:

- Use two indices, one at each end.
- Swap the corresponding elements.
- Move both indices towards the centre.
- Stop when they meet or cross.

Complete solution

```
#include <iostream>
using namespace std;

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

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    reverseArray(arr, 5);

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Output:

```
5 4 3 2 1
```

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 6: Find the minimum element using a function

Task: Write a function that receives an array and returns its smallest element.

Guided reasoning:

- Initialise `smallest` with the first element.
- Traverse the remaining elements.
- Update whenever a smaller element is found.
- Return the result.

Complete solution

```
#include <iostream>
using namespace std;

int findMinimum(int arr[], int n) {
    int smallest = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] < smallest) {
            smallest = arr[i];
        }
    }

    return smallest;
}

int main() {
    int arr[5] = {30, 12, 45, 7, 23};

    cout << findMinimum(arr, 5);

    return 0;
}
```

Output:

```
7
```

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 7: Count occurrences of a target

Task: Count how many times a target value appears in an array.

Complete solution

```
#include <iostream>
using namespace std;

int countOccurrences(int arr[], int n, int target) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            count++;
        }
    }

    return count;
}

int main() {
    int arr[7] = {2, 5, 2, 8, 2, 4, 5};

    cout << countOccurrences(arr, 7, 2);

    return 0;
}
```

Output:

```
3
```

Explanation: Unlike ordinary linear search, we don't stop at the first match. We examine the entire array because we need the total count.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 8: Implement binary search

Task: Find the index of a target in a sorted array.

Guided reasoning:

- Initialise `start` and `end`.
- Calculate the middle index.
- Compare the middle value with the target.
- Eliminate the half that cannot contain the target.
- Stop when found or when the search range becomes empty.

Complete solution

```
#include <iostream>
using namespace std;

int binarySearch(int arr[], int n, int target) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            return mid;
        }
        else if (arr[mid] < target) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }

    return -1;
}

int main() {
    int arr[7] = {10, 20, 30, 40, 50, 60, 70};

    cout << binarySearch(arr, 7, 50);

    return 0;
}
```

Output:

```
4
```

Complexity: \\(O(\log n)\\) time and \\(O(1)\\) auxiliary space.

## Advanced: Independent-style problems with complete solutions

### Problem 9: Find the second-largest distinct element

Task: Find the second-largest distinct value in an array. If no such value exists, return `-1`.

Complete solution

```
#include <iostream>
#include <climits>
using namespace std;

int secondLargest(int arr[], int n) {
    int largest = INT_MIN;
    int second = INT_MIN;

    for (int i = 0; i < n; i++) {
        if (arr[i] > largest) {
            second = largest;
            largest = arr[i];
        }
        else if (arr[i] > second && arr[i] < largest) {
            second = arr[i];
        }
    }

    if (second == INT_MIN) {
        return -1;
    }

    return second;
}

int main() {
    int arr[6] = {10, 40, 20, 40, 30, 15};

    cout << secondLargest(arr, 6);

    return 0;
}
```

Output:

```
30
```

Explanation: We maintain the largest and second-largest distinct values. When a new maximum appears, the old maximum becomes the second largest.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

Note: This version uses `-1` as a sentinel, so it is suitable when `-1` cannot be a legitimate answer. A more general function should return a status or optional result.

### Problem 10: Move all zeroes to the end

Task: Move all zeroes to the end while preserving the relative order of non-zero elements.

Example:

```
Input:  0 1 0 3 12
Output: 1 3 12 0 0
```

Complete solution

```
#include <iostream>
using namespace std;

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

int main() {
    int arr[5] = {0, 1, 0, 3, 12};

    moveZeroes(arr, 5);

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Output:

```
1 3 12 0 0
```

Explanation: The first loop copies non-zero values towards the beginning. The second loop fills the remaining positions with zeroes.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 11: Find the first and last occurrence using binary search

Task: Given a sorted array that may contain duplicates, return the first and last index of a target.

Complete solution

```
#include <iostream>
using namespace std;

int firstOccurrence(int arr[], int n, int target) {
    int start = 0;
    int end = n - 1;
    int answer = -1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            answer = mid;
            end = mid - 1;
        }
        else if (arr[mid] < target) {
            start = mid + 1;
        }
        else {
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
        }
        else if (arr[mid] < target) {
            start = mid + 1;
        }
        else {
            end = mid - 1;
        }
    }

    return answer;
}

int main() {
    int arr[8] = {1, 2, 2, 2, 3, 4, 4, 5};

    cout << firstOccurrence(arr, 8, 2) << endl;
    cout << lastOccurrence(arr, 8, 2) << endl;

    return 0;
}
```

Output:

```
1
3
```

Explanation: When a match is found, we save its index but continue searching for an earlier or later occurrence.

Complexity: Each search takes \\(O(\log n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 12: Search for a target using pointer arithmetic

Task: Write a function that searches an array using pointer arithmetic instead of `arr[i]`.

Complete solution

```
#include <iostream>
using namespace std;

int pointerSearch(int* ptr, int n, int target) {
    for (int i = 0; i < n; i++) {
        if (*(ptr + i) == target) {
            return i;
        }
    }

    return -1;
}

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    cout << pointerSearch(arr, 5, 40);

    return 0;
}
```

Output:

```
3
```

Explanation: `*(ptr + i)` accesses the same element as `arr[i]`.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

## Challenge: Design and reasoning

### Problem 13: Find whether an array is sorted

Task: Write a function that returns `true` if an array is sorted in non-decreasing order, and `false` otherwise.

Complete solution

```
#include <iostream>
using namespace std;

bool isSorted(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }

    return true;
}

int main() {
    int arr[5] = {10, 20, 20, 40, 50};

    cout << isSorted(arr, 5);

    return 0;
}
```

Output:

```
1
```

Explanation: We compare every element with its predecessor. If any element is smaller than the previous one, the array is not sorted in non-decreasing order.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

### Problem 14: Understand the difference between printing and reversing

Task: Write two functions:

1. One prints an array in reverse order without changing it.
2. The other actually reverses the array.

Complete solution

```
#include <iostream>
using namespace std;

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

int main() {
    int arr[5] = {1, 2, 3, 4, 5};

    printReverse(arr, 5);

    reverseArray(arr, 5);

    for (int i = 0; i < 5; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
```

Output:

```
5 4 3 2 1
5 4 3 2 1
```

Explanation: The first function only changes the order of printing. The second modifies the original array.

# Part III: Developer's Code Reading Lab

Long-term value

Arrays are an excellent opportunity to develop code-reading fluency. We'll focus on understanding the programmer's intention, the role of each variable, how data moves and why the algorithm works.

## Reading challenge 1: Understand array indexing

```
int arr[5] = {10, 20, 30, 40, 50};

for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

Developer's narration

Create an integer array containing five values. Initialise an index variable `i` to zero. Continue while `i` is less than five, accessing the current array element and printing it. Increment the index after each iteration.

Output:

```
10 20 30 40 50
```

Reasoning: `i` represents the current array index. The loop visits each valid index exactly once.

## Reading challenge 2: Understand the running maximum

```
int arr[5] = {8, 15, 3, 25, 12};

int largest = arr[0];

for (int i = 1; i < 5; i++) {
    if (arr[i] > largest) {
        largest = arr[i];
    }
}
```

Developer's narration

Initialise `largest` with the first element. Traverse the remaining elements. Whenever the current element is greater than the stored maximum, update `largest`.

Final value:

```
25
```

Reasoning: The variable `largest` maintains the maximum among all elements processed so far.

## Reading challenge 3: Understand early termination in linear search

```
int search(int arr[], int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) {
            return i;
        }
    }

    return -1;
}
```

Developer's narration

The function scans the array from the beginning. At each index, it compares the current value with the target. If they match, the function immediately returns the current index. If the loop finishes without finding a match, it returns `-1`.

Reasoning: The `return` statement terminates the function, so no unnecessary comparisons happen after a match.

## Reading challenge 4: Understand the two-pointer reversal

```
int start = 0;
int end = n - 1;

while (start < end) {
    int temp = arr[start];

    arr[start] = arr[end];
    arr[end] = temp;

    start++;
    end--;
}
```

Developer's narration

Create two indices, one at the beginning and another at the end of the array. While they have not met, swap the values at their positions. Move the first index forward and the second index backward. Continue until all opposite pairs have been exchanged.

Reasoning: Each iteration places two elements in their final reversed positions.

## Reading challenge 5: Understand binary search

```
while (start <= end) {
    int mid = start + (end - start) / 2;

    if (arr[mid] == target) {
        return mid;
    }
    else if (arr[mid] < target) {
        start = mid + 1;
    }
    else {
        end = mid - 1;
    }
}
```

Developer's narration

As long as the search range contains elements, calculate its middle index. If the middle value matches the target, return the index. If it is smaller than the target, discard the left half and middle. Otherwise, discard the right half and middle.

Reasoning: The array's sorted order allows us to eliminate half of the remaining search range after each comparison.

## Reading challenge 6: Understand pointer-based array access

```
int arr[5] = {10, 20, 30, 40, 50};

int* ptr = arr;

for (int i = 0; i < 5; i++) {
    cout << *(ptr + i) << " ";
}
```

Developer's narration

Create an array and a pointer to its first element. The loop calculates the address of each subsequent element by adding the current index to the pointer. Dereferencing that address retrieves and prints the corresponding value.

Output:

```
10 20 30 40 50
```

Reasoning: `*(ptr + i)` is equivalent to `arr[i]` for valid indices.

### Code-reading mastery checklist

- I can identify the responsibility of each array variable.
- I can mentally trace loop indices.
- I can explain why a maximum or minimum is updated.
- I can follow early returns in searching algorithms.
- I can trace both pointers in reversal.
- I can explain how binary search eliminates a search range.
- I can mentally follow pointer arithmetic.
- I can explain the intention of unfamiliar array code in natural English.

# Part IV: DSA Mastery Lab

Algorithmic reasoning

This section focuses on transferable problem-solving skills: state tracking, invariants, search-space reduction, edge cases and complexity.

## Guided challenge 1: Find the second-smallest distinct element

Problem: Find the second-smallest distinct value in an array.

Complete solution

```
#include <iostream>
#include <climits>
using namespace std;

int secondSmallest(int arr[], int n) {
    int smallest = INT_MAX;
    int second = INT_MAX;

    for (int i = 0; i < n; i++) {
        if (arr[i] < smallest) {
            second = smallest;
            smallest = arr[i];
        }
        else if (arr[i] > smallest && arr[i] < second) {
            second = arr[i];
        }
    }

    if (second == INT_MAX) {
        return -1;
    }

    return second;
}

int main() {
    int arr[6] = {20, 10, 30, 10, 40, 15};

    cout << secondSmallest(arr, 6);

    return 0;
}
```

Output:

```
15
```

Reasoning: Maintain the smallest and second-smallest distinct values while traversing the array.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

As with the earlier sentinel example, `-1` is an assumed failure value. For completely general integer inputs, use an explicit success indicator or optional result.

## Guided challenge 2: Check whether an array is a palindrome

Problem: An array is a palindrome if it reads the same from left to right and right to left. Check whether an array is a palindrome without creating another array.

Complete solution

```
#include <iostream>
using namespace std;

bool isPalindrome(int arr[], int n) {
    int start = 0;
    int end = n - 1;

    while (start < end) {
        if (arr[start] != arr[end]) {
            return false;
        }

        start++;
        end--;
    }

    return true;
}

int main() {
    int arr[5] = {1, 2, 3, 2, 1};

    cout << isPalindrome(arr, 5);

    return 0;
}
```

Output:

```
1
```

Reasoning: Compare opposite elements. If any pair differs, the array cannot be a palindrome.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

## Independent challenge 3: Find a pair with a target sum in a sorted array

Problem: Given a sorted array, determine whether two distinct elements add up to a target value.

Example:

```
Array:  1 2 4 6 8 9
Target: 10
```

Complete solution

```
#include <iostream>
using namespace std;

bool hasPairSum(int arr[], int n, int target) {
    int left = 0;
    int right = n - 1;

    while (left < right) {
        int sum = arr[left] + arr[right];

        if (sum == target) {
            return true;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    return false;
}

int main() {
    int arr[6] = {1, 2, 4, 6, 8, 9};

    cout << hasPairSum(arr, 6, 10);

    return 0;
}
```

Output:

```
1
```

One valid pair is `2 + 8`.

Reasoning:

- If the sum is too small, move the left pointer right to increase it.
- If the sum is too large, move the right pointer left to decrease it.
- If the sum matches, return true.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

This is a major two-pointer pattern.

## Independent challenge 4: Find the missing number

Problem: An array contains distinct numbers from `1` through `n`, but one number is missing. Find it.

Example:

```
Input:  1 2 4 5
Output: 3
```

Here, the expected range is `1` through `5`.

Complete solution

```
#include <iostream>
using namespace std;

int findMissing(int arr[], int n) {
    int expected = n * (n + 1) / 2;

    int actual = 0;

    for (int i = 0; i < n - 1; i++) {
        actual += arr[i];
    }

    return expected - actual;
}

int main() {
    int arr[4] = {1, 2, 4, 5};

    cout << findMissing(arr, 5);

    return 0;
}
```

Output:

```
3
```

Reasoning: The sum of numbers from `1` to `n` is \\(n(n+1)/2\\). Subtract the actual array sum to find the missing value.

Complexity: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

Assumptions: exactly one number is missing, all remaining values are distinct and within the specified range, and arithmetic does not overflow the chosen integer type.

## Advanced challenge 5: Search in a rotated sorted array

Problem: A sorted array has been rotated. Search for a target using binary search.

Example:

```
Original: 1 2 3 4 5 6 7
Rotated:  4 5 6 7 1 2 3
Target:   2
```

Complete solution

```
#include <iostream>
using namespace std;

int searchRotated(int arr[], int n, int target) {
    int start = 0;
    int end = n - 1;

    while (start <= end) {
        int mid = start + (end - start) / 2;

        if (arr[mid] == target) {
            return mid;
        }

        if (arr[start] <= arr[mid]) {
            if (target >= arr[start] && target < arr[mid]) {
                end = mid - 1;
            }
            else {
                start = mid + 1;
            }
        }
        else {
            if (target > arr[mid] && target <= arr[end]) {
                start = mid + 1;
            }
            else {
                end = mid - 1;
            }
        }
    }

    return -1;
}

int main() {
    int arr[7] = {4, 5, 6, 7, 1, 2, 3};

    cout << searchRotated(arr, 7, 2);

    return 0;
}
```

Output:

```
5
```

Reasoning: At each iteration, at least one side of the midpoint is sorted. We determine which side contains the target and discard the other side.

Complexity: \\(O(\log n)\\) time and \\(O(1)\\) auxiliary space, assuming distinct elements.

With duplicates, deciding which half is sorted can become ambiguous, and worst-case time can degrade to \\(O(n)\\).

## Advanced challenge 6: Compare linear and binary search

Problem: Explain which search algorithm you would choose in each situation.

Complete answer

| Situation                        | Better choice           | Reason                                |
| -------------------------------- | ----------------------- | ------------------------------------- |
| Small unsorted array             | Linear search           | Simple and no sorting required        |
| Large unsorted array, one search | Linear search           | Sorting first may cost more           |
| Large sorted array               | Binary search           | \\(O(\log n)\\) search                |
| Repeated searches on sorted data | Binary search           | Efficient repeated lookup             |
| Need to find all occurrences     | Depends on requirements | Linear scan or modified binary search |

Important reasoning: Binary search is not automatically better in every situation. Its sorted-input requirement matters.

# Part V: Module Checkpoints

These are short retrieval tests after the major learning units. Each question includes its answer.

## Checkpoint A: Array fundamentals

Q1. What is an array?

Answer: A collection of elements of the same data type stored in contiguous memory.

Q2. What is the last valid index of an array of size 10?

Answer: `9`.

Q3. What does `arr[3]` access?

Answer: The fourth element of the array.

Q4. What is the problem with `arr[10]` in an array of size 10?

Answer: It accesses outside the valid index range and causes undefined behaviour.

## Checkpoint B: Traversal and functions

Q1. Why do we initialise the maximum with `arr[0]` instead of zero?

Answer: Because all array elements could be negative.

Q2. Why does modifying `arr[0]` inside an ordinary array parameter function affect the original array?

Answer: The parameter is adjusted to a pointer that provides access to the original elements.

Q3. Why pass the array size separately?

Answer: The function parameter does not retain the original array's size.

Q4. What is the complexity of finding the maximum using one traversal?

Answer: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

## Checkpoint C: Searching and reversing

Q1. Does linear search require sorted input?

Answer: No.

Q2. Does ordinary binary search require sorted input?

Answer: Yes.

Q3. What does linear search return when the target is absent in our implementation?

Answer: `-1`.

Q4. Why does binary search use `start <= end`?

Answer: To continue while at least one candidate position remains.

Q5. What is the complexity of in-place reversal?

Answer: \\(O(n)\\) time and \\(O(1)\\) auxiliary space.

## Checkpoint D: Pointer arithmetic

Q1. What does `int* ptr = arr` point to?

Answer: The first element of the array.

Q2. If `ptr` is an `int*`, what does `ptr++` do?

Answer: Moves it to the next integer element.

Q3. What is `*(arr + 2)` equivalent to?

Answer: `arr[2]`.

Q4. What does subtracting two pointers into the same array return?

Answer: Their distance in elements.

Q5. Can we dereference a one-past-the-end pointer?

Answer: No. It may be formed, but dereferencing it is undefined behaviour.

# Part VI: Revision and Active Recall

## Smart Revision Sheet

Quick revision

| Concept                    | Key idea                                                            |
| -------------------------- | ------------------------------------------------------------------- |
| Array                      | Same-type elements in contiguous memory                             |
| Declaration                | `int arr[5];`                                                       |
| Initialisation             | `int arr[5] = {1,2,3,4,5};`                                         |
| Indexing                   | Starts at zero                                                      |
| Last valid index           | `n - 1`                                                             |
| Traversal                  | Visit elements using a loop                                         |
| Largest element            | Maintain a running maximum                                          |
| Array parameter            | Adjusted to a pointer parameter                                     |
| Linear search              | Sequential comparison                                               |
| Reverse array              | Two indices, opposite ends                                          |
| Binary search              | Repeatedly halve sorted search range                                |
| Array-pointer relationship | Array name converts to pointer to first element in most expressions |
| Pointer increment          | Moves by one pointed-to element                                     |
| Pointer subtraction        | Returns element distance for pointers into the same array           |
| Pointer indexing           | `*(arr + i)` equals `arr[i]`                                        |

### Important complexities

| Algorithm / Operation     | Time            | Auxiliary space |
| ------------------------- | --------------- | --------------- |
| Access by index           | \\(O(1)\\)      | \\(O(1)\\)      |
| Traversal                 | \\(O(n)\\)      | \\(O(1)\\)      |
| Find largest              | \\(O(n)\\)      | \\(O(1)\\)      |
| Linear search, worst case | \\(O(n)\\)      | \\(O(1)\\)      |
| Reverse array             | \\(O(n)\\)      | \\(O(1)\\)      |
| Binary search, iterative  | \\(O(\log n)\\) | \\(O(1)\\)      |
| Pair sum, two pointers    | \\(O(n)\\)      | \\(O(1)\\)      |

## Final Active Recall Test

Try answering these without referring to the explanations. The complete answers are included below.

### Q1. What is the output?

```
int arr[5] = {2, 4, 6, 8, 10};

cout << arr[0] + arr[3];
```

Answer:

```
10
```

`arr[0]` is `2`, and `arr[3]` is `8`.

### Q2. What is the output?

```
int arr[4] = {10, 20, 30, 40};

for (int i = 3; i >= 0; i--) {
    cout << arr[i] << " ";
}
```

Answer:

```
40 30 20 10
```

The loop visits the indices in reverse order.

### Q3. What is the final value of `largest`?

```
int arr[5] = {-10, -5, -30, -2, -20};

int largest = arr[0];

for (int i = 1; i < 5; i++) {
    if (arr[i] > largest) {
        largest = arr[i];
    }
}
```

Answer: `-2`.

The algorithm correctly handles negative numbers because it starts with the first element rather than zero.

### Q4. Why does this function modify the original array?

```
void update(int arr[]) {
    arr[0] = 100;
}
```

Answer: The array parameter is adjusted to a pointer parameter that provides access to the original array's elements.

### Q5. What is the time complexity?

```
for (int i = 0; i < n; i++) {
    cout << arr[i];
}
```

Answer: \\(O(n)\\). The loop processes each element once.

### Q6. What is the time complexity?

```
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        cout << arr[i] + arr[j];
    }
}
```

Answer: \\(O(n^2)\\). The inner loop runs \\(n\\) times for each of the \\(n\\) outer iterations.

### Q7. What is the difference between these two operations?

```
cout << arr[i];
```

```
cout << arr[n - 1 - i];
```

Answer: The first accesses elements in forward order when `i` increases. The second accesses corresponding elements in reverse order.

### Q8. What is the condition for binary search?

Answer: The array must be sorted in the order assumed by the algorithm.

### Q9. What is the output?

```
int arr[5] = {10, 20, 30, 40, 50};

int* ptr = arr;

ptr++;

cout << *ptr;
```

Answer:

```
20
```

The pointer initially points to the first element. Incrementing it moves it to the second element.

### Q10. What is the output?

```
int arr[5] = {10, 20, 30, 40, 50};

cout << *(arr + 3);
```

Answer:

```
40
```

`*(arr + 3)` accesses `arr[3]`.

### Q11. What is the output?

```
int arr[5] = {10, 20, 30, 40, 50};

int* p1 = &arr[0];
int* p2 = &arr[4];

cout << p2 - p1;
```

Answer:

```
4
```

There are four element positions between index `0` and index `4`.

### Q12. Why is this unsafe?

```
int arr[3] = {10, 20, 30};

int* ptr = arr + 3;

cout << *ptr;
```

Answer: `arr + 3` is a valid one-past-the-end pointer, but dereferencing it is undefined behaviour because no array element exists at that position.

# Part VII: Module Reflection

This is where we bring What → So What → Now What together at the module level.

WHAT DID I LEARN?

You learned how arrays store collections of elements, how to traverse and modify them, how functions interact with array parameters, how searching and reversing algorithms work, and how pointers provide access to array elements.

SO WHAT DOES IT ENABLE?

You can now process collections of data, select algorithms based on complexity, search efficiently in sorted data, use two-pointer techniques and reason about low-level memory access.

NOW WHAT CAN I DO?

You can implement common array algorithms, analyse their efficiency, read pointer-based array code and begin tackling more challenging array problems.

## Module Mastery Tracker

Arrays Part I mastery

# 0/12

I understand arrays and contiguous memory.

I can declare, initialise and access arrays.

I can take input and display array elements.

I can traverse arrays and find maximum/minimum values.

I understand how built-in arrays are passed to functions.

I can analyse time and auxiliary space complexity.

I can implement linear search.

I can reverse an array in place.

I can implement binary search and explain its conditions.

I understand array-to-pointer conversion.

I can perform pointer arithmetic safely.

I can explain unfamiliar array algorithms and their complexity.

Mark a skill complete only when you can demonstrate it without relying on the handbook.

## Final module audit

# Major Topic 01: Arrays

## Module 1: Arrays (Part I)

Screenshot syllabus topics

Covered

Eight integrated concept chunks

Complete

What → So What → Now What

Integrated

English and Hinglish

Included

Programming problems and solutions

Included

Developer's Code Reading Lab

Included

DSA Mastery Lab

Included

Checkpoints and active recall

Answered

### One idea to carry forward

An array is more than a collection of numbers. It is a structured sequence of objects that we can access, traverse, modify, search and reason about.

Once you understand the relationship between index, memory address, pointer and algorithm, arrays stop being a collection of syntax rules and become a powerful problem-solving tool.

And remember:

What? Understand the mechanism.

So What? Recognise the importance.

Now What? Put the knowledge to work.

That's how we'll turn every new DSA concept into a skill you can actually use. 🚀