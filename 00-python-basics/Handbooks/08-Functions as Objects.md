# **MIT 6.100L, Lecture 8: Functions as Objects**



Important for Python and DSA

Full notes



This lecture introduces an important idea: **functions are objects in Python.**

Until now, you've learned how to define functions, pass arguments and return values. Now you'll learn how Python manages functions, where variables live, and how functions can be treated like other values.

The lecture covers three major concepts:

1. Environments and scope.
2. Functions as objects.
3. Higher-order functions.

These concepts are useful for understanding Python code, callbacks, decorators and functional programming.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://learn.mit.edu\&sz=32)

MIT Learn+1



## **1. Environments**

An environment is a mapping between variable names and the objects or values they refer to.

Consider:

```
x = 10y = 20
```

Python's environment keeps track of the names and their associated values.

Conceptually:

| Variable | Value |
| -------- | ----- |
| `x`      | 10    |
| `y`      | 20    |

When Python executes:

```
x = 50
```

The binding for `x` changes.

**Important terminology**

- Variable: A name used to refer to an object.
- Binding: An association between a name and an object.
- Environment: A collection of these name-to-object associations.

## **2. Scope of variables**

**Scope** determines where a variable can be accessed in a program.

Python functions create their own local scope.

Example:

```
x = 10def calculate():    y = 20    print(x)    print(y)calculate()print(x)
```

Output:

```
10
20
10
```

Here:

- `x` is a global variable.
- `y` is a local variable.
- `x` can be accessed inside the function.
- `y` cannot normally be accessed outside the function.

### **Local vs Global variables**

| Local variable                           | Global variable                                          |
| ---------------------------------------- | -------------------------------------------------------- |
| Defined inside a function                | Defined at module level                                  |
| Accessible within its scope              | Accessible throughout the module, subject to scope rules |
| Usually exists during function execution | Exists while its module environment is active            |

### **Important: Local variables can shadow global variables**

```
x = 10def change():    x = 50    print(x)change()print(x)
```

Output:

```
50
10
```

Why?

The assignment `x = 50` creates a local binding inside `change()`. It doesn't change the global `x`.

### **The&#x20;**`global`**&#x20;keyword**

If you want to reassign a global variable inside a function:

```
x = 10def change():    global x    x = 50change()print(x)
```

Output:

```
50
```

**Notebook points:**

- Scope determines where names can be accessed.
- Local variables belong to function scope.
- Global variables belong to module scope.
- Local assignments can shadow global names.
- `global` allows reassignment of a module-level variable.

## **3. Enclosing Scope and LEGB**

Python uses the LEGB rule to resolve variable names.

**LEGB name resolution**

1. **L: Local**

   Inside the current function.
2. **E: Enclosing**

   Inside the enclosing function, when functions are nested.
3. **G: Global**

   At the module level.
4. **B: Built-in**

   Python's built-in names, such as `len()`, `print()` and `sum()`.

Example:

```
x = "global"def outer():    x = "enclosing"    def inner():        x = "local"        print(x)    inner()outer()
```

Output:

```
local
```

Python looks for `x` in the local scope first. It finds it there, so it doesn't need to search further.

**Notebook point:** Python resolves names using Local → Enclosing → Global → Built-in.

## **4. Functions as Objects**

This is the main concept of Lecture 8.

In Python, functions are **first-class objects**.

This means functions can be treated like other objects.

They can be:

1. Assigned to variables.
2. Passed as arguments to other functions.
3. Returned from other functions.

### **4.1 Assigning a function to a variable**

```
def is_even(n):    return n % 2 == 0check = is_evenprint(check(4))
```

Output:

```
True
```

Notice:

```
check = is_even
```

We are assigning the function itself to `check`, not executing it.

Compare:

| Expression           | Meaning                                |
| -------------------- | -------------------------------------- |
| `check = is_even`    | Assign function reference              |
| `check = is_even(4)` | Execute function and assign its result |

This distinction is extremely important.

### **4.2 Passing functions as arguments**

A function can receive another function as an argument.

```
def add(a, b):    return a + bdef multiply(a, b):    return a * bdef calculate(operation, x, y):    return operation(x, y)print(calculate(add, 5, 3))print(calculate(multiply, 5, 3))
```

Output:

```
8
15
```

How does this work?

When we write:

```
calculate(add, 5, 3)
```

- `operation` receives the `add` function.
- `x` receives 5.
- `y` receives 3.
- `operation(x, y)` executes `add(5, 3)`.

A function that accepts or returns another function is called a **higher-order function**.

### **4.3 Returning functions**

Functions can also return other functions.

```
def get_operation():    def add(a, b):        return a + b    return addmy_operation = get_operation()print(my_operation(5, 3))
```

Output:

```
8
```

Here, `get_operation()` returns the `add` function itself.

**Notebook points:**

- Functions are first-class objects in Python.
- Functions can be assigned to variables.
- Functions can be passed as arguments.
- Functions can be returned by other functions.
- Higher-order functions accept or return functions.

[image](https://www.google.com/s2/favicons?domain=https://ocw.mit.edu\&sz=32)

MIT OpenCourseWare+1

## **5. Understanding Function Calls and Environments**

This brings together the first two sections.

Every time Python calls a function, it creates a new local environment (also called a frame).

Consider:

```
def calculate(x):    x = x + 1    return xx = 10result = calculate(x)print(x)print(result)
```

Output:

```
10
11
```

Why doesn't the original `x` become 11?

Because Python creates a separate local binding for the parameter `x` inside `calculate()`.

**Visualizing the environments**

**Global environment**

| Name        | Value    |
| ----------- | -------- |
| `x`         | 10       |
| `result`    | 11       |
| `calculate` | Function |

**Local environment during function execution**

| Name | Value   |
| ---- | ------- |
| `x`  | 10 → 11 |

After the function returns, its local frame is normally discarded. The returned value is assigned to global `result`.

**Important:** Reassigning a parameter doesn't reassign the caller's variable.

This is a key concept for understanding function execution and debugging.

## **6. A few important reminders from the lecture**

### **A. Every function returns something**

If you don't explicitly use `return`, Python returns `None`.

```
def greet():    print("Hello")result = greet()print(result)
```

Output:

```
Hello
None
```

### **B. Code after return doesn't execute**

```
def example():    return 10    print("Hello")
```

The `print()` statement is unreachable because the function has already returned.

### **C. Accessing versus modifying global variables**

```
x = 5def show():    print(x)show()
```

This works because the function only reads the global variable.

But:

```
x = 5def change():    x += 1change()
```

This raises an `UnboundLocalError` because Python treats `x` as local due to the assignment, but it is being read before that local binding has been initialized.

Use `global` if you genuinely need to reassign a module-level variable, although returning values is generally cleaner.

[image](https://www.google.com/s2/favicons?domain=https://ocw.mit.edu\&sz=32)

MIT OpenCourseWare

## **7. What to write in your notebook**

This is your condensed revision sheet.

## **Lecture 8: Quick Revision**

**1. Environments**

- Mapping of names to objects.
- Every function call creates a new local environment.

**2. Scope**

- Determines where variables can be accessed.
- Local variables belong to function scope.
- Global variables belong to module scope.
- Local assignment does not automatically modify a global variable.

**3. First-class functions**

- Functions are objects in Python.
- Can be assigned, passed and returned.

**4. Higher-order functions**

\- Functions that accept or return other functions.

**5. Function calls**

- Arguments are bound to parameters.
- A local frame is created.
- Function executes and returns a result.
- Local frame normally disappears.

**6. Return**

- No explicit return → `None`.
- Code after an executed return is not reached.

## **8. DSA relevance and practice**

| Concept                       | DSA importance |
| ----------------------------- | -------------- |
| Local and global scope        | High           |
| Function environments         | High           |
| Function arguments and return | Very high      |
| Functions as objects          | Medium         |
| Higher-order functions        | Medium         |
| Returning functions           | Low for now    |
| `global` keyword              | Low            |

**Practice these three things:**

1. Predict the output of code involving local and global variables.
2. Trace a function passed as an argument to another function.
3. Write a higher-order function that accepts a function and applies it to a number.

Don't spend hours on complicated scope puzzles.

## **9. Official resources**

- [Lecture 8 slides (PDF)](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec08.pdf?utm_source=chatgpt.com).
- [MIT 6.100L complete lecture playlist](https://learn.mit.edu/c/unit/ocw?resource=13921\&utm_source=chatgpt.com).

## **Alice's final recommendation**

There are two concepts I particularly want you to become comfortable with:

**First:** Understanding what happens to variables when a function is called.

**Second:** Understanding the difference between passing a function and calling a function.

These will help you tremendously when reading Python code, especially callbacks, sorting functions, and other higher-order programming patterns.

You don't need extensive problem-solving practice for this lecture. Understand the concepts, trace a few examples, and move forward. 🚀