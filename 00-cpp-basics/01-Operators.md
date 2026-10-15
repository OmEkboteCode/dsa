Om, perfect. We'll make these Smart Notes: compact, exam-useful, easy to revise, and focused on concepts that actually matter. We'll follow the exact Operators section from your Sigma screenshot, without adding unnecessary theory.

# Smart Notes 01: Operators in C++

DSA with C++ · Sigma Batch · Chapter 6

## 1. Constants

A constant is a value that does not change during program execution.

```
const int MAX = 100;
```

- `const` prevents reassignment.
- By convention, constant names are often written in uppercase.
- Trying to modify `MAX` causes a compilation error.

```
const double PI = 3.14159;
```

## 2. Implicit type conversion

C++ automatically converts a value from one type to another when required.

```
int x = 10;
double y = x;   // int → double
```

Here, `y` becomes `10.0`.

Important: Converting a floating-point number to an integer discards the fractional part.

```
int x = 5.8;    // x = 5
```

## 3. Explicit typecasting

We manually convert a value into another type.

```
double x = 9.8;
int y = (int)x;     // y = 9
```

Modern C++ also supports:

```
int y = static_cast<int>(x); 
```

Classic DSA trap:

```
int a = 5, b = 2;
cout << a / b;      // 2
```

Both operands are integers, so integer division discards the fractional part.

```
cout << (double)a / b;  // 2.5
```

## 4. Arithmetic operators

| Operator | Meaning        | Example (`a = 7, b = 2`) |
| -------- | -------------- | ------------------------ |
| `+`      | Addition       | `a + b` → `9`            |
| `-`      | Subtraction    | `a - b` → `5`            |
| `*`      | Multiplication | `a * b` → `14`           |
| `/`      | Division       | `a / b` → `3`            |
| `%`      | Remainder      | `a % b` → `1`            |

Remember:

- `%` gives the remainder for integer operands.
- `*`, `/`, and `%` have higher precedence than `+` and `-`.
- Use parentheses to make complicated expressions clear.

```
cout << 2 + 3 * 4;    // 14
cout << (2 + 3) * 4;  // 20
```

## 5. Unary arithmetic operators

Unary operators act on one operand.

| Operator | Meaning           |
| -------- | ----------------- |
| `+x`     | Positive value    |
| `-x`     | Negates the value |
| `++x`    | Pre-increment     |
| `x++`    | Post-increment    |
| `--x`    | Pre-decrement     |
| `x--`    | Post-decrement    |

The key distinction is when the updated value is used.

```
int x = 5;
cout << ++x;   // 6
```

Pre-increment updates first, then uses the value.

```
int x = 5;
cout << x++;   // 5
```

Post-increment uses the old value first, then updates `x` to `6`.

## 6. Assignment operators

Assignment operators store a value in a variable.

| Operator | Equivalent operation |
| -------- | -------------------- |
| `x = 5`  | Assign `5` to `x`    |
| `x += 3` | `x = x + 3`          |
| `x -= 3` | `x = x - 3`          |
| `x *= 3` | `x = x * 3`          |
| `x /= 3` | `x = x / 3`          |
| `x %= 3` | `x = x % 3`          |

Example:

```
int x = 10;
x += 5;
x *= 2;
// x = 30
```

Code-reading habit: Read the right-hand side, calculate it, and then update the left-hand variable.

## 7. Relational operators

Relational operators compare two values and produce a Boolean result: `true` or `false`.

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

```
int a = 5, b = 8;
cout << (a < b);   // 1 (true)
cout << (a == b);  // 0 (false)
```

By default, `cout` prints Boolean values as `1` and `0`, unless Boolean formatting has been changed.

Common mistake: `=` assigns a value; `==` compares values.

## 8. Logical operators

Logical operators combine or reverse conditions.

| Operator | Meaning | Example                       |
| -------- | ------- | ----------------------------- |
| `&&`     | AND     | `(5 > 2 && 8 > 4)` → true     |
| `\\|\\|` | OR      | `(5 < 2 \\|\\| 8 > 4)` → true |
| `!`      | NOT     | `!(5 > 2)` → false            |

- AND (`&&`): true only when both conditions are true.
- OR (`||`): true when at least one condition is true.
- NOT (`!`): reverses a Boolean result.

C++ uses short-circuit evaluation: with `&&`, the second condition is skipped if the first is false; with `||`, it is skipped if the first is true.

Example:

```
int age = 20;
cout << (age >= 18 && age <= 60);  // 1
```
