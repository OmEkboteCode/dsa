# 02: Conditional Statements in C++

## 1. `if-else` statements

Definition: Conditional statements control the flow of execution by executing different blocks of code depending on whether a condition is true or false.

Syntax

```cpp
if (condition) {
    // Executes when true
} else {
    // Executes when false
}
```

Example

```cpp
int age = 20;

if (age >= 18) {
    cout << "Adult";
} else {
    cout << "Minor";
}
```

Output: `Adult`

### Traps and common mistakes

- `=` assigns a value; `==` compares two values.
- A condition such as `age >= 18` includes 18, whereas `age > 18` does not.
- Braces `{}` are optional for a single statement but recommended for clarity.
- An `else` belongs to the nearest unmatched `if`.

## 2. `else if` ladder

Used to check multiple conditions in sequence.

```cpp
int marks = 75;

if (marks >= 90) {
    cout << "A";
} else if (marks >= 60) {
    cout << "B";
} else {
    cout << "C";
}
```

Output: `B`

Execution stops checking the ladder once a condition is true.

Trap: Put conditions in the correct order. If you check `marks >= 60` first, a score of 95 will also match that condition, so the grade `A` will never be reached.

## 3. Ternary operator `?:`

A compact expression for choosing between two alternatives.

Syntax

```cpp
condition ? expression1 : expression2;
```

Example:

```cpp
int n = 7;
cout << (n % 2 == 0 ? "Even" : "Odd");
```

Output: `Odd`

Equivalent `if-else` logic:

```cpp
if (n % 2 == 0)
    cout << "Even";
else
    cout << "Odd";
```

Traps and common mistakes

- The condition comes before `?`.
- The true expression comes between `?` and `:`.
- The false expression comes after `:`.
- Avoid deeply nested ternary operators when `if-else` is clearer.

## 4. `switch` statement

Used to select a code block based on the value of an expression.

```cpp
int choice = 2;

switch (choice) {
    case 1:
        cout << "Start";
        break;
    case 2:
        cout << "Settings";
        break;
    default:
        cout << "Invalid choice";
}
```

Output: `Settings`

Important keywords

- `switch`: evaluates the expression.
- `case`: specifies a value to match.
- `break`: exits the switch.
- `default`: handles unmatched values.

### Traps and common mistakes

- Forgetting `break` can cause execution to fall through into subsequent cases.
- `default` is optional.
- A traditional `switch` uses supported integral, enumeration, or compatible converted values, not arbitrary conditions such as `marks >= 90`.
- Use `if-else` for ranges and complex conditions.

## 5. Build a calculator

This combines `switch`, arithmetic operators, input, and nested conditionals.

```cpp
#include <iostream>
using namespace std;

int main() {
    double a, b;
    char op;

    cin >> a >> op >> b;

    switch (op) {
        case '+':
            cout << a + b;
            break;

        case '-':
            cout << a - b;
            break;

        case '*':
            cout << a * b;
            break;

        case '/':
            if (b != 0)
                cout << a / b;
            else
                cout << "Cannot divide by zero";
            break;

        default:
            cout << "Invalid operator";
    }

    return 0;
}
```

Example input: `10 / 2`

Output: `5`

Common mistakes: forgetting `break`, failing to handle division by zero, and using the wrong data type when decimal results are required.

## 6. Quick revision table

| Statement | Best use                              |
| --------- | ------------------------------------- |
| `if`      | Execute code when a condition is true |
| `if-else` | Choose between two paths              |
| `else if` | Select among multiple conditions      |
| `?:`      | Short, simple conditional choice      |
| `switch`  | Select among fixed case values        |
| `break`   | Exit a switch case sequence           |
| `default` | Handle unmatched switch values        |

## 7. Descriptive questions with answers

Q1. What is a conditional statement?

A conditional statement controls program execution by evaluating a condition and choosing which block of code to execute.

Q2. Differentiate between `if-else` and `switch`.

`if-else` supports Boolean conditions, comparisons, and ranges. `switch` selects among discrete case values. `if-else` is generally more flexible, while `switch` can be clearer for fixed choices.

Q3. What is the ternary operator?

The ternary operator `?:` is a conditional operator that selects one of two expressions based on a condition. Its syntax is `condition ? expression1 : expression2`.

Q4. What is the purpose of `break` and `default` in a switch statement?

`break` exits the switch statement, preventing unintended fall-through. `default` specifies what to execute when no case matches.

## 8. Coding questions with answers

### Q1. Check whether a number is positive, negative, or zero.

```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;

    if (n > 0)
        cout << "Positive";
    else if (n < 0)
        cout << "Negative";
    else
        cout << "Zero";

    return 0;
}
```

Logic: First test whether the number is positive. If not, test whether it is negative. If neither condition holds, it must be zero.

### Q2. Find the larger of two numbers.

```cpp
int a = 12, b = 8;

if (a > b)
    cout << a;
else if (b > a)
    cout << b;
else
    cout << "Equal";
```

Output: `12`

Trap: Include equality if the question requires handling equal inputs.

### Q3. Check whether a year is a leap year.

```cpp
int year;
cin >> year;

if (year % 400 == 0 ||
    (year % 4 == 0 && year % 100 != 0))
    cout << "Leap year";
else
    cout << "Not a leap year";
```

Logic: A year is a leap year if it is divisible by 400, or if it is divisible by 4 but not by 100.

Examples: 2000 is a leap year; 1900 is not.

### Q4. Create a simple calculator.

Use the calculator program in Section 5. Practise entering different operators, invalid operators, and a zero divisor. Understand why each branch executes before attempting to reproduce the program from memory.

## 9. How to read code aloud 🎙️

Read the code in meaningful chunks, translating each statement into natural English.

Consider:

```cpp
int n = 8;

if (n % 2 == 0) {
    cout << "Even";
} else {
    cout << "Odd";
}
```

SAY IT ALOUD

Declare an integer `n` and initialize it to eight. Check whether the remainder when `n` is divided by two equals zero. If the condition is true, print Even. Otherwise, print Odd.

Your code-reading vocabulary

\| Syntax | Say it aloud as | |---|---| | `int n = 8` | Declare integer `n` and initialize it to eight | | `n % 2` | The remainder when `n` is divided by two | | `== 0` | Is equal to zero | | `&&` | And | | `||` | Or | | `!condition` | Not condition | | `else if` | Otherwise, if this condition holds | | `break` | Exit the switch statement |

### A 3-step fluency drill

1. Read: Say what each line means in English.
2. Predict: State which branch executes and what gets printed.
3. Explain: Justify the result without running the code.

