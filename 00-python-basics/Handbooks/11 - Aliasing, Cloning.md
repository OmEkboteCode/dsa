# **MIT 6.100L, Lecture 11: Aliasing and Cloning**



Very important for DSA

Study notes



This lecture builds on Lecture 10. The central question is:

**When you copy a list, are you creating a new list or just another reference to the same list?**

Understanding this distinction is essential when working with arrays, nested lists, functions and memory.

We'll cover:

1. Aliasing.
2. Cloning lists.
3. Shallow copying and nested lists.
4. Mutation and references.

## **1. Aliasing**

Aliasing happens when multiple variables refer to the same object.

```
L1 = [1, 2, 3]
L2 = L1
```

Now both variables refer to the same list.

**Memory representation**

Two names point to one list object.

Example:

```
L1 = [1, 2, 3]
L2 = L1
L2.append(4)
print(L1)  # [1, 2, 3, 4]
print(L2)  # [1, 2, 3, 4]
```

Changing the list through `L2` also affects what you see through `L1`.

**What to write:**

- Aliasing: multiple variables refer to the same object.
- Assignment (`L2 = L1`) does not create a new list.
- Mutating the shared list affects all aliases.

**DSA importance: Very high.** Essential for understanding unexpected changes to arrays and lists.

## **2. Cloning a List**

Cloning means creating a new list containing the elements of an existing list.

Unlike aliasing, cloning creates a separate outer list.

### **Method 1: Slicing**

```
L1 = [1, 2, 3]
L2 = L1[:]
```

### **Method 2:&#x20;**`list()`

```
L2 = list(L1)
```

### **Method 3:&#x20;**`.copy()`

```
L2 = L1.copy()
```

All three create a shallow copy.

Example:

```
L1 = [1, 2, 3]
L2 = L1.copy()
L2.append(4)
print(L1)  # [1, 2, 3]
print(L2)  # [1, 2, 3, 4]
```

The original list remains unchanged.

**What to write:**

- Cloning creates a separate list object.
- Changes to the outer structure of the clone do not affect the original.
- Common methods: `L[:]`, `list(L)`, `L.copy()`.

**DSA importance: High.** Useful when an algorithm needs to preserve the original list while modifying a copy.

## **3. Shallow Copy vs Deep Copy**

Important concept

This is the most important distinction in the lecture after aliasing.

Consider a nested list:

```
old_list = [[1, 2], [3, 4]]
```

A nested list contains other lists as elements.

### **A. Shallow copy**

A shallow copy creates a new outer list, but the nested lists are still shared.

```
import copyold_list = [[1, 2], [3, 4]]
new_list = copy.copy(old_list)
```

Now:

- `old_list` and `new_list` are different outer lists.
- Their inner lists are shared.

For example:

```
new_list[0][0] = 100
print(old_list)
```

Output:

```
[[100, 2], [3, 4]]
```

The original changed because both lists refer to the same inner list.

### **B. Deep copy**

A deep copy creates independent copies of the outer list and its nested structures.

```
import copyold_list = [[1, 2], [3, 4]]
new_list = copy.deepcopy(old_list)
new_list[0][0] = 100
print(old_list)
print(new_list)
```

Output:

```
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

The original remains unchanged.

### **Comparison**

| Feature                                  | Aliasing | Shallow copy | Deep copy |
| ---------------------------------------- | -------- | ------------ | --------- |
| New outer list                           | No       | Yes          | Yes       |
| Inner lists copied                       | No       | No           | Yes       |
| Changes to outer structure shared        | Yes      | No           | No        |
| Changes to nested mutable objects shared | Yes      | Yes          | No        |

**What to write in your notebook**

- Shallow copy: Creates a new outer object but shares nested mutable objects.
- Deep copy: Recursively copies nested objects.
- `copy.copy(L)` creates a shallow copy.
- `copy.deepcopy(L)` creates a deep copy.
- `L[:]` also creates a shallow copy.

**DSA importance: High.** Particularly useful when working with matrices, nested lists, graph representations and backtracking algorithms.

## **4. Mutation While Iterating: The Cloning Solution**

Remember the problem from Lecture 10?

Consider:

```
def remove_dups(L1, L2):    
for e in L1:        
if e in L2:            
L1.remove(e)
```

This function tries to remove elements from `L1` that also exist in `L2`.

But modifying a list while iterating over it can cause elements to be skipped.

### **The solution: Iterate over a clone**

```
def remove_dups(L1, L2):    
L1_copy = L1[:]    
for e in L1_copy:        
if e in L2:            
L1.remove(e)
```

Now:

- The loop iterates over `L1_copy`.
- The original `L1` is modified.
- The iteration sequence remains unchanged.

**What to write:**

When removing elements during iteration, consider iterating over a separate copy instead of the list being modified.

**DSA importance: High.** Useful for safely modifying collections during traversal.

## **5.&#x20;**`is`**&#x20;vs&#x20;**`==`

Another useful distinction.

- `==` checks whether two objects have equal values.
- `is` checks whether two variables refer to the exact same object.

Example:

```
L1 = [1, 2, 3]
L2 = [1, 2, 3]
L3 = L1
print(L1 == L2)  
# Trueprint(L1 is L2)  
# Falseprint(L1 is L3)  
# True
```

Why?

`L1` and `L2` contain equal values, but are separate lists.

`L1` and `L3` refer to the same list.

**What to write in your notebook**

| Operator | Checks          |
| -------- | --------------- |
| `==`     | Value equality  |
| `is`     | Object identity |

**DSA importance: Medium.** Useful for understanding references and debugging. For ordinary value comparisons, use `==`.

## **6. What deserves the most attention?**

| Topic                      | DSA importance | Priority   |
| -------------------------- | -------------- | ---------- |
| Aliasing                   | Very high      | Master     |
| Cloning using `[:]`        | High           | Practise   |
| Shallow vs deep copy       | High           | Understand |
| Mutation during iteration  | Very high      | Master     |
| Passing lists to functions | Very high      | Master     |
| `is` vs `==`               | Medium         | Understand |
| `copy.copy()`              | Medium         | Know usage |
| `copy.deepcopy()`          | Medium         | Know usage |

## **7. Practice exercises**

You only need three focused exercises.

**Exercise 1: Predict the output**

```
L1 = [1, 2, 3]
L2 = L1
L3 = L1[:]
L2.append(4)L3.append(5)
print(L1)
print(L2)
print(L3)
```

**Exercise 2: Understand nested copying**

```
import copyL1 = [[1, 2], [3, 4]]
L2 = L1[:]
L3 = copy.deepcopy(L1)
L2[0][0] = 100
L3[1][0] = 200
print(L1)
print(L2)
print(L3)
```

Predict all three outputs before running the code.

**Exercise 3: Implement&#x20;**`remove_dups(L1, L2)`

Write a function that removes every element from `L1` that also occurs in `L2`, without skipping elements.

## **8. Final notebook checklist**

**Lecture 11 completion**

0/6

Aliasing and shared references

Cloning using slicing, list() or copy()

Shallow copy vs deep copy

Mutation while iterating and the cloning solution

Passing lists to functions

is vs ==

## **9. Official resources**

- [MIT Lecture 11 slides (PDF, 54 pages)](https://live.ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_lec11.pdf?utm_source=chatgpt.com).
- [MIT 6.100L complete lecture playlist](https://learn.mit.edu/c/unit/ocw?resource=13921\&utm_source=chatgpt.com).
- [Lecture 11 finger exercise solutions](https://live.ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/mit6_100l_f22_ex11_sol.pdf?utm_source=chatgpt.com).

## **My recommendation**

Spend most of your practice time on these three concepts:

1. Aliasing versus cloning.
2. Shallow copy versus deep copy.
3. Mutation while iterating.

These are directly useful when you start working with complex data structures.

You don't need to solve dozens of copying problems. Learn to trace references accurately and predict which objects change.

**The real skill you're developing is understanding how data moves through your program, not merely memorizing Python syntax.** 🚀