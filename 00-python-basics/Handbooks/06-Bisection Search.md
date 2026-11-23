# MIT 6.100L, Lecture 6: Bisection Search

### DSA Foundation • Lecture Notes

This lecture is particularly relevant to your DSA preparation, Om. It introduces **Bisection Search**, an algorithmic technique that dramatically reduces the number of guesses needed to find an answer.

Unlike Lecture 5, I recommend paying closer attention to the problem-solving technique here. Bisection search is closely related to **binary search**, one of the fundamental algorithms in DSA.

We'll follow our usual approach:

1. Understand the concepts.
2. Study the algorithm and its implementation.
3. Identify what deserves space in your notebook.
4. Separate essential practice from exercises you can skip.

---

## 1. Bisection Search

### 1.1 The problem with approximation methods

In Lecture 5, we used incremental search to approximate square roots. For example, finding:

$$\sqrt{25}=5$$

We started at zero and repeatedly increased our guess. But imagine finding:

$$\sqrt{54321}$$

If our increment is `0.00001`, we need a huge number of iterations. Can we do better?

Yes. Instead of checking every possible value, we can **eliminate half of the search space after every guess**. This is the central idea behind **Bisection Search**.

### 1.2 Understanding the intuition

Imagine you're searching for a student in a classroom where everyone is seated alphabetically. There are 100 students. Instead of asking each student individually:

1. Ask the student sitting in the middle.
2. If the name you're searching for comes before theirs alphabetically, eliminate the second half.
3. Otherwise, eliminate the first half.
4. Repeat with the remaining half.

Each guess eliminates approximately half of the remaining possibilities. That's Bisection Search.

### 1.3 Applying it to square roots

Suppose we want:

$$\sqrt{25}$$

We know that the answer lies between `0` and `25`. Therefore:

$$low=0,\qquad high=25$$

* **Step 1: Find the midpoint.**

$$guess=\frac{low+high}{2}$$

$$guess=\frac{0+25}{2}=12.5$$

Check:

$$12.5^2=156.25$$

This is greater than `25`. Our guess is too large. Therefore, we eliminate the upper half:

$$high=12.5$$

* **Step 2: Find the new midpoint.**

$$guess=\frac{0+12.5}{2}=6.25$$

Check:

$$6.25^2=39.0625$$

Still too large. So:

$$high=6.25$$

* **Step 3: Find the next midpoint.**

$$guess=\frac{0+6.25}{2}=3.125$$

Check:

$$3.125^2=9.765625$$

This is smaller than `25`. Our guess is too small. So:

$$low=3.125$$

We continue until the answer is sufficiently accurate.

### 1.4 The fundamental rule

For square-root approximation:

| Condition | Meaning | Action |
| --- | --- | --- |
| $guess^2>x$ | Guess too large | Reduce `high` |
| $guess^2<x$ | Guess too small | Increase `low` |
| $\Vert{}guess^2-x\Vert{}<\epsilon$ | Accurate enough | Stop |

**The most important idea:** Every iteration reduces the search space by half.

> **What to write in your notebook — Bisection Search**
> * An efficient search technique that repeatedly divides a search interval into two halves.
> * Requires an ordered search space.
> * Requires the ability to determine whether a guess is too high or too low.
> * Eliminates half of the remaining search space in each iteration.
> 
> 
> **Midpoint:**
> $$mid=\frac{low+high}{2}$$
> 
> 
> **For square roots:**
> * If $mid^2>x$, set `high = mid`.
> * If $mid^2<x$, set `low = mid`.
> * Stop when $\vert{}mid^2-x\vert{}<\epsilon$.
> 
> 

---

## 2. Implementing Bisection Search in Python

Let's translate the reasoning into code.

```python
x = 25
epsilon = 0.01

low = 0
high = x

guess = (low + high) / 2

while abs(guess**2 - x) >= epsilon:

  if guess**2 < x:
    low = guess

  else:
    high = guess

  guess = (low + high) / 2

print("Square root is approximately", guess)

```

### Understanding the implementation

| Code | Purpose |
| --- | --- |
| `low = 0` | Lower boundary |
| `high = x` | Upper boundary |
| `(low + high) / 2` | Calculate midpoint |
| `abs(guess**2 - x)` | Calculate approximation error |
| `guess**2 < x` | Check whether guess is too small |
| `low = guess` | Discard lower half |
| `high = guess` | Discard upper half |

### Read the while loop aloud

```python
while abs(guess**2 - x) >= epsilon:

```

*While the difference between the square of my guess and the target is greater than or equal to the acceptable error, keep searching.*

This is the same stopping condition you encountered in Lecture 5. The difference is how we generate the next guess:

* **Lecture 5:** Add a fixed increment.
* **Lecture 6:** Calculate the midpoint of the remaining interval.

### 2.1 Why is Bisection Search faster?

Consider searching through `1,000` possible values. With a sequential search, you might need to examine up to `1,000` values. With Bisection Search:

| Iteration | Remaining search space |
| --- | --- |
| 0 | 1,000 |
| 1 | 500 |
| 2 | 250 |
| 3 | 125 |
| 4 | 63 |
| 5 | 32 |
| 6 | 16 |
| 7 | 8 |
| 8 | 4 |
| 9 | 2 |
| 10 | 1 |

Approximately `10` divisions are sufficient to isolate one value. This is the foundation of logarithmic time complexity:

$$O(\log n)$$

Compare:

* Linear search: $O(n)$
* Binary search: $O(\log n)$

This is extremely important for DSA.

---

## 3. When can we use Bisection Search?

This is an important conceptual question. Can we use Bisection Search to find a number in any collection? **No.** It relies on two important properties.

### Property 1: Ordered search space

We must have an order that allows us to divide the search space meaningfully. For example:

```python
numbers = [2, 5, 8, 12, 16, 20, 25]

```

This is sorted.

### Property 2: We must know which direction to search

After checking the midpoint, we must be able to determine whether the answer lies to its left or right. For example, when searching for `16`:

* Midpoint is `12`.
* `16` is greater than `12`.
* Eliminate everything at or below `12`.
* Search the right half.

This is why binary search works on sorted arrays.

### Requirements for Bisection Search

1. An ordered search space.
2. A way to determine which half can be eliminated.
3. A valid boundary or interval.
4. A stopping condition.

**Remember:** Binary search does not magically work on every collection. The search space must have the right structure.

### 3.1 Bisection Search versus Linear Search

| Feature | Linear search | Binary search |
| --- | --- | --- |
| Search strategy | One by one | Divide in half |
| Requires sorted data | No | Yes, for ordinary array search |
| Worst-case time | $O(n)$ | $O(\log n)$ |
| Search space reduction | One element | Approximately half |

For DSA, you should become very comfortable with this comparison.

---

## 4. Newton-Raphson Method

*Lower priority for your current DSA preparation*

The second major algorithm introduced in Lecture 6 is **Newton-Raphson**. It is another way to approximate the root of a mathematical function. Don't worry if the mathematical derivation feels difficult. The important thing is understanding the central idea.

### 4.1 The basic idea

Suppose we want to calculate:

$$\sqrt{24}$$

We can rewrite this as finding the root of:

$$f(x)=x^2-24$$

Why? Because:

$$\sqrt{24}=r$$

means:

$$r^2=24$$

Therefore:

$$r^2-24=0$$

We want to find a value where the function becomes zero.

### 4.2 How does Newton-Raphson work?

Newton-Raphson uses the derivative of a function to generate a better guess. Its general formula is:

$$g_{\text{new}}=g-\frac{f(g)}{f'(g)}$$

Where:

* $g$ = current guess.
* $f(g)$ = function evaluated at the guess.
* $f'(g)$ = derivative evaluated at the guess.
* $g_{\text{new}}$ = improved guess.

For our square-root problem:

$$f(g)=g^2-k$$

Its derivative is:

$$f'(g)=2g$$

Substituting:

$$g_{\text{new}}=g-\frac{g^2-k}{2g}$$

This becomes:

$$g_{\text{new}}=\frac{1}{2}\left(g+\frac{k}{g}\right)$$

That's the formula used to improve the square-root guess.

### 4.3 Python implementation

```python
epsilon = 0.01
k = 24.0

guess = k / 2.0
num_guesses = 0

while abs(guess**2 - k) >= epsilon:

  num_guesses += 1

  guess = guess - (((guess**2) - k) / (2 * guess))

print("Number of guesses:", num_guesses)
print("Square root:", guess)

```

Notice something interesting:

* Bisection Search calculates the next guess by finding the midpoint.
* Newton-Raphson calculates the next guess using a mathematical formula involving the derivative.

Both are trying to improve the current guess, but they use different strategies.

### 4.4 Bisection versus Newton-Raphson

| Feature | Bisection | Newton-Raphson |
| --- | --- | --- |
| Next guess | Midpoint | Derivative-based formula |
| Main idea | Halve the interval | Improve the current guess |
| Requires derivative | No | Yes |
| Convergence | Predictable when conditions hold | Often very fast near a suitable root |
| Mathematical requirement | Ordered interval and sign information | Differentiable function and suitable starting guess |

> **What to write in your notebook — Newton-Raphson**
> * Newton-Raphson is a numerical method for approximating roots of functions.
> * It uses derivatives to calculate improved guesses.
> * General formula:
> 
> 
> $$g_{\text{new}}=g-\frac{f(g)}{f'(g)}$$
> 
> 
> * For square roots:
> 
> 
> $$g_{\text{new}}=\frac{1}{2}\left(g+\frac{k}{g}\right)$$
> 
> 

You do not need to spend hours deriving this formula or solving numerous Newton-Raphson problems for your current DSA preparation.

---

## 5. Algorithmic efficiency: The big lesson

This lecture introduces an important shift in thinking. Consider two algorithms that solve the same problem:

* **Algorithm A** examines every possible candidate.
* **Algorithm B** eliminates half the candidates at each step.

Both may produce the correct answer. But their computational costs are dramatically different.

### Growth comparison

* **Linear search:** Operations grow proportionally with input size $n$ — $O(n)$.
* **Binary search:** Operations grow logarithmically with input size $n$ — $O(\log n)$.

The exact number of comparisons depends on implementation, but the growth pattern is what matters. This is why algorithm design isn't simply about getting the correct answer. It's about getting the correct answer efficiently.

---

## 6. What to prioritize for DSA

This is how I'd allocate your attention:

| Lecture 6 topic | DSA importance | Recommendation |
| --- | --- | --- |
| Bisection Search intuition | Very high | Master |
| Midpoint calculation | Very high | Master |
| Updating search boundaries | Very high | Master |
| Loop termination | Very high | Master |
| Binary search complexity | Very high | Master |
| Conditions for binary search | Very high | Master |
| Floating-point epsilon | Medium | Understand |
| Newton-Raphson derivation | Low | Skim |
| Derivative-based implementation | Low | No extensive practice |
| Numerical root-finding problems | Low | Skip extra exercises |

One distinction: Newton-Raphson is useful in numerical computing, but it isn't a prerequisite for learning ordinary DSA binary search.

---

## 7. What should go into your notebook?

This is the condensed version I'd actually recommend handwriting:

**Lecture 6: Bisection Search**

1. **Bisection Search:** Repeatedly divides the search interval into two halves. Eliminates half of the remaining search space per iteration. Requires an ordered search space and a way to determine which half contains the answer.
2. **Midpoint formula:**

$$mid=\frac{low+high}{2}$$

3. **Boundary updates:**
* Guess too small $\rightarrow$ `low = mid`
* Guess too large $\rightarrow$ `high = mid`
* Sufficiently accurate $\rightarrow$ stop.


4. **Approximation stopping condition:**

$$\vert{}mid^2-x\vert{}<\epsilon$$

5. **Time complexity:**

$$O(\log n)$$

6. **Newton-Raphson:** Uses derivatives to improve guesses.
* General formula:



$$g_{\text{new}}=g-\frac{f(g)}{f'(g)}$$

* For square roots:

$$g_{\text{new}}=\frac{1}{2}\left(g+\frac{k}{g}\right)$$

7. **Main lesson:** Efficient algorithms reduce the amount of work required to solve a problem.

---

## 8. Practice: What should you actually solve?

I don't want you repeating the Lecture 5 experience of spending hours implementing specialized numerical algorithms. For Lecture 6, however, binary search deserves practice because it is directly relevant to DSA.

| Exercise | Priority |
| --- | --- |
| Trace Bisection Search manually | Must do |
| Implement square-root approximation using Bisection | Must do once |
| Understand how `low` and `high` change | Must do |
| Implement integer binary search | Must do |
| MIT's finger exercise | Attempt |
| Multiple Newton-Raphson implementations | Skip |
| Multiple numerical approximation problems | Skip |

### One exercise for you

MIT's finger exercise asks you to guess an integer between `0` and `1000` using Bisection Search. Your program should print:

```text
count: <number of guesses>
answer: <the guessed number>

```

You should use the feedback from each guess to eliminate half of the remaining possibilities. Try implementing this independently. Don't look at the solution immediately.

---

## 9. Official resources

* Official Lecture 6: Bisection Search (available in your $\U0001f4d4$ [Python Main](https://gemini.google.com/notebook/f6430f22-5341-40c5-94ae-c19cd61318c9) notebook)
* Lecture 6 slides (PDF) and full lecture transcript
* Lecture 6 video

---

## 10. What you should take away

There are three particularly important ideas:

1. **Representation matters:** A mathematical number and its computer representation are not always identical.
2. **Precision must be designed:** Algorithms need explicit definitions of acceptable error.
3. **Correctness includes termination:** An algorithm must account for situations where its assumptions fail, such as overshooting.

One final connection: Lecture 6 introduces Bisection Search, which improves on the slow approximation approach by systematically narrowing down the search interval. That is where the algorithmic thinking gets particularly interesting.

Spend your effort understanding how the search space changes, why half can be eliminated, and how the loop maintains its boundaries. You don't need to become an expert in numerical approximation. You do need to become comfortable thinking in terms of search spaces and eliminating possibilities. That's the skill worth carrying into DSA. 🚀