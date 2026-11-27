# **MIT 6.100L, Lecture 10: Lists and Mutability**



Very important for DSA

Study notes



This lecture builds directly on Lecture 9. You'll learn how Python lists behave when modified, how variables can refer to the same list, and how list operations affect the original data.

**The central concept is mutability.** Understanding it will prevent many confusing bugs when working with arrays, nested lists and functions.

We'll cover:

1. List operations and mutation.
2. Aliasing.
3. Mutating lists while iterating over them.
4. Lists as arguments to functions.

For each topic, I'll specify what to write in your notebook and its DSA importance.

## **1. Mutability**

### **What is mutability?**

An object is mutable if its contents can be changed after creation.

Python lists are mutable.

```
numbers = [10, 20, 30]numbers[0] = 100print(numbers)
```

Output:

```
[100, 20, 30]
```

The original list was modified.

Compare this with strings and tuples:

| Data type | Mutable? |
| --------- | -------- |
| Integer   | No       |
| Float     | No       |
| String    | No       |
| Tuple     | No       |
| List      | Yes      |

### **What to write in your notebook**

**Mutability**

- Mutable objects can be modified after creation.
- Lists are mutable.
- Strings and tuples are immutable.
- Modifying a list changes the existing list rather than creating a new list automatically.

**DSA importance: Very high.** Arrays and lists are frequently modified during algorithms. You must understand whether an operation changes the original data.

## **2. List Operations**

Python provides several operations for modifying lists.

### **A.&#x20;**`append()`

Adds one element to the end of a list.

```
L = [1, 2, 3]L.append(4)print(L)
```

Output:

```
[1, 2, 3, 4]
```

### **B.&#x20;**`extend()`

Adds all elements from another iterable to the list.

```
L = [1, 2, 3]L.extend([4, 5])print(L)
```

Output:

```
[1, 2, 3, 4, 5]
```

### **C.&#x20;**`insert()`

Inserts an element at a specified index.

```
L = [1, 2, 4]L.insert(2, 3)print(L)
```

Output:

```
[1, 2, 3, 4]
```

### **D.&#x20;**`remove()`

Removes the first occurrence of a specified value.

```
L = [1, 2, 3, 2]L.remove(2)print(L)
```

Output:

```
[1, 3, 2]
```

### **E.&#x20;**`pop()`

Removes and returns an element.

```
L = [10, 20, 30]x = L.pop()print(x)  # 30print(L)  # [10, 20]
```

You can also specify an index:

```
L.pop(0)
```

This removes the first element.

### **F.&#x20;**`sort()`

Sorts the original list in place.

```
L = [4, 1, 3, 2]L.sort()print(L)
```

Output:

```
[1, 2, 3, 4]
```

### **G.&#x20;**`reverse()`

Reverses the original list in place.

```
L = [1, 2, 3]L.reverse()print(L)
```

Output:

```
[3, 2, 1]
```

### **Important distinction:&#x20;**`sort()`**&#x20;vs&#x20;**`sorted()`

```
L = [3, 1, 2]new_list = sorted(L)
```

- `L.sort()` modifies the original list.
- `sorted(L)` returns a new sorted list and leaves `L` unchanged.

### **What to write in your notebook**

| Method             | Purpose                     | Modifies original? |
| ------------------ | --------------------------- | ------------------ |
| `append(x)`        | Add one element             | Yes                |
| `extend(iterable)` | Add multiple elements       | Yes                |
| `insert(i, x)`     | Insert at index             | Yes                |
| `remove(x)`        | Remove first matching value | Yes                |
| `pop(i)`           | Remove and return element   | Yes                |
| `sort()`           | Sort list                   | Yes                |
| `reverse()`        | Reverse list                | Yes                |
| `sorted(L)`        | Return sorted copy          | No                 |

**DSA importance: Very high.** You should know these operations and their effects. Also remember that inserting or removing an element in the middle of a Python list generally takes \\(O(n)\\) time because other elements need to shift.

## **3. Aliasing**

Very important concept

This is one of the most important ideas in the lecture.

### **What is aliasing?**

Aliasing occurs when two or more variables refer to the same object in memory.

Example:

```
L1 = [10, 20, 30]L2 = L1
```

Now both variables refer to the same list.

**Visual representation**

Two variable names, one list object.

Let's test:

```
L1 = [10, 20, 30]L2 = L1L2.append(40)print(L1)print(L2)
```

Output:

```
[10, 20, 30, 40]
[10, 20, 30, 40]
```

Why did `L1` also change?

Because `L1` and `L2` refer to the same list. Modifying the object through either variable changes what both variables observe.

### **What to write in your notebook**

**Aliasing**

- Two or more variables refer to the same object.
- Modifying a mutable object through one alias affects the object seen through all aliases.
- Assignment (`L2 = L1`) does not create a copy of a list.

**DSA importance: Very high.** Essential for understanding function arguments, nested data structures and unexpected changes in lists.

## **4. Mutating a List While Iterating**

This is a common source of programming bugs.

Consider:

```
L = [1, 2, 3, 4, 5, 6]for num in L:    if num % 2 == 0:        L.remove(num)print(L)
```

You might expect:

```
[1, 3, 5]
```

But modifying a list while iterating over it can cause elements to be skipped.

Why?

The iterator advances through positions while removing an element shifts the remaining elements to the left.

For example:

- It visits `1`.
- It visits `2`, then removes it.
- `3` shifts into the position just visited.
- The iterator advances, potentially skipping `3`.

**The lesson:** Changing the structure of a list while iterating over it can produce unexpected results.

### **Safer approach**

Create a new list:

```
L = [1, 2, 3, 4, 5, 6]result = []for num in L:    if num % 2 != 0:        result.append(num)print(result)
```

Output:

```
[1, 3, 5]
```

### **What to write in your notebook**

- Avoid removing or inserting elements in a list while iterating over it.
- Modifications can shift indices and cause elements to be skipped or processed unexpectedly.
- When appropriate, build a new list instead.

**DSA importance: High.** Particularly relevant when filtering arrays, deleting elements and implementing traversal algorithms.

## **5. Lists and Functions**

Because lists are mutable, passing them to functions can have an important consequence.

Consider:

```
def modify(L):    L.append(100)numbers = [10, 20, 30]modify(numbers)print(numbers)
```

Output:

```
[10, 20, 30, 100]
```

Why?

The parameter `L` refers to the same list object as `numbers`.

Therefore, modifying the list inside the function changes the original list.

### **What if we reassign the parameter?**

```
def modify(L):    L = [100, 200]numbers = [10, 20, 30]modify(numbers)print(numbers)
```

Output:

```
[10, 20, 30]
```

Why?

Reassigning the local parameter `L` makes it refer to a different list. It doesn't change what `numbers` refers to.

**Remember the distinction:**

- Mutating the object changes the shared object.
- Reassigning a local variable changes its reference.

### **What to write in your notebook**

- Functions receive references to objects through their arguments.
- Mutating a passed list affects the original list.
- Reassigning a local parameter does not reassign the caller's variable.

**DSA importance: Very high.** Important when implementing functions that modify arrays, matrices and other data structures.

## **6. Mutating Lists Through Indexing**

MIT introduces an important programming pattern: modifying every element of a list.

Suppose you want to square every element of a list.

```
def square_list(L):    for i in range(len(L)):        L[i] = L[i] ** 2
```

Example:

```
numbers = [2, 3, 4]square_list(numbers)print(numbers)
```

Output:

```
[4, 9, 16]
```

Why use `range(len(L))`?

Because when we write:

```
for elem in L:
```

`elem` represents the element itself, not its index.

To replace elements at particular positions, we need their indices.

### **What to write in your notebook**

**Modifying elements during iteration**

- Use indices when you need to replace elements in a list.
- `range(len(L))` provides valid indices.
- `L[i] = new_value` modifies the existing list.
- A function that mutates its input does not necessarily need to return the list.

**DSA importance: Very high.** This pattern is frequently used when modifying arrays, traversing matrices and implementing algorithms.

## **7. Functions with Side Effects**

A side effect occurs when a function changes something outside its local computation, such as modifying a list passed to it.

Example:

```
def add_element(L):    L.append(100)numbers = [1, 2, 3]result = add_element(numbers)print(numbers)print(result)
```

Output:

```
[1, 2, 3, 100]
None
```

The function modifies the original list but doesn't explicitly return anything.

This is why `result` is `None`.

An important example from MIT:

```
L = [2, 1, 3]L.append(5)
```

This is correct.

But:

```
L = L.append(5)
```

is a mistake if you intend to keep the list in `L`.

Why? `append()` modifies the list and returns `None`, so `L` becomes `None`.

### **What to write in your notebook**

- Side effects are changes made by a function beyond returning a value.
- Some list methods mutate the list and return `None`.
- Don't assign the result of `append()`, `sort()` or `reverse()` back to the original list.

**DSA importance: Very high.** Helps prevent bugs when functions modify data structures.

## **8. Converting Between Strings and Lists**

MIT also covers converting strings into lists and lists back into strings.

### **A.&#x20;**`list()`

Converts a string into a list of individual characters.

```
s = "Python"L = list(s)print(L)
```

Output:

```
['P', 'y', 't', 'h', 'o', 'n']
```

### **B.&#x20;**`split()`

Splits a string into a list of substrings.

```
sentence = "I love programming"words = sentence.split()print(words)
```

Output:

```
['I', 'love', 'programming']
```

You can also specify a separator:

```
data = "apple,banana,orange"print(data.split(","))
```

### **C.&#x20;**`join()`

Combines a list of strings into one string.

```
words = ["I", "love", "Python"]sentence = " ".join(words)print(sentence)
```

Output:

```
I love Python
```

Another example:

```
letters = ["a", "b", "c"]print("-".join(letters))
```

Output:

```
a-b-c
```

Note: `join()` requires string elements.

### **What to write in your notebook**

| Method         | Purpose                            |
| -------------- | ---------------------------------- |
| `list(s)`      | Convert string into characters     |
| `s.split()`    | Split string into words            |
| `s.split(",")` | Split using a separator            |
| `" ".join(L)`  | Combine strings with spaces        |
| `"".join(L)`   | Combine strings without separators |

**DSA importance: High.** Particularly useful for string manipulation, parsing input and solving string-based problems.

## **9. Tricky Loops: Modifying a List During Iteration**

This is one of the most interesting parts of Lecture 10.

### **Example 1: Appending while using&#x20;**`range(len(L))`

```
L = [1, 2, 3, 4]for i in range(len(L)):    L.append(i)print(L)
```

Output:

```
[1, 2, 3, 4, 0, 1, 2, 3]
```

Why doesn't it continue indefinitely?

Because `range(len(L))` is created using the original length, which is 4.

It produces:

```
range(4)  # 0, 1, 2, 3
```

Even though the list grows, the range doesn't change.

### **Example 2: Appending while iterating directly over a list**

```
L = [1, 2, 3, 4]for e in L:    L.append(0)
```

This loop never naturally finishes!

Why?

The list iterator can encounter the newly appended elements as it continues iterating.

New elements keep getting added, so there are always more elements to visit.

Potential infinite loop

### **Example 3: Reassigning the list inside a loop**

```
L = [1, 2, 3, 4]for e in L:    L = L + L
```

Here, `L + L` creates a new list rather than modifying the original list.

The iterator still iterates over the original list object, so this loop executes four times.

### **What to write in your notebook**

**Mutating lists during iteration**

- `range(len(L))` uses the length determined when the range is created.
- Direct iteration over a list can encounter newly appended elements.
- `L.append()` mutates the existing list.
- `L = L + L` creates a new list and rebinds the variable.
- Understand the difference between mutation and reassignment.

**DSA importance: High.** Important for tracing loops, understanding iteration and avoiding infinite loops or unexpected behaviour.

## **10. Combining Lists:&#x20;**`+`**&#x20;vs&#x20;**`extend()`

Another important distinction:

```
L1 = [1, 2]L2 = [3, 4]L3 = L1 + L2
```

Creates a new list:

```
L3 = [1, 2, 3, 4]
```

But:

```
L1.extend(L2)
```

Modifies `L1` itself:

```
L1 = [1, 2, 3, 4]
```

| Operation       | Behaviour                     |
| --------------- | ----------------------------- |
| `L1 + L2`       | Creates a new list            |
| `L1.extend(L2)` | Modifies L1                   |
| `L1.append(L2)` | Adds L2 as one nested element |

**Notebook:** Write these three differences. They are useful when working with nested lists and array manipulation.

## **11. What deserves the most attention for DSA?**

| Topic                                        | Importance | Practice       |
| -------------------------------------------- | ---------- | -------------- |
| List mutability                              | Very high  | Master         |
| `append()` and `extend()`                    | Very high  | Practise       |
| `sort()` vs `sorted()`                       | High       | Understand     |
| Mutation vs reassignment                     | Very high  | Master         |
| Functions mutating lists                     | Very high  | Practise       |
| Modifying elements using indices             | Very high  | Practise       |
| Loops that modify lists                      | High       | Trace examples |
| `split()` and `join()`                       | High       | Practise       |
| List concatenation                           | Medium     | Understand     |
| All list methods (`insert`, `remove`, `pop`) | Medium     | Know usage     |

**One correction to keep your lecture sequence accurate:** Aliasing and cloning are formally covered in MIT Lecture 11. Lecture 10 introduces the mutation behaviour that makes those concepts important.

## **12. Practice exercises**

I'd recommend these four exercises:

1. Write a function that squares every element of a list by modifying the original list.
2. Write a function that returns a new list without a specified element.
3. Convert a sentence into a list of words, then combine the words into a string.
4. Predict the output of MIT's three tricky loop examples before executing them.

Don't solve dozens of variations. Focus on understanding what happens to the original list.

## **13. Final notebook checklist**

**Lecture 10 completion**

0/8

Mutability and modifying elements

List operations and their return values

Mutation vs reassignment

Functions with side effects

Modifying lists using indices

String/list conversion: split and join

Tricky loops involving list mutation

Concatenation (+) vs extend()

## **14. Official resources**

- [MIT Lecture 10 slides (45 pages)](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec10.pdf?utm_source=chatgpt.com).
- [MIT 6.100L lecture playlist](https://learn.mit.edu/c/unit/ocw?resource=13921\&utm_source=chatgpt.com).
- [Lecture 10 finger exercise solutions](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_ex10_sol.pdf?utm_source=chatgpt.com).

**My recommendation:** Give special attention to mutation, function side effects and modifying lists through indices. These are reusable programming skills, not just Python trivia.

You should be able to look at a piece of code and predict exactly which list changes, which variable refers to which object, and what the final output will be.

That's the level of understanding worth developing before moving to Lecture 11. 🚀