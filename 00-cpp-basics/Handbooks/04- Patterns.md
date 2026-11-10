Om, welcome to Module 5: Patterns! 🔥

This is an important transition in your DSA journey. Patterns might look like simple star-printing exercises, but they train some of the most fundamental programming skills: nested loops, iteration control, row-column relationships, conditions, and logical problem-solving.

And there's a secret: once you understand the logic behind patterns, many problems involving 2D arrays, matrices, and nested iterations become easier to approach.

For this module, we'll use your preferred format:

- Questions and answers as the primary learning material.
- English answers followed by Hinglish explanations.
- Important Smart Notes inserted between relevant Q&A sections.
- Code explained line by line.
- Dry-run tables for understanding execution.
- Common mistakes and traps.
- Questions about explaining code aloud.

We won't duplicate an entire Smart Notes chapter. We'll keep only the essential reference material.

# Sigma DSA with C++ · Module 5

# Pattern Programming

Q&A Handbook · Module 5

English + Hinglish

Sigma lecture lineup

1. Nested Loops
2. Nested Loops (Dry Run)
3. Star Pattern
4. Inverted Star Pattern
5. Half Pyramid Pattern
6. Character Pyramid Pattern
7. Hollow Rectangle Pattern
8. Inverted & Rotated Half-Pyramid Pattern
9. Floyd's Triangle Pattern
10. Diamond Pattern
11. Butterfly Pattern

# Part 1. Nested loops and pattern fundamentals

## Q1. What is pattern programming?

English answer:

Pattern programming is a programming technique in which loops and conditional statements are used to generate structured arrangements of characters, numbers, or symbols.

Patterns are commonly used to develop logical thinking and understand nested loops.

Hinglish:

Pattern programming mein loops aur conditions use karke stars, numbers ya characters ka specific design print karte hain. Isse nested loops aur logical thinking improve hoti hai.

## Q2. Why are patterns important in DSA?

English answer:

Pattern problems help develop:

1. Understanding of nested loops.
2. Control over iteration and loop conditions.
3. Ability to visualize rows and columns.
4. Logical problem-solving skills.
5. Understanding of how conditions control execution.

These concepts are useful in matrix traversal, 2D arrays, and other algorithmic problems.

Hinglish:

Patterns sirf stars print karna nahi sikhate. Ye sikhate hain ki multiple loops kaise coordinate karte hain, rows aur columns kaise control hote hain, aur conditions ke through output kaise design hota hai.

## Q3. What is a nested loop?

English answer:

A nested loop is a loop placed inside the body of another loop. The inner loop executes its iterations for every iteration of the outer loop, unless execution is interrupted.

Example:

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 4; j++) {
        cout << "* ";
    }

    cout << endl;
}
```

Hinglish:

Ek loop ke andar doosra loop likhna nested loop kehlata hai. Outer loop ki har iteration par inner loop apni complete iterations execute karta hai.

## Q4. In pattern programming, what does the outer loop usually represent?

English answer:

The outer loop generally controls the number of rows in a pattern.

For example, if the outer loop executes five times, the pattern generally contains five rows, assuming one row is completed during each outer iteration.

Hinglish:

Outer loop generally rows control karta hai. Agar outer loop five times execute hota hai, toh generally five rows print hongi.

## Q5. What does the inner loop usually represent?

English answer:

The inner loop generally controls the number of elements printed in each row, such as stars, numbers, or characters.

Hinglish:

Inner loop har row mein kitne stars, numbers ya characters print honge, woh control karta hai.

## Q6. Why do we use `cout << endl` outside the inner loop?

English answer:

We use `cout << endl` after the inner loop to move the output cursor to the next line once all elements of the current row have been printed.

If it is placed inside the inner loop, each element may appear on a separate line.

Hinglish:

Inner loop current row ke saare elements print karta hai. Uske complete hone ke baad `endl` cursor ko next line par le jaata hai.

Common mistake

Putting `endl` inside the inner loop accidentally converts a horizontal row into a vertical arrangement.

## Q7. How do you calculate the total number of executions in nested loops?

English answer:

When both loops have fixed iteration counts and the inner loop runs completely for every outer iteration, multiply their iteration counts.

For example:

- Outer loop: 3 iterations.
- Inner loop: 4 iterations per outer iteration.

Total inner-body executions:

\\[ 3 \times 4 = 12 \\]

Hinglish:

Outer loop 3 baar aur inner loop har baar 4 baar chalega. Total inner loop body 12 baar execute hogi.

## Smart Note 1 · The pattern-solving formula

## Think in rows, then columns

Outer loop

# i

Controls rows

Inner loop

# j

Controls columns

For every pattern, ask these four questions:

1. How many rows are required?
2. How many elements are printed in each row?
3. How many spaces are needed before the elements?
4. What changes from one row to the next?

This is the foundation. Don't start writing code immediately after looking at a pattern. First determine the row and column relationship.

# Part 2. Star and inverted star patterns

## Q8. How do you print a square star pattern?

English answer:

A square star pattern contains an equal number of rows and columns. Both the outer and inner loops execute N times.

Code:

```
int n = 4;

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n; j++) {
        cout << "* ";
    }

    cout << endl;
}
```

Output:

```
* * * *
* * * *
* * * *
* * * *
```

Hinglish:

Dono loops n times execute hote hain. Outer loop four rows banata hai aur inner loop har row mein four stars print karta hai.

## Q9. How do you print a right-angled half-pyramid star pattern?

English answer:

A right-angled half-pyramid contains an increasing number of stars in each row. The number of stars in row i is equal to i.

Code:

```
int n = 4;

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "* ";
    }

    cout << endl;
}
```

Output:

```
*
* *
* * *
* * * *
```

Hinglish:

Outer loop rows control karta hai. Inner loop ki condition `j <= i` hai. Isliye first row mein one star, second mein two, third mein three aur fourth mein four stars print hote hain.

## Q10. Why do we use `j <= i` in a half-pyramid pattern?

English answer:

The condition `j <= i` ensures that the inner loop executes exactly i times during the ith row. Therefore, the number of stars increases by one in every new row.

Hinglish:

Jab i ki value 1 hai, inner loop one time chalega. Jab i ki value 2 hai, two times chalega. Isi tarah stars increase hote hain.

## Q11. How do you print an inverted half-pyramid?

English answer:

An inverted half-pyramid contains a decreasing number of stars in successive rows. The inner loop starts from 1 and continues while `j <= n - i + 1`.

Code:

```
int n = 4;

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= n - i + 1; j++) {
        cout << "* ";
    }

    cout << endl;
}
```

Output:

```
* * * *
* * *
* *
*
```

Hinglish:

Har next row mein one star kam hota hai. Isliye inner loop ki limit `n - i + 1` rakhi gayi hai.

## Q12. What is the difference between an increasing and decreasing half-pyramid?

English answer:

In an increasing half-pyramid, the number of elements increases with each row. In a decreasing half-pyramid, the number of elements decreases with each row.

| Pattern    | Inner loop condition |
| ---------- | -------------------- |
| Increasing | `j <= i`             |
| Decreasing | `j <= n - i + 1`     |

Hinglish:

Increasing pattern mein har row mein stars badhte hain. Decreasing pattern mein har row mein stars kam hote hain.

# Part 3. Character pyramid patterns

## Q13. What is a character pyramid pattern?

English answer:

A character pyramid is a pattern in which alphabetic characters are printed in an organized arrangement using nested loops.

The inner loop controls how many characters appear in each row, while the character variable or expression determines which character is printed.

Example:

```
int n = 4;

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << char('A' + j - 1) << " ";
    }

    cout << endl;
}
```

Output:

```
A
A B
A B C
A B C D
```

Hinglish:

Is pattern mein har row mein alphabets print hote hain. Inner loop decide karta hai ki kitne characters print honge, aur `char('A' + j - 1)` alphabet generate karta hai.

## Q14. How does `char('A' + j - 1)` work?

English answer:

Characters have numeric character codes. Adding an integer to `'A'` produces the corresponding character code, which is converted back to a character using `char()`.

For example:

| Expression | Result |
| ---------- | ------ |
| `'A' + 0`  | A      |
| `'A' + 1`  | B      |
| `'A' + 2`  | C      |
| `'A' + 3`  | D      |

Hinglish:

Computer characters ko internally numeric codes ke through represent karta hai. `'A'` mein 1 add karne par next alphabet B milta hai. `char()` us numeric value ko character mein convert karta hai.

## Q15. How can you print a character pyramid where each row contains the same character?

English answer:

We can print the character corresponding to the outer loop variable in every iteration of the inner loop.

Code:

```
int n = 4;

for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j++) {
        cout << char('A' + i - 1) << " ";
    }

    cout << endl;
}
```

Output:

```
A
B B
C C C
D D D D
```

Hinglish:

Yahan character i par depend karta hai, j par nahi. Isliye same row mein same alphabet repeat hota hai.

# Part 4. Hollow rectangle pattern

## Q16. What is a hollow rectangle pattern?

English answer:

A hollow rectangle is a pattern in which characters are printed only along the boundary of a rectangular shape, leaving the interior empty.

Code:

```
int rows = 4;
int cols = 5;

for (int i = 1; i <= rows; i++) {

    for (int j = 1; j <= cols; j++) {

        if (i == 1 || i == rows ||
            j == 1 || j == cols) {

            cout << "* ";
        }
        else {
            cout << "  ";
        }
    }

    cout << endl;
}
```

Output:

```
* * * * *
*       *
*       *
* * * * *
```

Hinglish:

Hollow rectangle mein sirf boundary par stars print hote hain. First row, last row, first column aur last column par star print karte hain. Baaki positions par spaces print karte hain.

## Q17. Why do we use the OR operator in a hollow rectangle?

English answer:

The logical OR operator `||` combines the four boundary conditions. If any one condition is true, a star is printed.

```
i == 1 || i == rows || j == 1 || j == cols
```

These conditions represent:

- First row.
- Last row.
- First column.
- Last column.

Hinglish:

OR operator ka matlab hai ki chaar conditions mein se koi ek bhi true hui toh star print hoga. Isi tarah rectangle ki boundary identify hoti hai.

## Q18. What happens if we replace OR (`||`) with AND (`&&`) in this pattern?

English answer:

The conditions become much more restrictive. For an ordinary rectangle with more than one row and column, a position generally cannot simultaneously belong to the first and last row and first and last column. Therefore, the expected boundary will not be printed.

Hinglish:

OR mein koi ek condition true hona enough hai. AND mein saari conditions simultaneously true honi chahiye. Isliye hollow rectangle ka logic break ho jaayega.

Common trap

Remember the difference between boundary detection and interior detection. The hollow rectangle uses OR to identify the boundary.

# Part 5. Inverted and rotated half-pyramid

## Q19. What is an inverted and rotated half-pyramid?

English answer:

An inverted and rotated half-pyramid is a right-aligned triangular pattern in which the number of leading spaces decreases while the number of stars increases in successive rows.

Code:

```
int n = 4;

for (int i = 1; i <= n; i++) {

    for (int j = 1; j <= n - i; j++) {
        cout << " ";
    }

    for (int j = 1; j <= i; j++) {
        cout << "*";
    }

    cout << endl;
}
```

Output:

```
   *
  **
 ***
****
```

Hinglish:

Is pattern mein do inner loops use hote hain. Pehla spaces print karta hai aur doosra stars. Har next row mein spaces kam aur stars zyada hote hain.

## Q20. Why do we need two inner loops for this pattern?

English answer:

We need two inner loops because spaces and stars follow different repetition rules.

- The first loop prints `n - i` spaces.
- The second loop prints `i` stars.

Hinglish:

Spaces aur stars ki quantities alag-alag change hoti hain. Isliye unhe separately control karne ke liye two inner loops use karte hain.

## Q21. How do spaces help in pattern alignment?

English answer:

Spaces control the horizontal position of printed characters. By changing the number of leading spaces in each row, we can shift a pattern left or right.

Hinglish:

Spaces cursor ki horizontal position control karte hain. Har row ke starting spaces change karke pattern ko left ya right align kar sakte hain.

## Smart Note 2 · Spaces are also pattern elements

Remember this important concept:

In many patterns, you are not simply printing stars. You are printing two different things:

1. Leading spaces.
2. Visible characters.

For a right-aligned half-pyramid:

| Row | Spaces | Stars |
| --- | ------ | ----- |
| 1   | 3      | 1     |
| 2   | 2      | 2     |
| 3   | 1      | 3     |
| 4   | 0      | 4     |

Mental model: First position the cursor using spaces, then print the stars.

# Part 6. Floyd's Triangle

## Q22. What is Floyd's Triangle?

English answer:

Floyd's Triangle is a triangular arrangement of consecutive natural numbers, where each successive row contains one more number than the previous row.

Code:

```
int n = 4;
int num = 1;

for (int i = 1; i <= n; i++) {

    for (int j = 1; j <= i; j++) {
        cout << num << " ";
        num++;
    }

    cout << endl;
}
```

Output:

```
1
2 3
4 5 6
7 8 9 10
```

Hinglish:

Floyd's Triangle mein numbers continuously increase hote hain. First row mein one number, second mein two, third mein three numbers print hote hain. `num` har baar increment hota hai.

## Q23. Why is `num` initialized outside both loops?

English answer:

The variable `num` must preserve its value across all rows. Initializing it outside both loops ensures that it continues from the previous row instead of restarting.

Hinglish:

Agar num ko inner loop ke andar initialize karenge toh har iteration mein number reset ho sakta hai. Bahar initialize karne se previous value preserve hoti hai.

## Q24. What happens if we initialize `num = 1` inside the outer loop?

English answer:

The number sequence restarts from 1 for every new row. The output will no longer be a standard Floyd's Triangle.

For example:

```
1
1 2
1 2 3
1 2 3 4
```

Hinglish:

Outer loop ke andar num ko 1 karne se har row mein counting dobara start hogi. Continuous numbering nahi milegi.

## Q25. How many numbers are printed in Floyd's Triangle with N rows?

English answer:

The total number of elements is the sum of the first N natural numbers.

\\[ 1+2+3+\cdots+n=\frac{n(n+1)}{2} \\]

For four rows:

\\[ \frac{4(5)}{2}=10 \\]

Hinglish:

N rows mein total numbers 1 se N tak add karne ke equal hote hain. Four rows mein total 10 numbers print honge.

# Part 7. Diamond pattern

## Q26. What is a diamond pattern?

English answer:

A diamond pattern is a symmetrical arrangement of stars consisting of an increasing upper pyramid and a decreasing lower pyramid.

Code:

```
int n = 4;

// Upper half
for (int i = 1; i <= n; i++) {

    for (int j = 1; j <= n - i; j++) {
        cout << " ";
    }

    for (int j = 1; j <= 2 * i - 1; j++) {
        cout << "*";
    }

    cout << endl;
}

// Lower half
for (int i = n - 1; i >= 1; i--) {

    for (int j = 1; j <= n - i; j++) {
        cout << " ";
    }

    for (int j = 1; j <= 2 * i - 1; j++) {
        cout << "*";
    }

    cout << endl;
}
```

Output:

```
   *
  ***
 *****
*******
 *****
  ***
   *
```

Hinglish:

Diamond do parts se milkar banta hai: upper half aur lower half. Upper half mein stars increase hote hain, lower half mein decrease. Spaces alignment maintain karte hain.

## Q27. Why does the number of stars follow `2 * i - 1`?

English answer:

A centered pyramid requires an odd number of stars in each row.

The sequence is:

\\[ 1,3,5,7,9,\ldots \\]

The expression `2 * i - 1` generates this sequence for successive positive integer values of i.

Hinglish:

Diamond mein har row mein odd number of stars chahiye. Formula `2 * i - 1` se 1, 3, 5, 7 jaise numbers generate hote hain.

## Q28. Why does the lower half start from `n - 1` instead of `n`?

English answer:

The middle row has already been printed by the upper half. Starting the lower half from `n - 1` avoids printing the middle row twice.

Hinglish:

Upper half mein middle row already print ho chuki hai. Agar lower half n se start karenge toh middle row repeat hogi. Isliye n-1 se start karte hain.

# Part 8. Butterfly pattern

## Q29. What is a butterfly pattern?

English answer:

A butterfly pattern is a symmetrical star pattern consisting of two triangular wings separated by a central gap. The upper section expands and the lower section contracts.

Code:

```
int n = 4;

// Upper half
for (int i = 1; i <= n; i++) {

    for (int j = 1; j <= i; j++) {
        cout << "*";
    }

    for (int j = 1; j <= 2 * (n - i); j++) {
        cout << " ";
    }

    for (int j = 1; j <= i; j++) {
        cout << "*";
    }

    cout << endl;
}

// Lower half
for (int i = n; i >= 1; i--) {

    for (int j = 1; j <= i; j++) {
        cout << "*";
    }

    for (int j = 1; j <= 2 * (n - i); j++) {
        cout << " ";
    }

    for (int j = 1; j <= i; j++) {
        cout << "*";
    }

    cout << endl;
}
```

Output:

```
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *
```

Hinglish:

Butterfly pattern mein left wing, middle spaces aur right wing hote hain. Upper half mein wings grow karte hain aur spaces decrease hote hain. Lower half mein iska reverse hota hai.

## Q30. How many inner loops are used in each row of the butterfly pattern?

English answer:

Three inner loops are used:

1. The first loop prints the left wing.
2. The second loop prints the central spaces.
3. The third loop prints the right wing.

Hinglish:

First loop left stars print karta hai, second middle spaces aur third right stars print karta hai.

## Q31. Why is the number of middle spaces `2 * (n - i)`?

English answer:

Each wing contains i stars, while the gap must decrease by two spaces for every increase in i. The expression `2 * (n - i)` produces the required symmetrical gap.

Hinglish:

Har next row mein left aur right dono sides par one star increase hota hai. Isliye center gap two spaces kam hota hai.

# Part 9. Important code-tracing questions

These are especially useful because they test whether you understand loop execution rather than simply recognize patterns.

## Q32. What is the output of this program?

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= i; j++) {
        cout << j << " ";
    }
    cout << endl;
}
```

Answer:

```
1
1 2
1 2 3
```

Explanation:

- First row: i = 1, so j executes once.
- Second row: i = 2, so j executes twice.
- Third row: i = 3, so j executes three times.

Hinglish: Inner loop ki limit outer loop variable i par depend karti hai. Har next row mein one additional number print hota hai.

## Q33. What is the output if we exchange the roles of i and j?

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 3; j++) {
        cout << i << " ";
    }
    cout << endl;
}
```

Answer:

```
1 1 1
2 2 2
3 3 3
```

Explanation:

The printed expression is `i`, not `j`. Since i remains unchanged throughout each inner loop, the same number is printed three times in each row.

Hinglish: Inner loop mein j change hota hai, lekin hum i print kar rahe hain. Isliye ek row mein same number three times print hota hai.

## Q34. What happens if the update statement is missing?

```
for (int i = 1; i <= 3;) {
    cout << i << " ";
}
```

Answer:

The program enters an infinite loop because i remains 1 and the condition `i <= 3` always remains true.

Hinglish: i ki value kabhi update nahi hoti. Condition continuously true rahegi, isliye infinite loop banega.

## Q35. How many times does the following statement execute?

```
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= 5; j++) {
        for (int k = 1; k <= 2; k++) {
            cout << "*";
        }
    }
}
```

Answer:

\\[ 4 \times 5 \times 2 = 40 \\]

The print statement executes 40 times.

Hinglish: Teen nested loops hain. Total executions ke liye 4 × 5 × 2 multiply karenge.

## Q36. Find the mistake in this pattern.

```
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++);
    {
        cout << "*";
    }
    cout << endl;
}
```

Answer:

The semicolon after the inner `for` loop terminates that loop immediately. The following block is not part of the loop.

Corrected code:

```
for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "*";
    }
    cout << endl;
}
```

Hinglish: Inner loop ke baad extra semicolon lag gaya hai. Isse loop ka body empty ho jaata hai. Semicolon remove karna hoga.

# Part 10. Common mistakes and traps

\| Mistake | Why it is wrong |\
\|---|---|\
\| Putting `endl` inside inner loop | Elements print on separate lines |\
\| Using `j <= i` instead of `j <= n` | Changes the intended column count |\
\| Forgetting to update a counter | Can create an infinite loop |\
\| Resetting Floyd's Triangle counter | Number sequence restarts |\
\| Starting diamond's lower half at n | Middle row prints twice |\
\| Using `&&` instead of `||` for rectangle boundary | Incorrect boundary condition |\
\| Confusing `i` and `j` | Prints the wrong value or character |\
\| Forgetting spaces in aligned patterns | Pattern loses its shape |\
\| Wrong loop starting or ending value | Missing or extra rows |\
\| Incorrect braces | Changes which statements belong to the loop |

## Important vocabulary for Module 5

| Term               | Meaning                                    |
| ------------------ | ------------------------------------------ |
| Row                | Horizontal arrangement                     |
| Column             | Vertical arrangement                       |
| Symmetry           | Matching arrangement around a central axis |
| Boundary           | Outer edges of a shape                     |
| Hollow pattern     | Pattern with empty interior                |
| Alignment          | Positioning elements correctly             |
| Nested iteration   | Repetition inside another repetition       |
| Character encoding | Numeric representation of characters       |
| Accumulator        | Variable maintaining a running result      |
| Dry run            | Manually simulating program execution      |
| Inner loop         | Loop inside another loop                   |
| Outer loop         | Enclosing loop                             |
| Iteration count    | Number of executions                       |
| Pattern logic      | Rules determining the printed arrangement  |

# Part 11. Explain your code aloud 🎙️

This section is designed to improve your technical communication, not just your programming knowledge.

For each exercise, explain the code using complete English sentences.

Speaking exercise 1: Explain nested loops

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= i; j++) {
        cout << "* ";
    }
    cout << endl;
}
```

Your explanation must cover:

1. What is the purpose of this program?
2. What does i represent?
3. What does j represent?
4. Why does the inner loop depend on i?
5. Why is endl outside the inner loop?

Speaking exercise 2: Explain Floyd's Triangle

```
int num = 1;

for (int i = 1; i <= 4; i++) {
    for (int j = 1; j <= i; j++) {
        cout << num << " ";
        num++;
    }
    cout << endl;
}
```

Explain why `num` is initialized outside the loops and why it increments inside the inner loop.

Speaking exercise 3: Explain a hollow rectangle

```
if (i == 1 || i == rows ||
    j == 1 || j == cols) {
    cout << "* ";
} else {
    cout << "  ";
}
```

Explain how the four conditions identify the rectangle's boundary.

My rule: Don't read the code aloud character by character. Explain the purpose of each statement and how it contributes to the program.

# Part 12. Technical terms you should be able to define without looking

These are quick oral-revision questions.

1. What is an iteration?
2. What is a nested loop?
3. What is an inner loop?
4. What is an outer loop?
5. What is an accumulator?
6. What is a boundary condition?
7. What is symmetry in pattern programming?
8. What is a dry run?
9. What is the difference between a row and a column?
10. Why is initialization important?

