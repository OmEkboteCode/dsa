# **MIT 6.100L, Lecture 5: Floats and Approximation Methods**



MIT 6.100L · Fall 2022

Lecture notes



Om, this is an important lecture because it introduces a fundamental idea in computing: **computers do not represent and calculate every number with perfect mathematical precision.**

Until now, you've mostly worked with Python as though its numbers behave exactly like numbers in mathematics. Lecture 5 challenges that assumption.

We'll organize your notes into three layers:

1. **Conceptual understanding:** What you must genuinely understand.
2. **Notebook material:** What is worth writing down for future revision.
3. **Code experiments:** Small experiments that make the concepts intuitive.

Don't transcribe the entire lecture. Your notebook should become a compact reference that helps you reason about numerical computation.

## **1. Floating-point numbers**

### **1.1 Why do we need floats?**

Computers represent information using binary digits (bits): `0` and `1`.

Integers are relatively straightforward to represent in binary.

For example:

\\[ 19\_{10}=10011_2 \\]

But what about decimal fractions?

Consider:

- `0.5`
- `0.25`
- `0.125`
- `0.1`

Some fractions have exact, finite binary representations, while others have infinite binary representations.

### **1.2 Understanding fractional binary representation**

In decimal, each position after the decimal point represents a negative power of 10.

For example:

\\[ 0.375 = 3(10^{-1})+7(10^{-2})+5(10^{-3}) \\]

Binary works similarly, except it uses powers of 2.

| Binary position | Value               |
| --------------- | ------------------- |
| First           | \\(2^{-1}=0.5\\)    |
| Second          | \\(2^{-2}=0.25\\)   |
| Third           | \\(2^{-3}=0.125\\)  |
| Fourth          | \\(2^{-4}=0.0625\\) |

Therefore:

\\[ 0.375 = 0.25+0.125 \\]

\\[ \boxed{0.375\_{10}=0.011_2} \\]

**Why?**

\\[ 0.011_2 = 0(0.5)+1(0.25)+1(0.125) \\]

The result is exactly 0.375.

### **1.3 Why can't we represent 0.1 exactly?**

Consider:

\\[ 0.1\_{10} \\]

Its binary representation is:

\\[ 0.000110011001100110011\ldots_2 \\]

Notice something important: the sequence continues indefinitely.

There is no finite binary representation for this number.

Computers have finite memory, so they cannot store an infinite sequence of bits.

They store a rounded approximation instead.

**This is the fundamental reason floating-point errors exist.**

### **What to write in your notebook**

**Floating-point representation**

- Computers represent numbers using binary (base 2).
- Binary fractions use negative powers of 2.
- Some fractions, such as 0.375, have exact finite binary representations.
- Some fractions, such as 0.1, have infinite binary representations.
- Computers have finite storage, so they approximate such numbers.
- This introduces floating-point representation errors.

### **1.4 How are floating-point numbers stored?**

MIT introduces floating-point representation using two components:

1. Significant digits (significand).
2. Base-2 exponent.

Think of scientific notation.

For example:

\\[ 125\times 2^{-2}=31.25 \\]

The exponent determines how far the binary point shifts.

Examples:

| Significant digits | Exponent | Decimal result |
| ------------------ | -------- | -------------- |
| 1                  | 1        | 2              |
| 1                  | -1       | 0.5            |
| 125                | -2       | 31.25          |

This is why the name *floating point* is used: the position of the point can shift relative to the significant digits.

**Important distinction:** These are simplified teaching examples. Real floating-point formats use a sign, significand and exponent with a specific bit layout. Python's ordinary `float` generally uses IEEE 754 binary64 (64 bits).

### **What to write in your notebook**

- Floating-point numbers represent values using a significand and exponent.
- The exponent controls the position of the binary point.
- Finite bits mean some real numbers must be approximated.
- Precision refers to how accurately a number can be represented.

## **2. Floating-point errors in Python**

This is one of the most important practical lessons.

Consider:

```
x = 0for i in range(10):    x += 0.1print(x == 1)print(x)
```

Expected mathematical result:

\\[ 10\times 0.1=1 \\]

But Python produces approximately:

```
False
0.9999999999999999
```

Why?

Because `0.1` is not represented exactly in binary.

Every addition operates on its stored approximation. Repeated operations can accumulate small errors.

Now compare this:

```
x = 0for i in range(10):    x += 0.125print(x == 1.25)
```

Output:

```
True
```

Why?

Because 0.125 has an exact binary representation:

\\[ 0.125=0.001_2 \\]

**The important lesson:** Mathematically equivalent operations do not necessarily produce identical floating-point results.

### **2.1 Why should we avoid&#x20;**`==`**&#x20;with floats?**

Suppose you want to check whether two floating-point values are equal.

Instead of:

```
a == b
```

You can check whether their difference is sufficiently small:

```
epsilon = 0.00001if abs(a - b) < epsilon:    print("Close enough")
```

Here:

- `abs()` calculates absolute value.
- `epsilon` represents an acceptable error tolerance.
- A smaller epsilon means stricter accuracy.

Mathematically:

\\[ \boxed{|a-b|<\epsilon} \\]

This means the difference between the two values is smaller than the permitted tolerance.

### **What to write in your notebook**

**Floating-point comparison**

Never blindly depend on exact equality (`==`) when comparing calculated floating-point values.

Instead, use a tolerance:

\\[ |a-b|<\epsilon \\]

Where:

- \\(a,b\\): values being compared.
- \\(\epsilon\\): acceptable error tolerance.
- `abs()`: absolute difference.

**Example:**

```
epsilon = 0.00001abs(a - b) < epsilon
```

## **3. Approximation methods**

Now we move to the second half of the lecture.

This is where the lecture becomes particularly interesting from an algorithmic perspective.

### **3.1 The limitation of guess-and-check**

Recall the previous lecture.

You learned guess-and-check:

1. Generate a possible answer.
2. Check whether it satisfies the condition.
3. If not, generate another answer.
4. Repeat.

This works when the possible answers form an enumerable set.

For example, finding the square root of 36:

\\[ 1,2,3,4,5,6,\ldots \\]

Eventually, you find 6.

But suppose we want:

\\[ \sqrt{5} \\]

There is no integer answer.

The actual answer is approximately:

\\[ 2.2360679\ldots \\]

If we only check integers, we will never find the answer.

We need a different approach.

### **3.2 The central idea: Good enough**

Instead of demanding an exact answer, we search for an answer sufficiently close to the actual answer.

This is called an **approximation method**.

For square roots, suppose we want to approximate:

\\[ \sqrt{x} \\]

We need to find a number \\(g\\) such that:

\\[ g^2\approx x \\]

How close should it be?

We introduce a parameter called epsilon.

\\[ \boxed{|g^2-x|<\epsilon} \\]

This is our stopping condition.

For example:

- \\(x=25\\)
- \\(\epsilon=0.01\\)

We want a guess whose square differs from 25 by less than 0.01.

Notice that we are not directly comparing the guess with the square root. We are checking whether its square is sufficiently close to the target number.

### **3.3 Two important parameters**

The approximation algorithm has two parameters.

**Parameter 1: Epsilon (**\\(\epsilon\\)**)**

Accuracy

Determines how close the answer must be to the desired result.

Example:

- `epsilon = 0.1`: less strict.
- `epsilon = 0.01`: more strict.
- `epsilon = 0.0001`: even more strict.

**Parameter 2: Increment**

Step size

Determines how much we change our guess in each iteration.

Example:

- `increment = 0.1`
- `increment = 0.01`
- `increment = 0.001`

Smaller increments allow finer searching.

**The trade-off:**

| Change             | Accuracy                   | Speed             |
| ------------------ | -------------------------- | ----------------- |
| Decrease epsilon   | Increases                  | Usually decreases |
| Increase epsilon   | Decreases                  | Usually increases |
| Decrease increment | Improves search resolution | Decreases         |
| Increase increment | Reduces search resolution  | Increases         |

Remember: epsilon and increment are different things.

- Epsilon determines when to stop.
- Increment determines how far to move.

### **What to write in your notebook**

**Approximation method**

- Finds an answer sufficiently close to the actual answer.
- Useful when an exact answer is unavailable or impractical to find.
- Uses small increments to explore possible answers.
- Stops when the answer satisfies an acceptable error tolerance.

**Parameters:**

1. Epsilon: acceptable error.
2. Increment: change in guess per iteration.

**Trade-off:** Greater accuracy can require more computation.

## **4. Implementing an approximation algorithm**

Let's understand the actual Python implementation.

MIT uses the following example:

```
x = 36epsilon = 0.01num_guesses = 0guess = 0.0increment = 0.0001while abs(guess**2 - x) >= epsilon:    guess += increment    num_guesses += 1print('num_guesses =', num_guesses)print(guess, 'is close to square root of', x)
```

### **4.1 Understand the code line by line**

| Code                 | Meaning                           |
| -------------------- | --------------------------------- |
| `x = 36`             | Number whose square root we want  |
| `epsilon = 0.01`     | Acceptable error                  |
| `num_guesses = 0`    | Counts iterations                 |
| `guess = 0.0`        | Initial guess                     |
| `increment = 0.0001` | Amount added each time            |
| `while ...`          | Continue while error is too large |
| `guess += increment` | Increase guess                    |
| `num_guesses += 1`   | Count the iteration               |

Let's mentally execute the loop.

**How the algorithm searches**

| **Guess** | **Guess squared** |
| --------- | ----------------- |
| 0         | 0                 |
| 1         | 1                 |
| 2         | 4                 |
| 3         | 9                 |
| 4         | 16                |
| 5         | 25                |
| 6         | 36                |

Simplified illustration using whole-number guesses. MIT's actual implementation uses increments of 0.0001.

Eventually, the algorithm reaches a guess sufficiently close to 6.

However, there is a problem.

### **4.2 The overshooting problem**

Suppose:

```
x = 54321epsilon = 0.01increment = 0.0001
```

The algorithm increases its guess continuously.

But imagine the following:

- Current guess is slightly below the square root.
- The next increment moves it slightly above the square root.
- The squared value is now larger than the target.
- Further increments make the error larger again.

The algorithm has **overshot** the acceptable region.

It may continue indefinitely because the error will not become smaller again.

This is a classic algorithm-design problem: the loop's stopping condition does not account for every possible exit situation.

### **4.3 Fixing the overshooting problem**

MIT modifies the loop:

```
while abs(guess**2 - x) >= epsilon and guess**2 <= x:    guess += increment    num_guesses += 1
```

There are now two conditions.

1. The answer is not sufficiently close.
2. The guess has not exceeded the target when squared.

The loop continues only while both conditions are true.

After the loop:

```
if abs(guess**2 - x) >= epsilon:    print('Failed on square root of', x)else:    print(guess, 'is close to square root of', x)
```

Why check again?

Because the loop might have terminated for either reason:

- We found a sufficiently accurate answer.
- We overshot the target.

These are not equivalent outcomes!

### **What to write in your notebook**

**Overshooting problem**

- An increment can jump over the acceptable error region.
- The algorithm may continue indefinitely if it only checks the error condition.
- Add a boundary condition to prevent searching beyond the reasonable range.
- After the loop, verify whether it stopped because it found an answer or because it overshot.

**Key lesson:** A loop needs carefully designed termination conditions.

## **5. Improving accuracy and performance**

MIT then changes the increment:

```
increment = 0.00001
```

Previously:

```
increment = 0.0001
```

The new increment is ten times smaller.

This means the algorithm checks more possible values.

For the example with \\(x=54321\\), it can now find a sufficiently accurate approximation.

But there is a cost.

| Increment | Search behaviour                         |
| --------- | ---------------------------------------- |
| 0.001     | Larger jumps, fewer iterations           |
| 0.0001    | Smaller jumps, more iterations           |
| 0.00001   | Even smaller jumps, many more iterations |

This leads to a fundamental principle in algorithm design:

**Accuracy and computational efficiency can compete with each other.**

You cannot automatically assume that making an algorithm more accurate makes it better. You must consider the computational cost.

### **Write this down**

- Smaller increments improve search resolution.
- Smaller increments increase the number of iterations.
- Larger increments may overshoot the answer.
- Algorithm design involves balancing accuracy and efficiency.

## **6. Complete lecture summary**

This is the most important section to retain in your notebook.

**Lecture 5: Key takeaways**

**A. Floating-point representation**

- Computers use binary representation.
- Some decimal fractions have infinite binary expansions.
- Finite memory requires approximation.
- Floating-point operations can introduce small errors.

**B. Comparing floats**

- Avoid relying on `==` for calculated floating-point values.
- Use epsilon-based comparisons.
- Understand that displayed values may be rounded.

**C. Approximation algorithms**

- Find sufficiently accurate answers instead of demanding exact answers.
- Use incremental searching.
- Epsilon controls acceptable error.
- Increment controls step size.

**D. Algorithm design**

- Account for overshooting.
- Design proper loop termination conditions.
- Balance accuracy against computational efficiency.

## **7. What you should understand versus what you should memorize**

This distinction is important. I don't want you filling pages with information that you could understand in two minutes.

| Topic                            | Priority | What to do                   |
| -------------------------------- | -------- | ---------------------------- |
| Binary fractions                 | High     | Understand and write         |
| Why 0.1 is inexact               | High     | Understand deeply            |
| Floating-point representation    | High     | Understand and write         |
| Epsilon                          | High     | Memorize meaning and formula |
| Increment                        | High     | Understand                   |
| Approximation algorithm          | High     | Trace and implement          |
| Overshooting                     | High     | Understand the failure       |
| Loop termination                 | High     | Learn the reasoning          |
| Every binary conversion exercise | Low      | Practice selectively         |

## **8. Code-reading laboratory**

Since your objective is to become fluent at reading code, let's use this lecture to train that ability.

Take this expression:

```
while abs(guess**2 - x) >= epsilon:
```

An experienced programmer mentally reads it in chunks:

1. `guess**2`: square the current guess.
2. `guess**2 - x`: calculate the difference from the target.
3. `abs(...)`: remove the sign of that difference.
4. `>= epsilon`: check whether the error is still too large.
5. `while`: repeat while that condition remains true.

Read it aloud:

> While the absolute difference between the square of my guess and the target is greater than or equal to epsilon, keep searching.

This is the kind of fluency we want to develop.

## **9. Test your understanding**

Don't immediately look up the answers. Try reasoning through these.

**Lecture 5 knowledge check**

0/4 answered

**1. Why does Python sometimes produce 0.9999999999999999 instead of 1.0?**

Python uses decimal arithmetic

Some decimal fractions cannot be represented exactly in binary

Python rounds every calculation to an integer

**2. What does epsilon control?**

How much the guess changes

How many variables are created

How close the result must be to the target

**3. What happens when we decrease the increment?**

The search becomes finer but generally slower

The search becomes faster and less accurate

The algorithm stops immediately

**4. Why did MIT add guess\*\*2 <= x to the while condition?**

To make the guess negative

To prevent the search from continuing after overshooting

To increase epsilon

Check my understanding

## **10. One additional exercise from MIT**

The Lecture 5 finger exercise asks you to print the characters at even indices of a string.

For example:

```
my_str = "abcdefg"
```

Expected output:

```
aceg
```

Try solving it yourself. It reinforces string indexing and iteration, which are useful foundations for DSA.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://ocw.mit.edu\&sz=32)

MIT OpenCourseWare



## **11. Official lecture resources**

- [Watch MIT 6.100L Lecture 5](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/resources/6100l-lecture-5-multi_mp4/?utm_source=chatgpt.com).
- [Download Lecture 5 slides (PDF)](https://www.ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec05.pdf?utm_source=chatgpt.com).
- [Lecture transcript](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/1sdzlNzf_U9Dl1VICMcDzaSFH3WDS2W3x_transcript.pdf?utm_source=chatgpt.com).

The slides are particularly useful for revising the diagrams and tracing the approximation algorithm.&#x20;

[image](https://www.google.com/s2/favicons?domain=https://www.ocw.mit.edu\&sz=32)

MIT OpenCourseWare+1



## **Alice's recommendation for your notebook 📓**

Keep Lecture 5 to approximately **3–4 handwritten A4 pages**.

| Page | Contents                                           |
| ---- | -------------------------------------------------- |
| 1    | Binary fractions and floating-point representation |
| 2    | Floating-point errors, epsilon and comparisons     |
| 3    | Approximation algorithm and its parameters         |
| 4    | Python implementation, overshooting and lessons    |

One final thought: **don't confuse learning an algorithm with memorizing its code.**

For this lecture, I want you to be able to explain three things without looking at your notes:

1. Why can a computer fail to represent 0.1 exactly?
2. Why do we use epsilon instead of exact equality?
3. Why can an approximation algorithm run forever if we don't handle overshooting?

If you can explain those three from first principles, you've learned the heart of Lecture 5.

And there's a lovely continuation in Lecture 6: MIT will introduce faster approximation techniques, including bisection search and Newton-Raphson. That's where the algorithmic efficiency discussion gets even more interesting. 🚀