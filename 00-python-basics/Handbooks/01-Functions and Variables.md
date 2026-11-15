Here are your CS50P Module 1 notes focusing on **Functions and Variables**.

---

### 1. Functions

A function is a "chunk" of code that performs a specific task. Think of it as a little machine that takes inputs, does something with them, and optionally gives back an output.

* **`print()`**: A built-in function used to output text or values to the screen.
```python
print("Hello, World!")

```


* **`input()`**: A built-in function that prompts the user for input, pausing the program until the user types something and presses Enter. It always returns the input as a **string**.
```python
name = input("What is your name? ")

```


* **`len()`**: Returns the length (number of characters) of a string.
* **`str.strip()`**: Removes leading and trailing whitespace from a string.
* **`str.capitalize()`**: Capitalizes only the first letter of a string.
* **`str.title()`**: Capitalizes the first letter of every word in a string.
* **`str.split()`**: Splits a string into multiple parts (e.g., splitting a full name into first and last names).

---

### 2. Variables

A variable is a container that stores a value in computer memory so you can reference and manipulate it later.

* **Assignment Operator (`=`):** Used to assign a value to a variable. The value on the right is stored in the variable name on the left.
```python
# Assigning a string to a variable
name = "David"

```


* **Naming Conventions:** Variable names should be descriptive, use lowercase letters, and separate words with underscores (`snake_case`), such as `first_name` or `total_cost`.

---

### 3. Data Types

Python handles different kinds of data differently. The core types introduced in Module 1 include:

* **`str` (String):** Textual data enclosed in single (`'`) or double (`"`) quotes.
* **`int` (Integer):** Whole numbers (positive, negative, or zero).
* **`float` (Floating-point number):** Numbers containing a decimal point.

---

### 4. Type Casting (Converting Types)

Because `input()` always returns a string, you often need to convert data types manually using functions like `int()` or `float()`.

```python
# Getting numbers from the user
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

```

---

### 5. Creating Your Own Functions (`def`)

You can define your own custom functions using the `def` keyword.

* **Defining and Calling:**
```python
def hello(to="world"):
    print("Hello,", to)

hello()          # Outputs: Hello, world
hello("Alice")   # Outputs: Hello, Alice

```


* **Scope:** Variables defined inside a function only exist within that function (local scope), unless returned or defined globally.
* **Returning Values (`return`):** Instead of just printing inside a function, you can pass data back using `return`.
```python
def square(n):
    return n * n

result = square(4)  # result is 16

```



---