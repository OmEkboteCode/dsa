# MIT 6.100L, Lecture 7: Decomposition, Abstraction and Functions

### Very Important for Programming • DSA Foundations

Om, this is a particularly important lecture for your programming journey. So far, you've learned how to write programs using variables, conditions, loops, and basic algorithms. Now MIT introduces a way to organize programs so that they remain understandable as they become more complex.

The three central ideas are:

1. **Decomposition**
2. **Abstraction**
3. **Functions and function specifications**

These ideas will follow you throughout DSA, software engineering, research, and practically every serious programming project. Let's build your notes.

---

## 1. Decomposition

### 1.1 What is decomposition?

Imagine you're building a calculator. It needs to:

* Accept numbers.
* Perform addition.
* Perform subtraction.
* Perform multiplication.
* Perform division.
* Display results.

You could write the entire program as one enormous block of code. But that would become difficult to understand, modify, and debug. Instead, divide the program into smaller, independent parts. This is called **decomposition**.

> **Definition:** Decomposition is the process of breaking a complex problem into smaller, self-contained parts that can work together to solve the overall problem.

### 1.2 Example

Suppose you want to calculate the total price of an online purchase. The program needs to:

1. Calculate the price of individual products.
2. Calculate the tax.
3. Calculate the delivery charge.
4. Calculate the final amount.

Instead of writing everything together:

```python
price1 = 100
price2 = 200

subtotal = price1 + price2
tax = subtotal * 0.18
delivery = 40

total = subtotal + tax + delivery

print(total)

```

We can divide the work into smaller functions:

```python
def calculate_subtotal(price1, price2):
  return price1 + price2


def calculate_tax(subtotal):
  return subtotal * 0.18


def calculate_total(subtotal, tax, delivery):
  return subtotal + tax + delivery

```

Now each function has a specific responsibility.

### 1.3 Why is decomposition useful?

* **Understandability:** Smaller pieces are easier to understand.
* **Debugging:** You can isolate errors to individual parts.
* **Reusability:** You can reuse a function in other programs.
* **Maintainability:** Changes to one part need not affect everything else.
* **Collaboration:** Different programmers can work on different components.

> **What to write in your notebook — Decomposition**
> * Breaking a complex problem into smaller, self-contained parts.
> * Each part performs a specific task.
> * Parts combine to solve the overall problem.
> 
> 
> **Benefits:**
> 1. Understandability
> 2. Reusability
> 3. Maintainability
> 4. Easier debugging
> 5. Modularity
> 
> 

---

## 2. Abstraction

This is arguably the most important conceptual idea in this lecture.

### 2.1 Understanding abstraction through an example

Think about using a smartphone. When you open your camera application, you simply:

1. Open the camera.
2. Point it at something.
3. Press the capture button.

You don't need to understand:

* How the camera sensor works.
* How light is converted into electrical signals.
* How image processing happens.
* How pixels are stored in memory.
* How the image file is encoded.

You interact with the camera through a simple interface without needing to understand its internal implementation. This is **abstraction**.

> **Definition:** Abstraction is the process of hiding unnecessary implementation details and exposing only the essential functionality.

### 2.2 Abstraction in programming

Consider:

```python
def calculate_area(radius):
  return 3.14 * radius**2

```

Now imagine using this function:

```python
area = calculate_area(5)
print(area)

```

As someone using this function, you only need to know:

* What input it accepts.
* What output it produces.
* What the function does.

You don't need to know how the calculation is implemented every time you use it. The implementation is hidden behind the function interface.

### 2.3 What is a black box?

MIT uses the concept of a **black box** to explain abstraction. A black box can be understood through three things:

1. **Input:** What goes inside?
2. **Output:** What comes out?
3. **Relationship:** How does the output relate to the input?

You don't need to know the internal implementation to use it. For example:

```python
calculate_area(5)

```

You know that the function receives `5` and returns the area of a circle with radius `5`. You can use it without examining its internal code.

### 2.4 Decomposition vs abstraction

These two concepts are related but different:

| Decomposition | Abstraction |
| --- | --- |
| Breaks a complex problem into smaller parts | Hides unnecessary implementation details |
| Focuses on how to organize a program | Focuses on how to interact with a component |
| Makes problems manageable | Makes complexity easier to handle |

**Remember:**

* **Decomposition** helps us *divide* complexity.
* **Abstraction** helps us *hide* complexity.

> **What to write in your notebook — Abstraction**
> * Hides unnecessary implementation details.
> * Exposes essential functionality through an interface.
> * Allows users to interact with a component without understanding its internal implementation.
> 
> 
> **Black box model:**
> 1. Input
> 2. Output
> 3. Relationship between input and output
> 
> 
> **Difference:**
> * Decomposition = divide complexity.
> * Abstraction = hide complexity.
> 
> 

---

## 3. Functions

Now we arrive at the practical implementation of decomposition and abstraction.

### 3.1 What is a function?

A **function** is a reusable block of code designed to perform a particular task. Instead of writing the same instructions repeatedly, we define them once and call the function whenever needed.

Example:

```python
def greet():
  print("Hello, Om!")


greet()
greet()
greet()

```

Output:

```text
Hello, Om!
Hello, Om!
Hello, Om!

```

We wrote the function once and reused it three times.

### 3.2 Function syntax

```python
def function_name(parameters):
  # function body
  return result

```

Let's understand each component:

| Component | Meaning |
| --- | --- |
| `def` | Keyword used to define a function |
| `function_name` | Name of the function |
| `parameters` | Inputs accepted by the function |
| Function body | Instructions executed when called |
| `return` | Sends a result back to the caller |

A function can accept zero or more parameters.

### 3.3 Defining versus calling a function

This is a particularly important distinction. Consider:

```python
def is_even(i):
  return i % 2 == 0

```

Have we checked whether a number is even? **No!** We have only defined the function. Python now knows that a function named `is_even` exists. To execute it, we must call it:

```python
is_even(8)

```

Now the function actually runs.

* **Function definition** (`def is_even(i): ...`): Creates the function.
* **Function call** (`is_even(8)`): Executes the function using `8` as its input.

### 3.4 Parameters and arguments

Consider:

```python
def square(number):
  return number**2


square(5)

```

Here:

* `number` is a **parameter**.
* `5` is an **argument**.
* **Parameter:** A variable listed in the function definition that receives an input.
* **Argument:** The actual value supplied when calling the function.

This distinction is worth remembering because you'll encounter it constantly in Python and JavaScript.

### 3.5 What happens when a function is called?

Let's examine:

```python
def is_even(i):
  return i % 2 == 0


result = is_even(3)

```

Think of Python executing this in stages:

1. **Step 1: Function call** — `is_even(3)` (Python takes the argument `3`).
2. **Step 2: Parameter receives the argument** — `i = 3`.
3. **Step 3: Execute the function body** — `return 3 % 2 == 0`.
4. **Step 4: Evaluate the expression** — `return False`.
5. **Step 5: Replace the function call with its return value** — `result = False`.

$$\text{Function call} \longrightarrow \text{return value}$$

MIT emphasizes that a function call behaves like an expression: its result is the value returned by the function.

### 3.6 The importance of `return`

Consider these two functions:

```python
def add_a(a, b):
  return a + b


def add_b(a, b):
  print(a + b)

```

They might look similar, but they behave differently:

```python
x = add_a(5, 3)
y = add_b(5, 3)

print(x)
print(y)

```

Output:

```text
8
8
None

```

Why?

* `return` sends a value back to the caller.
* `print()` displays something on the screen.
* A function without an explicit `return` value returns `None`.

This distinction is extremely important for DSA. Most DSA problems expect your function to return an answer, not merely print it.

> **What to write in your notebook — Functions**
> * Reusable blocks of code that perform specific tasks.
> * Created using `def`.
> * Execute only when called.
> * Accept zero or more parameters.
> * Can return a value using `return`.
> 
> 
> **Important terminology:**
> * Parameter = variable in function definition.
> * Argument = actual value passed during a function call.
> * `return` = sends a value back.
> * `print()` = displays a value.
> 
> 
> **Execution model:**
> Function call $\rightarrow$ arguments assigned to parameters $\rightarrow$ body executes $\rightarrow$ return value replaces the call.

---

## 4. Function Specifications and Docstrings

This is another important concept from Lecture 7.

### 4.1 What is a function specification?

Before implementing a function, we should clearly define what it is supposed to do. Consider:

```python
def is_even(i):
  """
    Input: i, a positive integer.
    Returns True if i is even, otherwise False.
    """
  return i % 2 == 0

```

The specification tells us:

* What input is expected.
* What output is expected.
* What conditions the input must satisfy.

It describes the function's behaviour without requiring the reader to understand its implementation.

### 4.2 What is a docstring?

A **docstring** is a string written inside a function, usually immediately after its definition, describing what the function does.

Example:

```python
def calculate_area(radius):
  """
    Input: radius, a positive number.
    Returns the area of a circle.
    """
  return 3.14 * radius**2

```

Notice that the docstring explains the function's contract.

### 4.3 Function as a contract

Think of a function specification as an agreement between two people:

* **The programmer promises:** *"If you provide valid inputs according to my specification, I'll produce the promised output."*
* **The user of the function agrees to:**
* Supply valid inputs.
* Use the function according to its specification.
* Rely on its documented behaviour.



This is called a **contract**. MIT explains that specifications describe the relationship between valid inputs and expected outputs, including any specified side effects.

> **What to write in your notebook — Function specifications**
> A specification describes the expected behaviour of a function.
> Includes:
> 1. Input requirements.
> 2. Expected output.
> 3. Conditions the input must satisfy.
> 4. Relevant side effects, if any.
> 
> 
> * **Docstring:** A string describing the function's specification.
> * **Contract:** Agreement between the function's programmer and its user.
> 
> 

---

## 5. How to approach writing a function

This is one of the most valuable parts of Lecture 7. MIT demonstrates that you shouldn't immediately start writing code when given a problem. Instead, use a systematic process.

### Example: Sum of odd numbers

Suppose we want to write:

```python
def sum_odd(a, b):
  # implementation
  return sum_of_odds

```

The function should calculate the sum of all odd integers between `a` and `b`, including both endpoints. Suppose `sum_odd(2, 7)` — expected answer:

$$3+5+7=15$$

How should we approach this?

* **Step 1: Understand the problem.** What are we trying to calculate? The sum of odd integers in a given interval.
* **Step 2: Identify inputs and outputs.** Inputs: `a` and `b`. Output: Sum of odd integers.
* **Step 3: Work through an example on paper.** For `a = 2, b = 7`:

| Number | Odd? | Include in sum? |
| --- | --- | --- |
| 2 | No | No |
| 3 | Yes | Yes |
| 4 | No | No |
| 5 | Yes | Yes |
| 6 | No | No |
| 7 | Yes | Yes |

Expected result: $3+5+7=15$.

* **Step 4: Find a simpler related problem.** Before solving the odd-number problem, consider a simpler problem: *What if we wanted to sum all numbers between `a` and `b`?* This is easier because we only need a loop and an accumulator.
* **Step 5: Choose the overall structure.** We can use a `for` loop or a `while` loop.
* **Step 6: Add the additional condition.** Now include only numbers satisfying `i % 2 == 1`.
* **Step 7: Test the implementation.** Try different inputs and compare the output with the expected result.

The final implementation:

```python
def sum_odd(a, b):
  sum_of_odds = 0

  for i in range(a, b + 1):
    if i % 2 == 1:
      sum_of_odds += i

  return sum_of_odds

```

Notice the `b + 1`. Python's `range()` excludes its ending value, so we add one to include `b`.

### The important problem-solving principles

MIT highlights three particularly valuable ideas:

1. **Paper first:** Work through a small example before coding.
2. **Solve a simpler problem first:** Establish the basic structure, then add functionality.
3. **Test frequently:** Use test cases and print statements to investigate unexpected results.

> **What to write in your notebook — Function problem-solving workflow**
> 1. Understand the problem.
> 2. Identify inputs and outputs.
> 3. Write a specification.
> 4. Work through a small example manually.
> 5. Find a simpler related problem.
> 6. Choose the overall program structure.
> 7. Implement the solution.
> 8. Test with multiple inputs.
> 9. Debug if necessary.
> 
> 

---

## 6. Debugging and Testing

MIT also introduces an important programming habit: **test your code frequently**. Suppose your function produces an unexpected result. Instead of randomly changing the code, insert `print` statements to observe what's happening.

Example:

```python
def sum_numbers(a, b):
  total = 0

  for i in range(a, b + 1):
    total += i
    print(i, total)

  return total

```

The `print` statement helps you observe:

* Current iteration.
* Current value of the accumulator.
* How the state changes after each iteration.

This is called **debugging using print statements**. Another useful technique is testing with small examples before trying complicated inputs.

> **What to write in your notebook — Debugging & Testing**
> * Test functions using different inputs.
> * Compare actual and expected outputs.
> * Use `print` statements to inspect intermediate values.
> * Fix the underlying cause rather than randomly changing code.
> 
> 

---

## 7. Complete Lecture Summary

Here is your revision sheet:

**Lecture 7: Key Concepts**

1. **Decomposition:** Break complex problems into smaller, self-contained parts. Improves organization, reuse, and maintainability.
2. **Abstraction:** Hide implementation details. Expose essential functionality. Black box = input, output, and their relationship.
3. **Functions:** Reusable blocks of code. Defined using `def`. Executed through function calls. Accept parameters and return results.
4. **Function specifications:** Describe expected function behaviour. Include input requirements and expected output. Docstrings document specifications. Specifications act as contracts.
5. **Function execution:** Arguments are assigned to parameters. Function body executes. Return value replaces the function call.
6. **Problem-solving:** Understand before coding. Work through examples on paper. Solve simpler problems first. Test frequently. Debug using `print` statements.

---

## 8. What is important for DSA?

This lecture deserves more attention than Lectures 5 and 6's numerical approximation material.

| Concept | DSA importance | Recommendation |
| --- | --- | --- |
| Functions and syntax | Very high | Master |
| Parameters and arguments | Very high | Master |
| Return statements | Very high | Master |
| Function calls and execution | Very high | Master |
| Specifications | Very high | Master |
| Decomposition | Very high | Master |
| Abstraction | Very high | Master |
| Paper-first problem solving | Very high | Develop habit |
| Docstring formatting | Medium | Understand |
| Print-based debugging | High | Practise |

---

## 9. What should you practise?

Unlike Lecture 5, I don't recommend skipping most of the implementation exercises here. Functions are fundamental to virtually every DSA problem. However, you don't need dozens of exercises. I'd recommend these four:

* $\square$ Implement `is_even(i)`, returning `True` or `False`.
* $\square$ Implement `div_by(n, d)`, checking whether `d` divides `n` evenly.
* $\square$ Implement `sum_odd(a, b)`, summing odd integers in an inclusive interval.
* $\square$ Implement `is_palindrome(s)`, checking whether a string reads identically forward and backward.

My recommendation is to implement these independently, without looking at solutions. The palindrome exercise is especially useful for practising strings and conditions.

---

## 10. What I want you to take away from Lecture 7

There is a deeper connection between these three concepts:

* **Decomposition:** Divide a complex problem into smaller parts.
* **Abstraction:** Hide unnecessary details behind clear interfaces.
* **Functions:** Implement reusable, self-contained computational units.

These are not merely Python concepts. They are foundational principles of software design.

---

## 11. Official lecture resources

* Watch MIT Lecture 7: Decomposition, Abstraction and Functions (available in your $\U0001f4d4$ [Python Main](https://gemini.google.com/notebook/f6430f22-5341-40c5-94ae-c19cd61318c9) notebook)
* Lecture 7 slides (PDF)
* Lecture 7 finger exercise solutions — try the exercises before opening the solutions.

> **Alice's recommendation 📚**
> For your notebook, aim for approximately **3–4 A4 pages**:
> * **Page 1:** Decomposition and abstraction
> * **Page 2:** Functions, parameters, arguments, and `return`
> * **Page 3:** Specifications, docstrings, and contracts
> * **Page 4:** Problem-solving workflow and debugging
> 
> 
> **Suggested study time:** 1.5–2 hours, including the four exercises.

One important thing: I want you to become exceptionally comfortable with reading function calls. When you encounter:

```python
result = calculate_total(100, 200)

```

Your mind should naturally recognize:

* A function named `calculate_total`.
* Two arguments: `100` and `200`.
* A function call that executes its body.
* A returned value assigned to `result`.

Practise reading code this way until it becomes automatic. This will pay enormous dividends when we reach recursion, data structures, and eventually more complex algorithms. Lecture 7 is worth mastering—don't rush this one. 🚀