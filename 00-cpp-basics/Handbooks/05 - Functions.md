Sigma DSA with C++ | Module 5: Functions

 DSA Foundation

This version follows our revised design: fewer, more comprehensive learning prompts, integrated explanations, separate programming practice, and one unified Developer's Code Reading Lab.
Part 1. Module overview
What you'll learn
By the end of this module, you should be able to:
1. Understand why functions are essential in programming.
2. Declare, define and call functions.
3. Work with parameters, arguments and return values.
4. Use functions to solve mathematical and logical problems.
5. Understand how function calls execute using the call stack.
6. Distinguish local and global scope.
7. Apply function overloading.
8. Decompose larger problems into smaller functions.
The central idea: A function takes responsibility for one well-defined task. Instead of writing an entire program as one enormous block, we divide it into smaller, reusable units.

Part 2. Concept learning chunks
Chunk 1. Functions and modular programming
HIGH PRIORITY
Learning prompt
Imagine building a calculator that performs addition, subtraction, multiplication and division. Instead of writing all the operations inside main(), you create separate functions for each operation.

Explain what a function is, why programmers use functions, how functions support modular programming, and the roles of function declaration, definition and function call. Also explain why a function prototype is sometimes necessary.
Model answer
A function is a reusable block of code designed to perform a specific task.

For example:
int add(int a, int b) {
    return a + b;
}


This function accepts two integers and returns their sum.
Why do we use functions?
Consider a program containing 500 lines of code. If every operation is written inside main(), the program becomes difficult to understand, maintain and debug.

Functions solve this problem through modular programming.

Modular programming means dividing a large program into smaller, independent and manageable parts.

The advantages include:
- Reusability: Write a function once and call it multiple times.
- Readability: Smaller functions make code easier to understand.
- Maintainability: Modify one function without unnecessarily changing the entire program.
- Debugging: Isolate problems within individual functions.
- Testing: Test smaller units independently.
Three important stages of a function
1. Function declaration

A declaration informs the compiler about the function's name, return type and parameters.
int add(int a, int b);


2. Function definition

The definition contains the actual implementation.
int add(int a, int b) {
    return a + b;
}


3. Function call

A function call executes the function.
int result = add(10, 20);


The value returned by add() is stored in result.
Complete example
#include <iostream>
using namespace std;

int add(int a, int b);

int main() {
    int result = add(10, 20);
    cout << result;
    return 0;
}

int add(int a, int b) {
    return a + b;
}


Output:
30


Why is the function prototype needed?
C++ generally requires a function to be declared before it is called.

Here, main() calls add() before its definition appears. The prototype informs the compiler about the function beforehand.

Without a prior declaration, the compiler may not know how to interpret the call.
Hinglish explanation
Function ek reusable code block hota hai jo ek specific task perform karta hai.

Maan lo calculator bana rahe ho. Addition, subtraction aur multiplication ke liye alag-alag functions bana sakte ho.

Isse poora program ek hi jagah likhne ki zarurat nahi padti.
- Declaration compiler ko function ke baare mein batata hai.
- Definition function ka actual kaam batati hai.
- Function call function ko execute karta hai.
Prototype tab useful hota hai jab function ki definition uske call ke baad likhi ho.
Smart Notes
Term	Meaning
Function	Reusable block of code
Declaration	Introduces a function
Definition	Contains implementation
Function call	Executes a function
Prototype	Function declaration before its use
Modular programming	Dividing a program into smaller units

Remember: Declaration tells, definition implements, call executes.

Chunk 2. Parameters, arguments and return values

HIGH PRIORITY
 DSA FOUNDATION

Learning prompt
A function receives two numbers, performs an operation and gives the result back to the calling program. Explain how functions receive input and produce output. Discuss parameters, arguments, return types, return, void, and the difference between printing a value and returning a value.
Model answer
Functions communicate with the rest of the program through parameters and return values.
1. Parameters and arguments
Consider:
int multiply(int a, int b) {
    return a * b;
}

int main() {
    int result = multiply(4, 5);
}


- a and b are parameters. They receive values inside the function.
- 4 and 5 are arguments. They are supplied when calling the function.
Think of parameters as input slots and arguments as the actual values placed into those slots.
2. Return type
The return type specifies what type of value a function gives back.
int getNumber() {
    return 10;
}


Here, int indicates that the function returns an integer.

Common return types:
Return type	Purpose
int	Returns an integer
float	Returns a floating-point value
double	Returns a double-precision value
char	Returns a character
bool	Returns true or false
void	Returns no value

3. Return statement
The return statement sends a value back to the calling function and terminates the current function execution.
int square(int n) {
    return n * n;
}


If we call:
int result = square(5);


The returned value is 25.
4. Void functions
A void function performs a task but does not return a value.
void greet() {
    cout << "Hello!";
}


Calling:
greet();


prints the message.
5. Printing versus returning
This is an important distinction.

Printing:
void square(int n) {
    cout << n * n;
}


Returning:
int square(int n) {
    return n * n;
}


The first function displays the result. The second gives the result back so another part of the program can use it.

For example:
int result = square(5);
cout << result + 10;


This is possible because square() returns a value.

DSA insight: Returning values makes functions composable. One function's output can become another function's input.
Hinglish explanation
Parameters function ke input variables hote hain. Arguments woh actual values hain jo function call karte waqt pass karte hain.

Return type batata hai ki function kis type ki value wapas dega.

return value ko calling function tak bhejta hai.

void ka matlab hai function koi value return nahi karega.

Ek important difference:
- cout value screen par dikhata hai.
- return value program ke doosre parts ko use karne ke liye deta hai.
Smart Notes
return expression;


- A function's return type should match the returned value.
- A non-void function should return an appropriate value on every reachable path.
- A void function does not return a value.
- return ends the current function.
- Printing and returning are not interchangeable.

Chunk 3. Functions as problem-solving tools

DSA FOUNDATION
 HIGH PRIORITY

Learning prompt
You are developing a mathematical utility program. It should calculate factorials, check whether a number is prime, and calculate binomial coefficients.

Explain how these tasks can be implemented using separate functions. Discuss the logic, use of return types, loop-based calculations, early returns, function reuse and relevant edge cases.
Model answer
Functions are not just a way to organise code. They help us break a problem into smaller logical tasks.

Let's explore three examples.
A. Factorial function
The factorial of a non-negative integer is the product of all positive integers up to that number.
\[
n! = n \times (n-1) \times \cdots \times 1
\]

Special case:
\[
0! = 1
\]

Program:
int factorial(int n) {
    int result = 1;

    for (int i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}


Example:

For factorial(5):
Iteration	i	result
Initial	'-	1
1	1	1
2	2	2
3	3	6
4	4	24
5	5	120

Output: 120

Why initialise result = 1?

Because 1 is the multiplicative identity. Multiplying by 1 does not change a number.

If we initialise it to zero, every multiplication will remain zero.

Complexity:
- Time: \(O(n)\)
- Auxiliary space: \(O(1)\)
Edge cases:
- factorial(0) should return 1.
- Negative inputs are invalid for this definition.
- int overflows for relatively small factorials. Use an appropriate type and check its limits.
B. Prime-checking function
A prime number is a natural number greater than 1 that has exactly two positive divisors: 1 and itself.

Examples: 2, 3, 5, 7, 11.

Program:
bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}


How does it work?
1. Numbers less than or equal to 1 are not prime.
2. Start checking possible divisors from 2.
3. If a divisor divides n exactly, the number is not prime.
4. If no divisor is found, the number is prime.
Why check only while i * i <= n?

If a number has a factor larger than its square root, it must also have a corresponding factor smaller than its square root.

Therefore, checking beyond the square root is unnecessary.

Complexity:
- Time: \(O(\sqrt n)\)
- Auxiliary space: \(O(1)\)
C. Binomial coefficient
The binomial coefficient is used to calculate the number of ways to select r objects from n objects, without considering order.
\[
{n \choose r} = \frac{n!}{r!(n-r)!}
\]

We can reuse the factorial function.
int factorial(int n) {
    int result = 1;

    for (int i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}

int nCr(int n, int r) {
    return factorial(n) /
           (factorial(r) * factorial(n - r));
}


Example:
\[
{5 \choose 2} = \frac{5!}{2!3!} = 10
\]

Important: This simple implementation assumes valid inputs, 0 <= r <= n, and that intermediate factorial calculations do not overflow. A mathematically valid final answer does not guarantee that intermediate calculations fit in int.
Hinglish explanation
Factorial mein hum 1 se n tak sab numbers multiply karte hain.

Prime number check karne ke liye dekhte hain ki kya 1 aur khud ke alawa koi divisor hai.

Agar koi divisor mil gaya, toh false return karte hain. Agar koi divisor nahi mila, toh true.

Binomial coefficient mein factorial function ko reuse kar sakte hain. Isse hume same logic baar-baar likhna nahi padta.
Smart Notes
Concept	Key idea
Factorial	Running product
Prime check	Divisor search
bool	Logical true/false result
Early return	Exit as soon as the answer is known
Function reuse	Call an existing function inside another
sqrt(n) optimisation	Avoid unnecessary divisor checks

DSA foundation: The prime-checking function demonstrates algorithmic optimisation. A simple loop can become significantly more efficient when we understand the mathematical structure of the problem.

Chunk 4. Function execution and the call stack
DSA FOUNDATION
Learning prompt
Consider a program where main() calls function A, function A calls function B, and function B calls function C. Explain how the program executes these calls, how control returns to previous functions, and how the call stack manages function execution. Connect this idea to recursion.
Model answer
When a function calls another function, the program temporarily pauses the current function and starts executing the called function.

To manage this process, programs use a memory structure called the call stack.
Understanding the call stack
A stack follows the principle:

LIFO: Last In, First Out.

The last function called is the first one to finish.

Example:
#include <iostream>
using namespace std;

void third() {
    cout << "Third\n";
}

void second() {
    cout << "Second\n";
    third();
}

void first() {
    cout << "First\n";
    second();
}

int main() {
    first();
    return 0;
}


Output:
First
Second
Third


Execution sequence
Call sequence
main()


first()


second()


third()

Each function returns to the function that called it.
When third() finishes, execution returns to second(). When second() finishes, execution returns to first(). Finally, first() returns to main().

Each active function call has an associated stack frame, which stores information needed to continue execution, such as local variables and return information.
Connection to recursion
Recursion occurs when a function calls itself.
int factorial(int n) {
    if (n == 0) {
        return 1;
    }

    return n * factorial(n - 1);
}


For factorial(3):
factorial(3)
    factorial(2)
        factorial(1)
            factorial(0)


The calls then return in reverse order.
\[
3 \times 2 \times 1 \times 1 = 6
\]

Important: Each recursive call creates another active call frame. Deep recursion can consume substantial stack memory.
Hinglish explanation
Jab ek function doosre function ko call karta hai, toh current function temporarily pause ho jata hai.

Called function complete hone ke baad control wapas caller ke paas aata hai.

Call stack LIFO principle follow karta hai. Jo function sabse last mein call hua hai, woh sabse pehle finish hota hai.

Recursion mein function khud ko call karta hai, isliye call stack par multiple function calls ho sakte hain.
Smart Notes
- Call stack manages active function calls.
- LIFO means Last In, First Out.
- Each active call has its own stack frame.
- A function returns control to its caller.
- Recursion uses the call stack.
- Missing or incorrect base cases can cause infinite recursion or stack exhaustion.

Chunk 5. Scope and lifetime of variables
HIGH PRIORITY
Learning prompt
A program contains variables declared inside functions as well as variables declared outside all functions. Explain the difference between local and global variables, their scope and lifetime, how variable shadowing works, and how the scope resolution operator accesses a global variable when a local variable has the same name.
Model answer
Scope determines where a variable can be accessed.

Lifetime determines how long a variable exists during program execution.

These are related but different concepts.
1. Local variables
A variable declared inside a function or block is local to that scope.
void display() {
    int x = 10;
    cout << x;
}


The variable x is accessible within the function's scope.

Ordinary local variables generally exist while execution is inside their block and are destroyed when that block exits.
2. Global variables
A variable declared outside all functions is a global variable.
int x = 100;

int main() {
    cout << x;
    return 0;
}


The global variable can generally be accessed by functions after its declaration, subject to normal visibility and scope rules.

Its lifetime normally extends throughout the program's execution.
3. Local and global variables with the same name
#include <iostream>
using namespace std;

int x = 100;

int main() {
    int x = 20;

    cout << x << endl;
    cout << ::x << endl;

    return 0;
}


Output:
20
100


Here:
- x accesses the local variable.
- ::x accesses the global variable.
The :: symbol is called the scope resolution operator.
4. Variable shadowing
When a variable in an inner scope has the same name as a variable in an outer scope, the inner variable hides the outer variable within that inner scope.

This is called variable shadowing.
5. Static local variables
A static local variable retains its value between function calls.
void counter() {
    static int count = 0;

    count++;
    cout << count << endl;
}


Calling counter() three times produces:
1
2
3


Unlike an ordinary local variable, the static local variable has program-long storage duration, while its name remains accessible only within its scope.
Hinglish explanation
Local variable function ya block ke andar declare hota hai. Usko usi scope ke andar access kar sakte hain.

Global variable sabhi suitable functions ke liye accessible ho sakta hai.

Scope batata hai variable kahan accessible hai. Lifetime batata hai variable kitni der memory mein exist karta hai.

Agar local aur global variable ka naam same ho, toh local variable outer variable ko hide kar sakta hai.

::x global variable ko access karne ke liye use hota hai.
Smart Notes
Concept	Meaning
Local variable	Declared inside a function/block
Global variable	Declared outside functions
Scope	Region where a name is accessible
Lifetime	Duration for which an object exists
Shadowing	Inner name hides an outer name
::	Scope resolution operator
Static local	Retains its value between calls


Chunk 6. Function overloading
HIGH PRIORITY
Learning prompt
A calculator should perform addition on integers, floating-point numbers and different numbers of arguments. Explain how function overloading allows multiple functions to share the same name, the conditions required for overloading, and why changing only the return type is insufficient.
Model answer
Function overloading allows multiple functions to have the same name but different parameter lists.

The compiler identifies which function to execute based on the arguments supplied in the function call.
Example 1: Different number of parameters
int add(int a, int b) {
    return a + b;
}

int add(int a, int b, int c) {
    return a + b + c;
}


Calls:
add(2, 3);       // Two parameters
add(2, 3, 4);    // Three parameters


Example 2: Different parameter types
int add(int a, int b) {
    return a + b;
}

double add(double a, double b) {
    return a + b;
}


Calls:
add(2, 3);
add(2.5, 3.5);


Example 3: Different order of parameter types
void display(int a, double b) {
    cout << a << " " << b;
}

void display(double a, int b) {
    cout << a << " " << b;
}


The parameter types appear in a different order, so these are different overloads.
Important rules
Functions can be overloaded based on:
- Number of parameters.
- Types of parameters.
- Order of parameter types.
However, return type alone cannot distinguish overloaded functions.

This is invalid:
int calculate(int a) {
    return a;
}

double calculate(int a) {
    return a;
}


Both functions have the same parameter list. Changing only the return type does not create a valid overload.
Ambiguous overloads
Sometimes the compiler cannot determine which overload is the best match.
void show(int a, double b);
void show(double a, int b);

// Depending on the supplied arguments,
// the compiler may find no unique best match.


Avoid creating overload sets that make function calls ambiguous.
Hinglish explanation
Function overloading ka matlab hai same naam ke multiple functions banana, lekin unke parameter lists different hone chahiye.

Difference number, type ya order mein ho sakta hai.

Compiler arguments dekhkar decide karta hai ki kaunsa function call karna hai.

Sirf return type change karne se function overloading valid nahi hoti.
Smart Notes
- Same function name, different parameter lists.
- Compiler selects the appropriate overload.
- Return type alone cannot distinguish overloads.
- Ambiguous calls can cause compilation errors.

Part 3. Integrated programming problems
These problems connect the concepts above. Some have complete worked solutions, while others are designed for guided or independent implementation.
Problem 1. Create a calculator using functions
DSA FOUNDATION
Problem statement

Write a program that accepts two integers and performs addition, subtraction, multiplication and division using separate functions.
Approach
Break the calculator into four independent tasks:
- add() returns the sum.
- subtract() returns the difference.
- multiply() returns the product.
- divide() returns the quotient.
Worked solution
#include <iostream>
using namespace std;

int add(int a, int b) {
    return a + b;
}

int subtract(int a, int b) {
    return a - b;
}

int multiply(int a, int b) {
    return a * b;
}

double divide(int a, int b) {
    return (double)a / b;
}

int main() {
    int a = 20;
    int b = 5;

    cout << add(a, b) << endl;
    cout << subtract(a, b) << endl;
    cout << multiply(a, b) << endl;
    cout << divide(a, b) << endl;

    return 0;
}


Output:
25
15
100
4


The division function converts one operand to double, allowing floating-point division. In a complete calculator, you should also handle division by zero.
Hinglish explanation
Humne har operation ke liye alag function banaya hai.

main() sirf inputs aur function calls manage karta hai. Actual calculations respective functions perform karte hain.

Isse program modular aur reusable ban jata hai.
What → So What → Now What
- What: A calculator implemented using separate functions.
- So What: Each function has one clear responsibility.
- Now What: Try adding modulus and power operations without putting their logic inside main().

Problem 2. Find the maximum of three numbers
DSA FOUNDATION
Problem statement

Write a function that accepts three integers and returns the largest.
Guided approach
1. Assume the first number is the maximum.
2. Compare the second number with the current maximum.
3. Update the maximum if necessary.
4. Compare the third number.
5. Return the final maximum.
Complete the implementation:
int maximum(int a, int b, int c) {
    int maxNum = a;

    if (b > maxNum) {
        maxNum = b;
    }

    if (c > maxNum) {
        maxNum = c;
    }

    return maxNum;
}


Example: maximum(10, 25, 15) returns 25.

Complexity: Time \(O(1)\), auxiliary space \(O(1)\).
What → So What → Now What
- What: A function that finds the largest among three numbers.
- So What: The variable maxNum maintains the best answer found so far.
- Now What: Extend this idea to find the maximum element in an array.

Problem 3. Count the digits of a number

DSA FOUNDATION
 HIGH PRIORITY

Problem statement

Write a function that counts the number of digits in an integer.
Approach
Repeatedly divide the number by 10. Every division removes the last digit.

For example:
5432 → 543 → 54 → 5 → 0


The number of divisions is the digit count.
Worked solution
int countDigits(int n) {
    if (n == 0) {
        return 1;
    }

    int count = 0;

    while (n != 0) {
        count++;
        n /= 10;
    }

    return count;
}


This version assumes a non-negative integer input. For negative values, convert to a safe non-negative representation or use a carefully designed alternative that handles the minimum representable integer.

Complexity: Time \(O(\log_{10} n)\), auxiliary space \(O(1)\).
Hinglish explanation
Har baar number ko 10 se divide karne par last digit remove ho jata hai.

Hum har division ke saath count increment karte hain. Jab number zero ho jata hai, tab count return kar dete hain.

Special case: 0 mein ek digit hota hai, isliye directly 1 return karte hain.
What → So What → Now What
- What: A function counts digits through repeated division.
- So What: The loop gradually reduces the problem.
- Now What: Modify it to calculate the sum of all digits.

Problem 4. Build a mathematical utility library
DSA FOUNDATION
Problem statement

Create separate functions to:
1. Calculate the square of a number.
2. Calculate the cube of a number.
3. Check whether a number is even.
4. Check whether a number is odd.
Worked solution
int square(int n) {
    return n * n;
}

int cube(int n) {
    return n * n * n;
}

bool isEven(int n) {
    return n % 2 == 0;
}

bool isOdd(int n) {
    return n % 2 != 0;
}


Why use bool?

Because even/odd checks have only two possible answers: true or false.
Hinglish explanation
Square aur cube numerical values return karte hain, isliye unka return type int hai.

Even aur odd checks logical answers return karte hain, isliye unka return type bool hai.
What → So What → Now What
- What: A small collection of mathematical utility functions.
- So What: Functions can represent different types of results.
- Now What: Combine these functions into a program that analyses several numbers.

Problem 5. Print all prime numbers in a range

DSA FOUNDATION
 HIGH PRIORITY

Problem statement

Write a program that prints all prime numbers between two given integers using separate functions.
Approach
Use two functions:
1. isPrime(n) checks whether a number is prime.
2. printPrimes(start, end) checks every number in the range and prints prime numbers.
Worked solution
#include <iostream>
using namespace std;

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }

    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }

    return true;
}

void printPrimes(int start, int end) {
    for (int i = start; i <= end; i++) {
        if (isPrime(i)) {
            cout << i << " ";
        }
    }
}

int main() {
    printPrimes(10, 30);

    return 0;
}


Output:
11 13 17 19 23 29


Why is this program modular?
isPrime() handles the mathematical logic.

printPrimes() handles the iteration and printing.

Each function has a distinct responsibility.
Complexity
For a range of \(N\) positive integers, with each primality check taking up to \(O(\sqrt{N})\) time, a simple upper bound is:
\[
O(N\sqrt{N})
\]

Auxiliary space: \(O(1)\).
Hinglish explanation
printPrimes() range ke har number ko isPrime() function mein bhejta hai.

Agar function true return karta hai, toh number print hota hai.

Is tarah ek function doosre function ki functionality reuse karta hai.
What → So What → Now What
- What: Two functions cooperate to solve one larger problem.
- So What: A complex task can be divided into reusable components.
- Now What: Try returning the count of prime numbers instead of printing them.

Problem 6. Calculate factorial and binomial coefficient
DSA FOUNDATION
Problem statement

Write reusable functions to calculate factorial and the binomial coefficient.
Worked solution
#include <iostream>
using namespace std;

long long factorial(int n) {
    long long result = 1;

    for (int i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}

long long nCr(int n, int r) {
    if (n < 0 || r < 0 || r > n) {
        return -1;
    }

    return factorial(n) /
           (factorial(r) * factorial(n - r));
}

int main() {
    cout << factorial(5) << endl;
    cout << nCr(5, 2) << endl;

    return 0;
}


Output:
120
10


Important limitation: Even long long overflows for sufficiently large factorials. This implementation is suitable only for inputs where every intermediate factorial and multiplication is representable. For larger values, consider a multiplicative approach or arbitrary-precision arithmetic.
Hinglish explanation
nCr() factorial function ko reuse karta hai.

Agar r, n se bada hai ya inputs negative hain, toh invalid result indicate karte hain.

Lekin large values ke liye overflow ka dhyan rakhna zaroori hai.

Part 4. Developer's Code Reading Lab
LONG-TERM VALUE
This lab has one goal: make you comfortable explaining unfamiliar code in natural English while thinking about it like a developer.

For each example, focus on the intent, variable responsibilities, control flow and correctness. Output prediction supports the explanation, but is not the main exercise.
Lab 1. Understand a function's responsibility
int calculate(int a, int b) {
    int result = a + b;
    return result;
}


Developer's Code Reading

The function calculate accepts two integer inputs, a and b. It adds them together and stores the result in a local variable called result. Finally, it returns that value to the calling function.

The function has one responsibility: calculate the sum of two integers.

Notice that the function does not print anything. It returns the result, allowing the caller to decide what to do with it.

What to notice:
- a and b are input parameters.
- result stores the intermediate answer.
- return transfers the calculated value to the caller.
- The function is reusable because it does not depend on a specific input.
Lab 2. Read nested function calls
int doubleValue(int n) {
    return n * 2;
}

int addFive(int n) {
    return n + 5;
}

int main() {
    cout << addFive(doubleValue(3));
}


Developer's Code Reading

The program first evaluates the inner function call, doubleValue(3). That function doubles its input and returns 6.

The returned value becomes the argument to addFive(). That function adds 5 and returns 11.

Finally, cout displays the result.

The important concept is function composition: the output of one function becomes the input of another.

Output: 11
Lab 3. Understand nested loops inside a function
void printTable(int n) {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= 3; j++) {
            cout << n * j << " ";
        }

        cout << endl;
    }
}


Developer's Code Reading

The function receives a number n and prints a multiplication pattern.

The outer loop controls how many rows are printed. The inner loop iterates three times and prints multiples of n.

After the inner loop finishes, the program prints a newline and starts the next outer-loop iteration.

Notice that the inner loop does not use i. Therefore, each row prints the same three multiples.

For printTable(2), the output is:
2 4 6
2 4 6
2 4 6


The repeated output is not necessarily a bug. It depends on the intended pattern. If the goal were a conventional multiplication table with increasing row values, the expression would need to use i as well.
Lab 4. Identify a logical bug
bool isEven(int n) {
    if (n % 2 == 0) {
        return true;
    }

    return true;
}


Developer's Code Reading

The function intends to determine whether an integer is even.

It checks whether the remainder after division by 2 is zero. If that condition is true, it returns true.

However, when the condition is false, the function also returns true.

Therefore, the function incorrectly classifies every integer as even.

Correct implementation:
bool isEven(int n) {
    return n % 2 == 0;
}


The comparison itself produces a Boolean result, so we can return it directly.
Lab 5. Trace function calls
void C() {
    cout << "C ";
}

void B() {
    cout << "B ";
    C();
}

void A() {
    cout << "A ";
    B();
}

int main() {
    A();
}


Developer's Code Reading

Execution begins in main(), which calls A().

A() prints its label and then calls B(). B() prints its label and calls C(). Finally, C() prints its label and finishes.

Control returns from C() to B(), then from B() to A(), and eventually back to main().

The function calls follow a nested execution pattern managed by the call stack.

Output:
A B C


Lab 6. Follow variable state through a loop
int sumEven(int n) {
    int sum = 0;

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 0) {
            sum += i;
        }
    }

    return sum;
}


Developer's Code Reading

The function calculates the sum of all even integers from 1 through n.

It begins with sum equal to zero. The loop visits every integer from 1 to n. During each iteration, the condition checks whether the current number is divisible by 2.

If it is even, the program adds it to the running total. Odd numbers are ignored.

After the loop finishes, the accumulated sum is returned.

For sumEven(6), the selected numbers are 2, 4 and 6, producing 12.

The important invariant is that after each iteration, sum contains the total of all even numbers processed so far.

Complexity: Time \(O(n)\), auxiliary space \(O(1)\).

Part 5. DSA Mastery Lab
Now we move from understanding examples to solving problems independently.
Guided challenges
These are designed to help you build the reasoning process.
Challenge	Task	Main skill
G1	Create a function to calculate the sum of digits	Loop and accumulator
G2	Create a function to reverse an integer	Digit extraction
G3	Create a function to check a palindrome number	Comparison and state
G4	Create a function to find the GCD of two numbers	Mathematical reasoning

G1. Sum of digits
Example:
Input: 583
Output: 16


Reasoning:
\[
5+8+3=16
\]

Hint: Use % 10 to extract the last digit and / 10 to remove it.
G2. Reverse a number
Example:
Input: 1234
Output: 4321


Hint: Extract the last digit and append it to a new number.
G3. Palindrome number
Example:
Input: 121
Output: true


Hint: Reverse the number and compare it with the original. Think about negative numbers and overflow.
G4. GCD
Example:
GCD(12, 18) = 6


Hint: Explore Euclid's algorithm:
\[
\gcd(a,b)=\gcd(b,a\bmod b)
\]


Independent challenges
INDEPENDENT PRACTICE
Try these without looking at solutions first.
1. Write a function that returns the smallest of four numbers.
2. Write a function that checks whether a number is an Armstrong number.
3. Write a function that checks whether a number is a perfect number.
4. Write a function that returns the sum of all prime numbers up to n.
5. Write a function that counts how many digits in a number are even.
6. Create a calculator using function overloading.
7. Write a function that returns the nth Fibonacci number.
8. Build a menu-driven mathematical utility program using separate functions.
Advanced reasoning challenges
These are slightly beyond routine implementation.

Challenge A: Function decomposition

You are given a task to analyse a number. Your program must:
- Count its digits.
- Calculate the sum of its digits.
- Reverse the number.
- Check whether it is prime.
- Check whether it is a palindrome.
Design the function architecture before writing the code. Which functions should be independent? Which functions can reuse others?

Challenge B: Complexity comparison

Consider two ways of checking whether a number is prime:
- Method 1: Check all divisors from 2 to n - 1.
- Method 2: Check divisors only up to the square root of n.
Explain why both methods are correct but their running times differ.

Challenge C: Recursion and iteration

Implement factorial using both a loop and recursion.

Compare:
- Execution flow.
- Memory usage.
- Time complexity.
- Stack usage.
- Risk of stack overflow.

Part 6. Revision sheet
Functions: essential syntax
Function declaration
int add(int a, int b);


Function definition
int add(int a, int b) {
    return a + b;
}


Function call
int result = add(10, 20);


Void function
void greet() {
    cout << "Hello";
}


Boolean function
bool isEven(int n) {
    return n % 2 == 0;
}


Function overloading
int add(int a, int b);
double add(double a, double b);


Static local variable
static int count = 0;


Concepts you must remember
Topic	Key takeaway
Function	Reusable block of code
Prototype	Declaration before use
Parameters	Inputs received by function
Arguments	Values supplied during call
Return	Sends a value back
Void	No returned value
Call stack	Manages active function calls
Scope	Where a variable can be accessed
Lifetime	How long a variable exists
Shadowing	Inner variable hides outer variable
Overloading	Same name, different parameter lists
Recursion	A function calls itself


Part 7. Syllabus coverage and mastery checklist
Coverage audit
Module 6 topic	Covered
Introduction to functions	Yes
Function declaration and definition	Yes
Function calls and prototypes	Yes
Parameters and arguments	Yes
Return types and void	Yes
Factorial	Yes
Prime checking	Yes
Call stack	Yes
Scope and lifetime	Yes
Global and local variables	Yes
Binomial coefficient	Yes
Function overloading	Yes
Functions in integrated programs	Yes

This is a coverage audit of the Module 6 topics included in this handbook, not a verification against the exact wording of every Sigma lecture or assignment.
Your mastery checklist
Module 6 progress
0/12



[ ] I can explain why functions are used.
[ ] I can distinguish declaration, definition and function call.
[ ] I understand parameters and arguments.
[ ] I can explain return values versus printing.
[ ] I can write factorial and prime-checking functions.
[ ] I understand the call stack and function execution.
[ ] I can distinguish scope from lifetime.
[ ] I understand local and global variables.
[ ] I can explain function overloading.
[ ] I can decompose a larger problem into smaller functions.
[ ] I can read unfamiliar code and explain its intent naturally.
[ ] I can identify edge cases and analyse complexity.
Reset checklist

Final learning principle
For this module, don't measure your understanding only by whether you can write a function from scratch.

Measure it by whether you can:
1. Understand what a function is responsible for.
2. Construct it with correct inputs, logic and outputs.
3. Connect multiple functions to solve a larger problem.
4. Explain unfamiliar code clearly and naturally.
5. Evaluate its correctness, edge cases and efficiency.
That's the foundation we want to carry into loops, arrays, strings, pointers, recursion and eventually advanced DSA. 🚀