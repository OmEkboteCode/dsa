Om, time for the second half of Module 4! 📘

The Smart Notes gave you the technical reference. This Q&A Handbook will train you to remember definitions, understand the reasoning behind code, trace every iteration, and explain programs confidently in English.

I've expanded the code-reading section because loops are where programmers must learn to mentally simulate execution rather than simply recognize syntax.

# Sigma DSA with C++ · Module 4

# Loops in C++

Q&A Handbook · Sigma 12

English + Hinglish

What you'll master

- Loop terminology and definitions
- For, while and do-while loops
- Loop execution and iteration
- Break and continue
- Nested loops
- Prime number checking and optimization
- Code tracing and line-by-line explanations
- Descriptive and coding questions with answers

## 01 · Fundamentals of loops

Q1. What is a loop in C++?

English answer

A loop is a control structure that repeatedly executes a block of code as long as a specified condition is satisfied.

Hinglish explanation

Loop ek control structure hai jo same block of code ko repeatedly execute karta hai jab tak specified condition true hoti hai.

Q2. Why do we use loops in programming?

English answer

Loops reduce code repetition, improve readability, and allow programs to process repeated operations efficiently.

For example, printing numbers from 1 to 100 requires only a few lines using a loop instead of writing 100 separate print statements.

Hinglish explanation

Loops ka use repetitive tasks ko automate karne ke liye hota hai. Har baar same code manually likhne ki zarurat nahi padti.

Q3. What are the three main types of loops in C++?

English answer

The three main loop structures in C++ are:

1. `for` loop
2. `while` loop
3. `do-while` loop

They differ mainly in how their initialization, condition checking, and updates are organized.

Hinglish explanation

C++ mein teen main loops hain: for, while aur do-while. Teeno repetition ke liye use hote hain, lekin condition check karne aur execution ka order alag hota hai.

Q4. What is an iteration?

English answer

An iteration is one complete execution of a loop's body.

For example, if a loop prints five numbers, its body executes five times, meaning five iterations.

Hinglish explanation

Loop ka ek complete round ek iteration kehlata hai. Agar loop five times execute hota hai, toh five iterations hongi.

Q5. What is an infinite loop?

English answer

An infinite loop is a loop that continues executing indefinitely because its termination condition never becomes false, or because it is intentionally designed to run continuously.

```
while (true) {
    cout << "Hello\n";
}
```

Hinglish explanation

Infinite loop woh loop hai jo terminate nahi hota kyunki uski condition false nahi hoti. Kabhi-kabhi infinite loops intentionally bhi banaye jaate hain, jaise continuously running services.

Common mistake

Forgetting to update a loop variable can accidentally create an infinite loop.

## 02 · For loop

Q6. What is a for loop?

English answer

A for loop is an entry-controlled loop that repeatedly executes a block of code while its condition remains true. It places initialization, condition checking, and update in one statement.

Syntax

```
for (initialization; condition; update) {
    // Loop body
}
```

Hinglish explanation

For loop mein initialization, condition aur update ek hi statement mein likhe jaate hain. Ye generally tab useful hota hai jab iterations ka count known ho.

Q7. What are the three components of a for loop?

English answer

1. Initialization: Establishes the starting value of the loop variable.
2. Condition: Determines whether another iteration should execute.
3. Update: Changes the loop variable after each iteration.

```
for (int i = 1; i <= 5; i++)
```

- `int i = 1`: Initialization
- `i <= 5`: Condition
- `i++`: Update

Hinglish explanation

Initialization starting value set karta hai. Condition decide karti hai ki loop chalega ya nahi. Update har iteration ke baad variable ki value change karta hai.

Q8. What is the execution order of a for loop?

English answer

The execution order is:

1. Initialization happens once.
2. The condition is evaluated.
3. If true, the loop body executes.
4. The update expression executes.
5. Control returns to the condition.
6. When the condition becomes false, the loop terminates.

Hinglish explanation

Pehle initialization hota hai. Phir condition check hoti hai. True hone par body execute hoti hai, uske baad update hota hai. Ye process condition false hone tak repeat hota hai.

Q9. How many times will this loop execute?

```
for (int i = 1; i <= 5; i++) {
    cout << i;
}
```

English answer: The loop executes five times because the values of `i` are 1, 2, 3, 4, and 5. When `i` becomes 6, the condition becomes false.

Hinglish: Loop five baar chalega. Last iteration mein i ki value 5 hogi. Uske baad 6 hone par condition false ho jaayegi.

Q10. What happens if the initial condition of a for loop is false?

English answer

The loop body does not execute even once because a for loop checks its condition before entering the body.

```
for (int i = 10; i < 5; i++) {
    cout << i;
}
```

Output: Nothing.

Hinglish explanation

Agar initial condition hi false hai, toh loop body ek baar bhi execute nahi hogi.

Q11. Can a for loop run without initialization, condition, or update?

English answer

Yes. These expressions are optional, but the semicolons separating them must remain.

```
int i = 1;

for (; i <= 5;) {
    cout << i << '\n';
    i++;
}
```

The loop still works because initialization and update are written outside the for-loop header.

Hinglish explanation

For loop ke header mein ye expressions omit kar sakte hain. Lekin agar update nahi likha, toh zarurat padne par body ke andar update karna hoga.

Q12. What is a loop variable?

English answer

A loop variable is a variable used to control or track the progress of a loop.

```
for (int i = 1; i <= 5; i++)
```

Here, `i` is the loop variable.

Hinglish explanation

Loop variable woh variable hota hai jo iterations ko track karta hai aur loop ki progress control karne mein help karta hai.

## 03 · While loop

Q13. What is a while loop?

English answer

A while loop is an entry-controlled loop that repeatedly executes its body as long as its condition evaluates to true.

Syntax

```
while (condition) {
    // Loop body
    // Update
}
```

Hinglish explanation

While loop pehle condition check karta hai. Agar condition true hai toh body execute hoti hai. False hone par loop terminate ho jaata hai.

Q14. What happens if a while loop's condition is initially false?

English answer

The loop body is skipped completely because the condition is checked before the first iteration.

```
int i = 10;

while (i < 5) {
    cout << i;
}
```

Output: Nothing.

Hinglish explanation

While loop body execute karne se pehle condition check karta hai. Initially false hone par body skip ho jaati hai.

Q15. Why is updating the loop variable important in a while loop?

English answer

Updating the loop variable ensures that the loop makes progress toward its termination condition. Without an appropriate update, the loop may execute indefinitely.

```
int i = 1;

while (i <= 5) {
    cout << i << '\n';
    i++;
}
```

Hinglish explanation

While loop mein variable update karna important hai. Agar value change nahi hui aur condition continuously true rahi, toh infinite loop ban sakta hai.

Q16. Can a while loop be used when the number of iterations is unknown?
Om, time for the second half of Module 4! 📘

The Smart Notes gave you the technical reference. This Q&A Handbook will train you to remember definitions, understand the reasoning behind code, trace every iteration, and explain programs confidently in English.

I've expanded the code-reading section because loops are where programmers must learn to mentally simulate execution rather than simply recognize syntax.

# Sigma DSA with C++ · Module 4

# Loops in C++

Q&A Handbook · Sigma 12

English + Hinglish

What you'll master

- Loop terminology and definitions
- For, while and do-while loops
- Loop execution and iteration
- Break and continue
- Nested loops
- Prime number checking and optimization
- Code tracing and line-by-line explanations
- Descriptive and coding questions with answers

## 01 · Fundamentals of loops

Q1. What is a loop in C++?

English answer

A loop is a control structure that repeatedly executes a block of code as long as a specified condition is satisfied.

Hinglish explanation

Loop ek control structure hai jo same block of code ko repeatedly execute karta hai jab tak specified condition true hoti hai.

Q2. Why do we use loops in programming?

English answer

Loops reduce code repetition, improve readability, and allow programs to process repeated operations efficiently.

For example, printing numbers from 1 to 100 requires only a few lines using a loop instead of writing 100 separate print statements.

Hinglish explanation

Loops ka use repetitive tasks ko automate karne ke liye hota hai. Har baar same code manually likhne ki zarurat nahi padti.

Q3. What are the three main types of loops in C++?

English answer

The three main loop structures in C++ are:

1. `for` loop
2. `while` loop
3. `do-while` loop

They differ mainly in how their initialization, condition checking, and updates are organized.

Hinglish explanation

C++ mein teen main loops hain: for, while aur do-while. Teeno repetition ke liye use hote hain, lekin condition check karne aur execution ka order alag hota hai.

Q4. What is an iteration?

English answer

An iteration is one complete execution of a loop's body.

For example, if a loop prints five numbers, its body executes five times, meaning five iterations.

Hinglish explanation

Loop ka ek complete round ek iteration kehlata hai. Agar loop five times execute hota hai, toh five iterations hongi.

Q5. What is an infinite loop?

English answer

An infinite loop is a loop that continues executing indefinitely because its termination condition never becomes false, or because it is intentionally designed to run continuously.

```
while (true) {
    cout << "Hello\n";
}
```

Hinglish explanation

Infinite loop woh loop hai jo terminate nahi hota kyunki uski condition false nahi hoti. Kabhi-kabhi infinite loops intentionally bhi banaye jaate hain, jaise continuously running services.

Common mistake

Forgetting to update a loop variable can accidentally create an infinite loop.

## 02 · For loop

Q6. What is a for loop?

English answer

A for loop is an entry-controlled loop that repeatedly executes a block of code while its condition remains true. It places initialization, condition checking, and update in one statement.

Syntax

```
for (initialization; condition; update) {
    // Loop body
}
```

Hinglish explanation

For loop mein initialization, condition aur update ek hi statement mein likhe jaate hain. Ye generally tab useful hota hai jab iterations ka count known ho.

Q7. What are the three components of a for loop?

English answer

1. Initialization: Establishes the starting value of the loop variable.
2. Condition: Determines whether another iteration should execute.
3. Update: Changes the loop variable after each iteration.

```
for (int i = 1; i <= 5; i++)
```

- `int i = 1`: Initialization
- `i <= 5`: Condition
- `i++`: Update

Hinglish explanation

Initialization starting value set karta hai. Condition decide karti hai ki loop chalega ya nahi. Update har iteration ke baad variable ki value change karta hai.

Q8. What is the execution order of a for loop?

English answer

The execution order is:

1. Initialization happens once.
2. The condition is evaluated.
3. If true, the loop body executes.
4. The update expression executes.
5. Control returns to the condition.
6. When the condition becomes false, the loop terminates.

Hinglish explanation

Pehle initialization hota hai. Phir condition check hoti hai. True hone par body execute hoti hai, uske baad update hota hai. Ye process condition false hone tak repeat hota hai.

Q9. How many times will this loop execute?

```
for (int i = 1; i <= 5; i++) {
    cout << i;
}
```

English answer: The loop executes five times because the values of `i` are 1, 2, 3, 4, and 5. When `i` becomes 6, the condition becomes false.

Hinglish: Loop five baar chalega. Last iteration mein i ki value 5 hogi. Uske baad 6 hone par condition false ho jaayegi.

Q10. What happens if the initial condition of a for loop is false?

English answer

The loop body does not execute even once because a for loop checks its condition before entering the body.

```
for (int i = 10; i < 5; i++) {
    cout << i;
}
```

Output: Nothing.

Hinglish explanation

Agar initial condition hi false hai, toh loop body ek baar bhi execute nahi hogi.

Q11. Can a for loop run without initialization, condition, or update?

English answer

Yes. These expressions are optional, but the semicolons separating them must remain.

```
int i = 1;

for (; i <= 5;) {
    cout << i << '\n';
    i++;
}
```

The loop still works because initialization and update are written outside the for-loop header.

Hinglish explanation

For loop ke header mein ye expressions omit kar sakte hain. Lekin agar update nahi likha, toh zarurat padne par body ke andar update karna hoga.

Q12. What is a loop variable?

English answer

A loop variable is a variable used to control or track the progress of a loop.

```
for (int i = 1; i <= 5; i++)
```

Here, `i` is the loop variable.

Hinglish explanation

Loop variable woh variable hota hai jo iterations ko track karta hai aur loop ki progress control karne mein help karta hai.

## 03 · While loop

Q13. What is a while loop?

English answer

A while loop is an entry-controlled loop that repeatedly executes its body as long as its condition evaluates to true.

Syntax

```
while (condition) {
    // Loop body
    // Update
}
```

Hinglish explanation

While loop pehle condition check karta hai. Agar condition true hai toh body execute hoti hai. False hone par loop terminate ho jaata hai.

Q14. What happens if a while loop's condition is initially false?

English answer

The loop body is skipped completely because the condition is checked before the first iteration.

```
int i = 10;

while (i < 5) {
    cout << i;
}
```

Output: Nothing.

Hinglish explanation

While loop body execute karne se pehle condition check karta hai. Initially false hone par body skip ho jaati hai.

Q15. Why is updating the loop variable important in a while loop?

English answer

Updating the loop variable ensures that the loop makes progress toward its termination condition. Without an appropriate update, the loop may execute indefinitely.

```
int i = 1;

while (i <= 5) {
    cout << i << '\n';
    i++;
}
```

Hinglish explanation

While loop mein variable update karna important hai. Agar value change nahi hui aur condition continuously true rahi, toh infinite loop ban sakta hai.

Q16. Can a while loop be used when the number of iterations is unknown?

English answer

Yes. A while loop is particularly useful when the number of iterations depends on a condition that may not be known in advance.

For example, repeatedly reading input until the user enters zero.

Hinglish explanation

Jab hume pehle se nahi pata ki loop kitni baar chalega, aur execution kisi condition par depend karta hai, tab while loop useful hota hai.

## 04 · Do-while loop

Q17. What is a do-while loop?

English answer

A do-while loop is an exit-controlled loop that executes its body before checking the condition. Therefore, its body executes at least once.

Syntax

```
do {
    // Loop body
} while (condition);
```

Hinglish explanation

Do-while pehle body execute karta hai aur baad mein condition check karta hai. Isliye condition initially false hone par bhi ek iteration zaroor hoti hai.

Q18. Why is a do-while loop called an exit-controlled loop?

English answer

It is called an exit-controlled loop because its continuation condition is checked after executing the loop body.

Hinglish explanation

Ismein condition end mein check hoti hai, jabki for aur while mein condition body se pehle check hoti hai. Isliye ise exit-controlled loop kehte hain.

Q19. What is the minimum number of iterations of a do-while loop?

English answer

The minimum number of iterations is one, regardless of whether the condition is initially true or false.

```
int i = 10;

do {
    cout << i;
} while (i < 5);
```

Output: `10`.

Hinglish explanation

Condition false hone ke baad bhi body pehle execute ho chuki hoti hai. Isliye minimum one iteration hoti hai.

Q20. What is the difference between while and do-while loops?

English answer

A while loop checks the condition before executing its body, whereas a do-while loop checks the condition after executing its body.

| While                  | Do-while               |
| ---------------------- | ---------------------- |
| Entry-controlled       | Exit-controlled        |
| May execute zero times | Executes at least once |
| Condition before body  | Condition after body   |

Hinglish explanation

While mein pehle condition check hoti hai. Do-while mein pehle body execute hoti hai. Ye dono ke beech ka main difference hai.

Q21. Why is a semicolon required after a do-while condition?

English answer

The do-while construct is defined with a terminating semicolon after its condition.

```
do {
    cout << "Hello";
} while (false);
```

Omitting the semicolon causes a syntax error.

Hinglish explanation

Do-while statement ka syntax semicolon ke saath complete hota hai. Isliye `while(condition);` likhna mandatory hai.

## 05 · Nested loops

Although nested loops aren't explicitly listed in the visible portion of your Sigma screenshot, they are an important extension of loop fundamentals, especially for patterns and 2D arrays.

Q22. What is a nested loop?

English answer

A nested loop is a loop placed inside the body of another loop. The inner loop completes its iterations for each iteration of the outer loop, unless control flow interrupts it.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 3; j++) {
        cout << "* ";
    }
    cout << '\n';
}
```

Output:

```
* * *
* * *
```

Hinglish explanation

Nested loop ka matlab ek loop ke andar doosra loop. Outer loop ki har iteration par inner loop apni complete iterations perform karta hai.

Q23. How many times does an inner loop execute in a nested loop?

English answer

The inner loop executes its complete set of iterations for every iteration of the outer loop, assuming no early termination.

If the outer loop executes 3 times and the inner loop executes 4 times per outer iteration, the inner body executes:

\\[ 3 \times 4 = 12 \\]

Hinglish explanation

Outer loop ki har iteration par inner loop dobara start hota hai. Agar outer 3 baar aur inner har baar 4 baar chale, toh total 12 inner iterations hongi.

Q24. What is the difference between the outer loop and inner loop?

English answer

The outer loop controls the larger repetition structure, while the inner loop performs repeated operations within each outer iteration.

Hinglish explanation

Outer loop overall rounds control karta hai. Inner loop har outer round ke andar repeated work perform karta hai.

Q25. How are nested loops useful in pattern printing?

English answer

Nested loops are used to control rows and columns when generating patterns. The outer loop commonly controls the rows, while the inner loop controls the elements printed in each row.

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 4; j++) {
        cout << "* ";
    }
    cout << '\n';
}
```

Hinglish explanation

Pattern printing mein outer loop rows control karta hai aur inner loop har row mein kitne stars ya numbers print honge, woh control karta hai.

## 06 · Break statement

Q26. What is the break statement?

English answer

The `break` statement immediately terminates the nearest enclosing loop or switch statement and transfers control to the statement following it.

```
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        break;
    }
    cout << i << '\n';
}
```

Output: `1 2`.

Hinglish explanation

Break execute hote hi nearest loop terminate ho jaata hai. Program loop ke baad wale statement par chala jaata hai.

Q27. What happens to the remaining iterations after break executes?

English answer

All remaining iterations of that loop are skipped because the loop terminates immediately.

Hinglish explanation

Break execute hone ke baad loop ki remaining iterations nahi chalti. Loop wahi khatam ho jaata hai.

Q28. What happens when break is used inside nested loops?

English answer

A break statement terminates only the nearest enclosing loop or switch, not every surrounding loop.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) {
            break;
        }
        cout << i << "," << j << '\n';
    }
}
```

Output:

```
1,1
2,1
```

Hinglish explanation

Nested loop mein break sirf inner loop ko terminate karega. Outer loop apni next iteration continue karega.

Important trap

Break does not automatically terminate all nested loops.

## 07 · Continue statement

Q29. What is the continue statement?

English answer

The `continue` statement skips the remaining statements in the current loop iteration and transfers control to the next iteration of the loop.

```
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    cout << i << '\n';
}
```

Output: `1 2 4 5`.

Hinglish explanation

Continue current iteration ka remaining code skip karta hai aur next iteration par le jaata hai. Loop terminate nahi hota.

Q30. What happens after continue executes in a for loop?

English answer

The update expression executes, and then the loop condition is checked again.

Hinglish explanation

For loop mein continue ke baad update expression execute hota hai, phir condition check hoti hai.

Q31. What happens after continue executes in a while loop?

English answer

Control returns directly to the condition check. Any update statement placed later in the loop body is skipped.

Hinglish explanation

While loop mein continue ke baad direct condition check hoti hai. Agar update statement continue ke neeche hai, toh woh skip ho jaayega.

Important trap

```
int i = 1;

while (i <= 5) {
    if (i == 3) {
        continue;
    }
    i++;
}
```

This becomes an infinite loop when `i` reaches 3, because the update is skipped and the condition remains true.

Q32. What is the difference between break and continue?

English answer

`break` terminates the nearest enclosing loop completely. `continue` skips the current iteration and proceeds to the next iteration.

Hinglish explanation

Break poora loop stop karta hai, jabki continue sirf current round skip karta hai.

## 08 · Natural numbers and summation

Q33. What are natural numbers?

English answer

Natural numbers are counting numbers. They are commonly represented as 1, 2, 3, 4, and so on. Some mathematical conventions include zero, so the convention should be stated when relevant.

Hinglish explanation

Natural numbers counting numbers hote hain, jaise 1, 2, 3, 4... Is course mein generally 1 se counting start karenge.

Q34. How can we print the first N natural numbers using a for loop?

English answer

Initialize a loop variable to 1 and continue executing the loop while it is less than or equal to N.

```
int n = 5;

for (int i = 1; i <= n; i++) {
    cout << i << " ";
}
```

Output: `1 2 3 4 5`.

Hinglish explanation

i ko 1 se start karte hain aur jab tak i, n se chhota ya equal hai, print karte hain. Har iteration ke baad i increment hota hai.

Q35. How do you calculate the sum of the first N natural numbers using a loop?

English answer

Initialize a variable `sum` to zero, then repeatedly add each natural number to it.

```
int n = 5;
int sum = 0;

for (int i = 1; i <= n; i++) {
    sum += i;
}

cout << sum;
```

Output: `15`.

Hinglish explanation

Sum variable ko initially zero rakhte hain. Har iteration mein current i ko sum mein add karte hain. End mein total 15 milta hai.

Q36. Why should the sum variable be initialized to zero?

English answer

Zero is the additive identity. Adding zero to a number does not change its value, making it the correct starting value for accumulating a sum.

Hinglish explanation

Zero se addition start karne par original number change nahi hota. Isliye sum calculate karne ke liye initial value zero rakhte hain.

Q37. What is an accumulator variable?

English answer

An accumulator is a variable that stores and progressively updates a running result across multiple iterations.

For example, `sum` accumulates the total of natural numbers.

Hinglish explanation

Accumulator aisa variable hota hai jisme har iteration ka result add ya combine hota rehta hai. Jaise sum variable continuously total calculate karta hai.

## 09 · Prime numbers

Q38. What is a prime number?

English answer

A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.

Examples: 2, 3, 5, 7, 11, 13.

Hinglish explanation

Prime number 1 se bada natural number hota hai jiske exactly do positive factors hote hain: 1 aur woh number khud.

Q39. What is a composite number?

English answer

A composite number is a natural number greater than 1 that has more than two distinct positive divisors.

Examples: 4, 6, 8, 9, 10, 12.

Hinglish explanation

Composite number ke do se zyada positive factors hote hain. Jaise 6 ke factors 1, 2, 3 aur 6 hain.

Q40. Why is 1 neither prime nor composite?

English answer

The number 1 has only one positive divisor, itself. A prime number must have exactly two distinct positive divisors, while a composite number must have more than two.

Hinglish explanation

Number 1 ka sirf ek positive factor hai. Prime ke liye exactly do factors aur composite ke liye do se zyada factors chahiye. Isliye 1 dono mein nahi aata.

Q41. How can we check whether a number is prime using a basic loop?

English answer

We check whether any integer from 2 through `n - 1` divides the number exactly. If a divisor is found, the number is not prime. Otherwise, it is prime, provided `n` is greater than 1.

```
int n = 13;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i < n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

cout << (isPrime ? "Prime" : "Not Prime");
```

Output: `Prime`.

Hinglish explanation

2 se n-1 tak divisors check karte hain. Agar koi number completely divide kar deta hai, toh number prime nahi hai. Agar koi divisor nahi milta aur n, 1 se bada hai, toh number prime hai.

Q42. Why do we use the modulo operator in prime checking?

English answer

The modulo operator `%` calculates the remainder of integer division. If `n % i == 0`, then `i` divides `n` exactly and is a divisor.

Hinglish explanation

Modulo remainder deta hai. Agar `n % i == 0` hai, toh i, n ko completely divide karta hai. Iska matlab hume ek divisor mil gaya.

Q43. Why is the break statement useful in prime checking?

English answer

Once a divisor is found, there is no need to check additional values because the number is already known to be non-prime. `break` terminates the loop immediately.

Hinglish explanation

Ek divisor milte hi prove ho jaata hai ki number prime nahi hai. Isliye baaki numbers check karne ki zarurat nahi, aur break loop stop kar deta hai.

## 10 · Optimized prime checking

Q44. Why is checking divisors only up to the square root of N sufficient?

English answer

If a number has a factor greater than its square root, it must have a corresponding factor smaller than its square root. Therefore, checking all possible divisors beyond the square root is unnecessary.

Hinglish explanation

Agar kisi number ka ek factor square root se bada hai, toh uska doosra corresponding factor square root se chhota hoga. Woh smaller factor pehle hi check ho chuka hoga. Isliye square root tak check karna sufficient hai.

Q45. What is the time complexity of basic prime checking?

English answer

The basic algorithm checks up to `n - 1` possible divisors in the worst case. Its time complexity is \\(O(n)\\).

Hinglish explanation

Basic approach worst case mein n ke proportional number of divisors check karta hai. Isliye time complexity O(n) hai.

Q46. What is the time complexity of optimized prime checking?

English answer

The optimized algorithm checks possible divisors only up to the square root of N. Its time complexity is \\(O(\sqrt n)\\).

Hinglish explanation

Optimized approach sirf square root tak check karta hai, isliye complexity O(root n) ho jaati hai.

Q47. What is the difference between the basic and optimized prime-checking algorithms?

| Basic              | Optimized              |
| ------------------ | ---------------------- |
| Checks up to `n-1` | Checks up to `sqrt(n)` |
| \\(O(n)\\)         | \\(O(\sqrt n)\\)       |
| More iterations    | Fewer iterations       |
| Simpler but slower | More efficient         |

Hinglish: Dono algorithms prime check karte hain, lekin optimized algorithm unnecessary checks remove karke faster execution deta hai.

Q48. Why can we use `i * i <= n` instead of `i <= sqrt(n)`?

English answer

Comparing `i * i` with `n` avoids repeatedly calculating a square root and expresses the same mathematical boundary for positive integer inputs.

```
for (int i = 2; i * i <= n; i++)
```

For large integers, use `i <= n / i` to avoid possible multiplication overflow.

Hinglish explanation

`i * i <= n` square root boundary ko directly represent karta hai. Isse sqrt function baar-baar calculate karne ki zarurat nahi. Very large values ke liye overflow ka dhyan rakhna chahiye.

# 11 · Code-reading and explanation studio 🎙️

This is the most important practical section of your handbook.

I want you to develop the ability to look at unfamiliar code and mentally follow its execution. Don't just memorize the output. Understand how the program reaches that output.

For each example, I'll provide:

- The complete code.
- A line-by-line English explanation.
- A Hinglish explanation.
- A dry-run table where useful.
- The output and reasoning.

## Drill 1 · Print N natural numbers

Code

```
int n = 5;

for (int i = 1; i <= n; i++) {
    cout << i << " ";
}
```

Line-by-line explanation

| Code         | What it does                                                 |
| ------------ | ------------------------------------------------------------ |
| `int n = 5;` | Declares an integer and initializes it to 5.                 |
| `int i = 1;` | Declares the loop variable and sets its starting value to 1. |
| `i <= n`     | Checks whether the current value is within the limit.        |
| `i++`        | Increments i by one after each iteration.                    |
| `cout << i`  | Prints the current value of i.                               |

Dry run

| Iteration | i | Condition | Output |
| --------- | - | --------- | ------ |
| 1         | 1 | True      | 1      |
| 2         | 2 | True      | 2      |
| 3         | 3 | True      | 3      |
| 4         | 4 | True      | 4      |
| 5         | 5 | True      | 5      |
| Exit      | 6 | False     | None   |

Output: 1 2 3 4 5

Hinglish explanation

N ki value 5 hai. Loop variable i, 1 se start hota hai. Jab tak i, n se chhota ya equal hai, current value print hoti hai. Har iteration ke baad i increment hota hai. i = 6 hone par condition false ho jaati hai aur loop terminate hota hai.

## Drill 2 · Sum of natural numbers

Code

```
int n = 4;
int sum = 0;

for (int i = 1; i <= n; i++) {
    sum = sum + i;
}

cout << sum;
```

Line-by-line explanation

1. `int n = 4;` establishes the upper limit.
2. `int sum = 0;` creates an accumulator and initializes it to zero.
3. `int i = 1;` initializes the loop counter.
4. `i <= n` checks whether the loop should continue.
5. `sum = sum + i;` adds the current value of i to the accumulated total.
6. `i++` moves to the next natural number.
7. When the loop finishes, `cout` prints the accumulated sum.

Dry run

| Iteration | i | Previous sum | New sum |
| --------- | - | ------------ | ------- |
| 1         | 1 | 0            | 1       |
| 2         | 2 | 1            | 3       |
| 3         | 3 | 3            | 6       |
| 4         | 4 | 6            | 10      |

Output: 10

Hinglish explanation

Sum initially zero hai. Har iteration mein current i ki value sum mein add hoti hai. Pehle 1, phir 2, phir 3 aur phir 4 add hota hai. Final sum 10 hota hai.

## Drill 3 · While loop with a changing condition

Code

```
int i = 10;

while (i > 0) {
    cout << i << " ";
    i -= 2;
}
```

Line-by-line explanation

1. Initialize the variable `i` to 10.
2. Check whether `i` is greater than zero.
3. If true, print the current value.
4. Subtract 2 from i using the compound assignment operator.
5. Return to the condition check.
6. When i becomes zero, the condition becomes false and the loop exits.

Dry run

| Iteration | i before | Output | i after |
| --------- | -------- | ------ | ------- |
| 1         | 10       | 10     | 8       |
| 2         | 8        | 8      | 6       |
| 3         | 6        | 6      | 4       |
| 4         | 4        | 4      | 2       |
| 5         | 2        | 2      | 0       |
| Exit      | 0        | None   | 0       |

Output: 10 8 6 4 2

Hinglish explanation

i ki starting value 10 hai. Jab tak i zero se bada hai, print hota rahega. Har iteration mein 2 subtract hoga. Zero hone par loop stop ho jaayega.

## Drill 4 · Do-while with a false condition

Code

```
int i = 10;

do {
    cout << i << '\n';
    i++;
} while (i < 5);
```

Line-by-line explanation

1. Initialize i to 10.
2. Enter the do-while body without checking the condition first.
3. Print 10.
4. Increment i to 11.
5. Check whether `i < 5`.
6. The condition is false, so the loop terminates.

Output: 10

Hinglish explanation

Do-while pehle body execute karta hai. Isliye 10 print hota hai. Phir i increment hokar 11 ho jaata hai. Condition false hone par loop stop ho jaata hai.

## Drill 5 · Break in a loop

Code

```
for (int i = 1; i <= 10; i++) {

    if (i == 6) {
        break;
    }

    cout << i << " ";
}

cout << "\nFinished";
```

Line-by-line explanation

1. Initialize i to 1.
2. Check whether i is less than or equal to 10.
3. Evaluate `i == 6` in the if statement.
4. If i is not 6, print its value.
5. When i reaches 6, the if condition becomes true.
6. The break statement immediately terminates the loop.
7. Execution continues after the loop and prints `Finished`.

Output: 1 2 3 4 5, then Finished

Hinglish explanation

Loop 1 se start hota hai aur numbers print karta hai. Jab i ki value 6 hoti hai, if condition true hoti hai aur break execute hota hai. Loop terminate hokar Finished print karta hai.

## Drill 6 · Continue in a for loop

Code

```
for (int i = 1; i <= 5; i++) {

    if (i == 3) {
        continue;
    }

    cout << i << " ";
}
```

Line-by-line explanation

1. Initialize i to 1.
2. Check whether i is within the limit.
3. If i equals 3, execute continue.
4. Continue skips the remaining statements of the current iteration.
5. In this for loop, control moves to the update expression.
6. The loop continues with i = 4.
7. The program prints all values except 3.

Output: 1 2 4 5

Hinglish explanation

Jab i ki value 3 hoti hai, continue execute hota hai aur cout skip ho jaata hai. For loop mein uske baad i increment hota hai. Isliye 3 print nahi hota, lekin loop continue karta hai.

## Drill 7 · Nested loops and pattern printing

Code

```
for (int i = 1; i <= 3; i++) {

    for (int j = 1; j <= 3; j++) {
        cout << "* ";
    }

    cout << '\n';
}
```

Line-by-line explanation

1. The outer loop initializes `i` to 1 and controls the number of rows.
2. For every outer iteration, the inner loop initializes `j` to 1.
3. The inner loop prints three stars because j takes the values 1, 2, and 3.
4. After the inner loop completes, the newline statement moves the cursor to the next row.
5. The outer loop increments i and starts another row.
6. This process repeats until the outer loop finishes its three iterations.

Output

```
* * *
* * *
* * *
```

Dry run summary

| Outer iteration | Inner iterations | Stars printed |
| --------------- | ---------------- | ------------- |
| 1               | 3                | 3             |
| 2               | 3                | 3             |
| 3               | 3                | 3             |
| Total           | 9                | 9             |

Hinglish explanation

Outer loop three rows control karta hai. Har row ke liye inner loop three stars print karta hai. Inner loop complete hone ke baad newline execute hota hai. Is tarah three rows aur three columns ka pattern banta hai.

## Drill 8 · Basic prime checking

Code

```
int n = 9;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i < n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

if (isPrime) {
    cout << "Prime";
} else {
    cout << "Not Prime";
}
```

Line-by-line explanation

1. Initialize `n` to 9.
2. Initialize the Boolean variable `isPrime` to true, assuming the number is prime until a divisor proves otherwise.
3. Check whether n is less than or equal to 1. Since n is 9, this condition is false.
4. Start the for loop with i equal to 2.
5. Check whether `n % i == 0`.
6. When i equals 3, the remainder becomes zero.
7. This proves that 9 has a divisor other than 1 and itself.
8. Set `isPrime` to false.
9. Execute break because additional divisor checks are unnecessary.
10. The final if-else checks `isPrime` and prints `Not Prime`.

Output: Not Prime

Hinglish explanation

9 se start karte hain aur isPrime ko initially true rakhte hain. Divisors check karte waqt 3 milta hai jo 9 ko completely divide karta hai. Isliye isPrime false ho jaata hai aur break loop stop kar deta hai. Final output Not Prime hota hai.

## Drill 9 · Optimized prime checking

Code

```
int n = 29;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

cout << (isPrime ? "Prime" : "Not Prime");
```

Line-by-line explanation

1. Initialize n to 29.
2. Assume the number is prime initially.
3. Reject numbers less than or equal to 1.
4. Initialize the divisor-checking variable i to 2.
5. The condition `i * i <= n` restricts the search to possible divisors up to the square root of n.
6. Check whether the remainder of `n / i` is zero.
7. If a divisor is found, mark the number as non-prime and exit the loop.
8. If no divisor is found, `isPrime` remains true.
9. The ternary operator selects the appropriate output string.

For n = 29, the loop checks:

| i | i × i | Condition        | Divisor? |
| - | ----- | ---------------- | -------- |
| 2 | 4     | 4 ≤ 29           | No       |
| 3 | 9     | 9 ≤ 29           | No       |
| 4 | 16    | 16 ≤ 29          | No       |
| 5 | 25    | 25 ≤ 29          | No       |
| 6 | 36    | 36 ≤ 29 is false | Stop     |

Output: Prime

Hinglish explanation

29 ke liye hum divisors 2 se check karna start karte hain. Condition `i * i <= n` hume square root tak hi checking karne deti hai. Koi divisor nahi milta, isliye number prime hai.

# 12 · Descriptive questions for exams and revision

These questions are particularly useful for written examinations and explaining concepts without code.

Q49. Explain the different types of loops in C++.

English answer

C++ provides three main types of loops:

1. For loop: Used when the repetition structure can conveniently be controlled using initialization, condition, and update in one statement.
2. While loop: Used when repetition depends on a condition checked before each iteration.
3. Do-while loop: Used when the body must execute at least once before checking the condition.

Hinglish explanation

For loop mein initialization, condition aur update ek saath likhte hain. While mein pehle condition check hoti hai. Do-while mein pehle body execute hoti hai.

Q50. Differentiate between break and continue statements.

English answer

The break statement terminates the nearest enclosing loop or switch, whereas the continue statement skips the remaining statements in the current loop iteration and proceeds to the next iteration.

Hinglish explanation

Break poora nearest loop stop karta hai. Continue sirf current iteration skip karta hai aur next iteration par le jaata hai.

Q51. Explain nested loops with an example.

English answer

A nested loop is a loop placed inside another loop. The inner loop executes its iterations for every iteration of the outer loop.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 2; j++) {
        cout << i << "," << j << '\n';
    }
}
```

Output:

```
1,1
1,2
2,1
2,2
```

Hinglish explanation

Inner loop outer loop ke har round mein complete execute hota hai. Is example mein outer two times aur inner har baar two times chalta hai.

Q52. Explain the algorithm for checking whether a number is prime.

English answer

To check whether a number is prime:

1. Read the input number.
2. If it is less than or equal to 1, classify it as non-prime.
3. Check possible divisors starting from 2.
4. If any divisor divides the number exactly, classify it as non-prime.
5. Otherwise, classify it as prime.

Hinglish explanation

Pehle n check karte hain. Agar n, 1 ya usse chhota hai toh non-prime. Otherwise divisors check karte hain. Koi divisor mil gaya toh non-prime, warna prime.

Q53. Explain the optimization used in prime number checking.

English answer

The optimized prime-checking algorithm examines divisors only up to the square root of the input number. This works because every factor pair of a number must contain at least one factor less than or equal to its square root. This reduces the time complexity from \\(O(n)\\) to \\(O(\sqrt n)\\).

Hinglish explanation

Hume square root se aage divisors check karne ki zarurat nahi. Agar koi factor square root se bada hai toh uska corresponding smaller factor pehle mil chuka hoga. Isse algorithm faster ho jaata hai.

Q54. What is the difference between entry-controlled and exit-controlled loops?

English answer

An entry-controlled loop checks its condition before executing the loop body. A do-while loop is exit-controlled because it checks the condition after executing the body.

Hinglish explanation

Entry-controlled loops mein pehle condition check hoti hai. Exit-controlled loop mein pehle body execute hoti hai aur baad mein condition check hoti hai.

# 13 · Technical vocabulary dictionary

These are terms I particularly want you to become comfortable using while explaining your code.

| Technical term   | Meaning                                              |
| ---------------- | ---------------------------------------------------- |
| Iteration        | One execution of a loop body                         |
| Loop counter     | Variable that tracks iterations                      |
| Initialization   | Setting the initial value                            |
| Condition        | Expression evaluated as true or false                |
| Update           | Changing a variable's value                          |
| Termination      | Ending the loop                                      |
| Infinite loop    | Loop that does not terminate naturally               |
| Accumulator      | Variable that maintains a running result             |
| Nested loop      | Loop inside another loop                             |
| Divisor          | Number that divides another number exactly           |
| Remainder        | Amount left after division                           |
| Prime number     | Number with exactly two distinct positive divisors   |
| Composite number | Number with more than two distinct positive divisors |
| Optimization     | Improving resource efficiency                        |
| Time complexity  | How execution requirements grow with input size      |
| Entry-controlled | Condition checked before the body                    |
| Exit-controlled  | Condition checked after the body                     |
| Control flow     | Order in which program statements execute            |

# 14 · How to explain code like an engineer

For Module 4, I want you to adopt this five-part explanation framework.

## The L-I-C-U-O framework

A speaking structure for explaining any loop

L · Logic

What is the purpose of the loop? What problem is it solving?

I · Initialization

What are the starting values of the variables?

C · Condition

What determines whether another iteration executes?

U · Update

Which values change during each iteration, and how?

O · Output

What does the program produce, and why?

For example, if somebody asks you to explain a loop that calculates the sum of natural numbers:

> The purpose of this loop is to calculate the sum of the first N natural numbers. We initialize the sum variable to zero and the loop counter to one. The loop continues while the counter is less than or equal to N. During every iteration, the current counter value is added to the accumulator. The counter is then incremented. Once the condition becomes false, the loop terminates and the accumulated sum is printed.

That's the kind of explanation I want you to develop naturally.

# 15 · Module 4 final revision checklist

## Q&A mastery tracker

Module 4

Loop fundamentals and terminology

For loop and execution order

While loop

Do-while loop

Nested loops

Break statement

Continue statement

Natural numbers and summation

Basic prime checking

Optimized prime checking

Nine code-reading drills

Descriptive questions

Technical vocabulary and spoken explanations

Revision progress

# 0%

0 of 13 sections reviewed.

## My recommended study sequence

1. First day: Study the definitions and understand the three loops.
2. Second day: Revise break, continue, nested loops, and summation.
3. Third day: Study prime checking and optimization. Practise all nine code-reading drills.
4. Fourth day: Attempt to explain five programs aloud without looking at the answers.

Don't aim to memorize 54 answers word for word. Understand the important terms, reproduce the definitions in your own English, and use Hinglish whenever it helps recover the meaning.

What I want you to achieve by the end of Module 4: You should be able to look at an unfamiliar loop, trace every iteration, predict its output, identify mistakes, explain its time complexity at a basic level, and teach its logic to another person.

Next, we'll run the DSA Mastery Lab assessment for Module 4, with unfamiliar questions, traps, debugging, tracing, and independent coding. I'll withhold the answers until you've submitted your first attempts. 🚀
English answer

Yes. A while loop is particularly useful when the number of iterations depends on a condition that may not be known in advance.

For example, repeatedly reading input until the user enters zero.

Hinglish explanation

Jab hume pehle se nahi pata ki loop kitni baar chalega, aur execution kisi condition par depend karta hai, tab while loop useful hota hai.

## 04 · Do-while loop

Q17. What is a do-while loop?

English answer

A do-while loop is an exit-controlled loop that executes its body before checking the condition. Therefore, its body executes at least once.

Syntax

```
do {
    // Loop body
} while (condition);
```

Hinglish explanation

Do-while pehle body execute karta hai aur baad mein condition check karta hai. Isliye condition initially false hone par bhi ek iteration zaroor hoti hai.

Q18. Why is a do-while loop called an exit-controlled loop?

English answer

It is called an exit-controlled loop because its continuation condition is checked after executing the loop body.

Hinglish explanation

Ismein condition end mein check hoti hai, jabki for aur while mein condition body se pehle check hoti hai. Isliye ise exit-controlled loop kehte hain.

Q19. What is the minimum number of iterations of a do-while loop?

English answer

The minimum number of iterations is one, regardless of whether the condition is initially true or false.

```
int i = 10;

do {
    cout << i;
} while (i < 5);
```

Output: `10`.

Hinglish explanation

Condition false hone ke baad bhi body pehle execute ho chuki hoti hai. Isliye minimum one iteration hoti hai.

Q20. What is the difference between while and do-while loops?

English answer

A while loop checks the condition before executing its body, whereas a do-while loop checks the condition after executing its body.

| While                  | Do-while               |
| ---------------------- | ---------------------- |
| Entry-controlled       | Exit-controlled        |
| May execute zero times | Executes at least once |
| Condition before body  | Condition after body   |

Hinglish explanation

While mein pehle condition check hoti hai. Do-while mein pehle body execute hoti hai. Ye dono ke beech ka main difference hai.

Q21. Why is a semicolon required after a do-while condition?

English answer

The do-while construct is defined with a terminating semicolon after its condition.

```
do {
    cout << "Hello";
} while (false);
```

Omitting the semicolon causes a syntax error.

Hinglish explanation

Do-while statement ka syntax semicolon ke saath complete hota hai. Isliye `while(condition);` likhna mandatory hai.

## 05 · Nested loops

Although nested loops aren't explicitly listed in the visible portion of your Sigma screenshot, they are an important extension of loop fundamentals, especially for patterns and 2D arrays.

Q22. What is a nested loop?

English answer

A nested loop is a loop placed inside the body of another loop. The inner loop completes its iterations for each iteration of the outer loop, unless control flow interrupts it.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 3; j++) {
        cout << "* ";
    }
    cout << '\n';
}
```

Output:

```
* * *
* * *
```

Hinglish explanation

Nested loop ka matlab ek loop ke andar doosra loop. Outer loop ki har iteration par inner loop apni complete iterations perform karta hai.

Q23. How many times does an inner loop execute in a nested loop?

English answer

The inner loop executes its complete set of iterations for every iteration of the outer loop, assuming no early termination.

If the outer loop executes 3 times and the inner loop executes 4 times per outer iteration, the inner body executes:

\\[ 3 \times 4 = 12 \\]

Hinglish explanation

Outer loop ki har iteration par inner loop dobara start hota hai. Agar outer 3 baar aur inner har baar 4 baar chale, toh total 12 inner iterations hongi.

Q24. What is the difference between the outer loop and inner loop?

English answer

The outer loop controls the larger repetition structure, while the inner loop performs repeated operations within each outer iteration.

Hinglish explanation

Outer loop overall rounds control karta hai. Inner loop har outer round ke andar repeated work perform karta hai.

Q25. How are nested loops useful in pattern printing?

English answer

Nested loops are used to control rows and columns when generating patterns. The outer loop commonly controls the rows, while the inner loop controls the elements printed in each row.

```
for (int i = 1; i <= 3; i++) {
    for (int j = 1; j <= 4; j++) {
        cout << "* ";
    }
    cout << '\n';
}
```

Hinglish explanation

Pattern printing mein outer loop rows control karta hai aur inner loop har row mein kitne stars ya numbers print honge, woh control karta hai.

## 06 · Break statement

Q26. What is the break statement?

English answer

The `break` statement immediately terminates the nearest enclosing loop or switch statement and transfers control to the statement following it.

```
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        break;
    }
    cout << i << '\n';
}
```

Output: `1 2`.

Hinglish explanation

Break execute hote hi nearest loop terminate ho jaata hai. Program loop ke baad wale statement par chala jaata hai.

Q27. What happens to the remaining iterations after break executes?

English answer

All remaining iterations of that loop are skipped because the loop terminates immediately.

Hinglish explanation

Break execute hone ke baad loop ki remaining iterations nahi chalti. Loop wahi khatam ho jaata hai.

Q28. What happens when break is used inside nested loops?

English answer

A break statement terminates only the nearest enclosing loop or switch, not every surrounding loop.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 3; j++) {
        if (j == 2) {
            break;
        }
        cout << i << "," << j << '\n';
    }
}
```

Output:

```
1,1
2,1
```

Hinglish explanation

Nested loop mein break sirf inner loop ko terminate karega. Outer loop apni next iteration continue karega.

Important trap

Break does not automatically terminate all nested loops.

## 07 · Continue statement

Q29. What is the continue statement?

English answer

The `continue` statement skips the remaining statements in the current loop iteration and transfers control to the next iteration of the loop.

```
for (int i = 1; i <= 5; i++) {
    if (i == 3) {
        continue;
    }
    cout << i << '\n';
}
```

Output: `1 2 4 5`.

Hinglish explanation

Continue current iteration ka remaining code skip karta hai aur next iteration par le jaata hai. Loop terminate nahi hota.

Q30. What happens after continue executes in a for loop?

English answer

The update expression executes, and then the loop condition is checked again.

Hinglish explanation

For loop mein continue ke baad update expression execute hota hai, phir condition check hoti hai.

Q31. What happens after continue executes in a while loop?

English answer

Control returns directly to the condition check. Any update statement placed later in the loop body is skipped.

Hinglish explanation

While loop mein continue ke baad direct condition check hoti hai. Agar update statement continue ke neeche hai, toh woh skip ho jaayega.

Important trap

```
int i = 1;

while (i <= 5) {
    if (i == 3) {
        continue;
    }
    i++;
}
```

This becomes an infinite loop when `i` reaches 3, because the update is skipped and the condition remains true.

Q32. What is the difference between break and continue?

English answer

`break` terminates the nearest enclosing loop completely. `continue` skips the current iteration and proceeds to the next iteration.

Hinglish explanation

Break poora loop stop karta hai, jabki continue sirf current round skip karta hai.

## 08 · Natural numbers and summation

Q33. What are natural numbers?

English answer

Natural numbers are counting numbers. They are commonly represented as 1, 2, 3, 4, and so on. Some mathematical conventions include zero, so the convention should be stated when relevant.

Hinglish explanation

Natural numbers counting numbers hote hain, jaise 1, 2, 3, 4... Is course mein generally 1 se counting start karenge.

Q34. How can we print the first N natural numbers using a for loop?

English answer

Initialize a loop variable to 1 and continue executing the loop while it is less than or equal to N.

```
int n = 5;

for (int i = 1; i <= n; i++) {
    cout << i << " ";
}
```

Output: `1 2 3 4 5`.

Hinglish explanation

i ko 1 se start karte hain aur jab tak i, n se chhota ya equal hai, print karte hain. Har iteration ke baad i increment hota hai.

Q35. How do you calculate the sum of the first N natural numbers using a loop?

English answer

Initialize a variable `sum` to zero, then repeatedly add each natural number to it.

```
int n = 5;
int sum = 0;

for (int i = 1; i <= n; i++) {
    sum += i;
}

cout << sum;
```

Output: `15`.

Hinglish explanation

Sum variable ko initially zero rakhte hain. Har iteration mein current i ko sum mein add karte hain. End mein total 15 milta hai.

Q36. Why should the sum variable be initialized to zero?

English answer

Zero is the additive identity. Adding zero to a number does not change its value, making it the correct starting value for accumulating a sum.

Hinglish explanation

Zero se addition start karne par original number change nahi hota. Isliye sum calculate karne ke liye initial value zero rakhte hain.

Q37. What is an accumulator variable?

English answer

An accumulator is a variable that stores and progressively updates a running result across multiple iterations.

For example, `sum` accumulates the total of natural numbers.

Hinglish explanation

Accumulator aisa variable hota hai jisme har iteration ka result add ya combine hota rehta hai. Jaise sum variable continuously total calculate karta hai.

## 09 · Prime numbers

Q38. What is a prime number?

English answer

A prime number is a natural number greater than 1 that has exactly two distinct positive divisors: 1 and itself.

Examples: 2, 3, 5, 7, 11, 13.

Hinglish explanation

Prime number 1 se bada natural number hota hai jiske exactly do positive factors hote hain: 1 aur woh number khud.

Q39. What is a composite number?

English answer

A composite number is a natural number greater than 1 that has more than two distinct positive divisors.

Examples: 4, 6, 8, 9, 10, 12.

Hinglish explanation

Composite number ke do se zyada positive factors hote hain. Jaise 6 ke factors 1, 2, 3 aur 6 hain.

Q40. Why is 1 neither prime nor composite?

English answer

The number 1 has only one positive divisor, itself. A prime number must have exactly two distinct positive divisors, while a composite number must have more than two.

Hinglish explanation

Number 1 ka sirf ek positive factor hai. Prime ke liye exactly do factors aur composite ke liye do se zyada factors chahiye. Isliye 1 dono mein nahi aata.

Q41. How can we check whether a number is prime using a basic loop?

English answer

We check whether any integer from 2 through `n - 1` divides the number exactly. If a divisor is found, the number is not prime. Otherwise, it is prime, provided `n` is greater than 1.

```
int n = 13;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i < n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

cout << (isPrime ? "Prime" : "Not Prime");
```

Output: `Prime`.

Hinglish explanation

2 se n-1 tak divisors check karte hain. Agar koi number completely divide kar deta hai, toh number prime nahi hai. Agar koi divisor nahi milta aur n, 1 se bada hai, toh number prime hai.

Q42. Why do we use the modulo operator in prime checking?

English answer

The modulo operator `%` calculates the remainder of integer division. If `n % i == 0`, then `i` divides `n` exactly and is a divisor.

Hinglish explanation

Modulo remainder deta hai. Agar `n % i == 0` hai, toh i, n ko completely divide karta hai. Iska matlab hume ek divisor mil gaya.

Q43. Why is the break statement useful in prime checking?

English answer

Once a divisor is found, there is no need to check additional values because the number is already known to be non-prime. `break` terminates the loop immediately.

Hinglish explanation

Ek divisor milte hi prove ho jaata hai ki number prime nahi hai. Isliye baaki numbers check karne ki zarurat nahi, aur break loop stop kar deta hai.

## 10 · Optimized prime checking

Q44. Why is checking divisors only up to the square root of N sufficient?

English answer

If a number has a factor greater than its square root, it must have a corresponding factor smaller than its square root. Therefore, checking all possible divisors beyond the square root is unnecessary.

Hinglish explanation

Agar kisi number ka ek factor square root se bada hai, toh uska doosra corresponding factor square root se chhota hoga. Woh smaller factor pehle hi check ho chuka hoga. Isliye square root tak check karna sufficient hai.

Q45. What is the time complexity of basic prime checking?

English answer

The basic algorithm checks up to `n - 1` possible divisors in the worst case. Its time complexity is \\(O(n)\\).

Hinglish explanation

Basic approach worst case mein n ke proportional number of divisors check karta hai. Isliye time complexity O(n) hai.

Q46. What is the time complexity of optimized prime checking?

English answer

The optimized algorithm checks possible divisors only up to the square root of N. Its time complexity is \\(O(\sqrt n)\\).

Hinglish explanation

Optimized approach sirf square root tak check karta hai, isliye complexity O(root n) ho jaati hai.

Q47. What is the difference between the basic and optimized prime-checking algorithms?

| Basic              | Optimized              |
| ------------------ | ---------------------- |
| Checks up to `n-1` | Checks up to `sqrt(n)` |
| \\(O(n)\\)         | \\(O(\sqrt n)\\)       |
| More iterations    | Fewer iterations       |
| Simpler but slower | More efficient         |

Hinglish: Dono algorithms prime check karte hain, lekin optimized algorithm unnecessary checks remove karke faster execution deta hai.

Q48. Why can we use `i * i <= n` instead of `i <= sqrt(n)`?

English answer

Comparing `i * i` with `n` avoids repeatedly calculating a square root and expresses the same mathematical boundary for positive integer inputs.

```
for (int i = 2; i * i <= n; i++)
```

For large integers, use `i <= n / i` to avoid possible multiplication overflow.

Hinglish explanation

`i * i <= n` square root boundary ko directly represent karta hai. Isse sqrt function baar-baar calculate karne ki zarurat nahi. Very large values ke liye overflow ka dhyan rakhna chahiye.

# 11 · Code-reading and explanation studio 🎙️

This is the most important practical section of your handbook.

I want you to develop the ability to look at unfamiliar code and mentally follow its execution. Don't just memorize the output. Understand how the program reaches that output.

For each example, I'll provide:

- The complete code.
- A line-by-line English explanation.
- A Hinglish explanation.
- A dry-run table where useful.
- The output and reasoning.

## Drill 1 · Print N natural numbers

Code

```
int n = 5;

for (int i = 1; i <= n; i++) {
    cout << i << " ";
}
```

Line-by-line explanation

| Code         | What it does                                                 |
| ------------ | ------------------------------------------------------------ |
| `int n = 5;` | Declares an integer and initializes it to 5.                 |
| `int i = 1;` | Declares the loop variable and sets its starting value to 1. |
| `i <= n`     | Checks whether the current value is within the limit.        |
| `i++`        | Increments i by one after each iteration.                    |
| `cout << i`  | Prints the current value of i.                               |

Dry run

| Iteration | i | Condition | Output |
| --------- | - | --------- | ------ |
| 1         | 1 | True      | 1      |
| 2         | 2 | True      | 2      |
| 3         | 3 | True      | 3      |
| 4         | 4 | True      | 4      |
| 5         | 5 | True      | 5      |
| Exit      | 6 | False     | None   |

Output: 1 2 3 4 5

Hinglish explanation

N ki value 5 hai. Loop variable i, 1 se start hota hai. Jab tak i, n se chhota ya equal hai, current value print hoti hai. Har iteration ke baad i increment hota hai. i = 6 hone par condition false ho jaati hai aur loop terminate hota hai.

## Drill 2 · Sum of natural numbers

Code

```
int n = 4;
int sum = 0;

for (int i = 1; i <= n; i++) {
    sum = sum + i;
}

cout << sum;
```

Line-by-line explanation

1. `int n = 4;` establishes the upper limit.
2. `int sum = 0;` creates an accumulator and initializes it to zero.
3. `int i = 1;` initializes the loop counter.
4. `i <= n` checks whether the loop should continue.
5. `sum = sum + i;` adds the current value of i to the accumulated total.
6. `i++` moves to the next natural number.
7. When the loop finishes, `cout` prints the accumulated sum.

Dry run

| Iteration | i | Previous sum | New sum |
| --------- | - | ------------ | ------- |
| 1         | 1 | 0            | 1       |
| 2         | 2 | 1            | 3       |
| 3         | 3 | 3            | 6       |
| 4         | 4 | 6            | 10      |

Output: 10

Hinglish explanation

Sum initially zero hai. Har iteration mein current i ki value sum mein add hoti hai. Pehle 1, phir 2, phir 3 aur phir 4 add hota hai. Final sum 10 hota hai.

## Drill 3 · While loop with a changing condition

Code

```
int i = 10;

while (i > 0) {
    cout << i << " ";
    i -= 2;
}
```

Line-by-line explanation

1. Initialize the variable `i` to 10.
2. Check whether `i` is greater than zero.
3. If true, print the current value.
4. Subtract 2 from i using the compound assignment operator.
5. Return to the condition check.
6. When i becomes zero, the condition becomes false and the loop exits.

Dry run

| Iteration | i before | Output | i after |
| --------- | -------- | ------ | ------- |
| 1         | 10       | 10     | 8       |
| 2         | 8        | 8      | 6       |
| 3         | 6        | 6      | 4       |
| 4         | 4        | 4      | 2       |
| 5         | 2        | 2      | 0       |
| Exit      | 0        | None   | 0       |

Output: 10 8 6 4 2

Hinglish explanation

i ki starting value 10 hai. Jab tak i zero se bada hai, print hota rahega. Har iteration mein 2 subtract hoga. Zero hone par loop stop ho jaayega.

## Drill 4 · Do-while with a false condition

Code

```
int i = 10;

do {
    cout << i << '\n';
    i++;
} while (i < 5);
```

Line-by-line explanation

1. Initialize i to 10.
2. Enter the do-while body without checking the condition first.
3. Print 10.
4. Increment i to 11.
5. Check whether `i < 5`.
6. The condition is false, so the loop terminates.

Output: 10

Hinglish explanation

Do-while pehle body execute karta hai. Isliye 10 print hota hai. Phir i increment hokar 11 ho jaata hai. Condition false hone par loop stop ho jaata hai.

## Drill 5 · Break in a loop

Code

```
for (int i = 1; i <= 10; i++) {

    if (i == 6) {
        break;
    }

    cout << i << " ";
}

cout << "\nFinished";
```

Line-by-line explanation

1. Initialize i to 1.
2. Check whether i is less than or equal to 10.
3. Evaluate `i == 6` in the if statement.
4. If i is not 6, print its value.
5. When i reaches 6, the if condition becomes true.
6. The break statement immediately terminates the loop.
7. Execution continues after the loop and prints `Finished`.

Output: 1 2 3 4 5, then Finished

Hinglish explanation

Loop 1 se start hota hai aur numbers print karta hai. Jab i ki value 6 hoti hai, if condition true hoti hai aur break execute hota hai. Loop terminate hokar Finished print karta hai.

## Drill 6 · Continue in a for loop

Code

```
for (int i = 1; i <= 5; i++) {

    if (i == 3) {
        continue;
    }

    cout << i << " ";
}
```

Line-by-line explanation

1. Initialize i to 1.
2. Check whether i is within the limit.
3. If i equals 3, execute continue.
4. Continue skips the remaining statements of the current iteration.
5. In this for loop, control moves to the update expression.
6. The loop continues with i = 4.
7. The program prints all values except 3.

Output: 1 2 4 5

Hinglish explanation

Jab i ki value 3 hoti hai, continue execute hota hai aur cout skip ho jaata hai. For loop mein uske baad i increment hota hai. Isliye 3 print nahi hota, lekin loop continue karta hai.

## Drill 7 · Nested loops and pattern printing

Code

```
for (int i = 1; i <= 3; i++) {

    for (int j = 1; j <= 3; j++) {
        cout << "* ";
    }

    cout << '\n';
}
```

Line-by-line explanation

1. The outer loop initializes `i` to 1 and controls the number of rows.
2. For every outer iteration, the inner loop initializes `j` to 1.
3. The inner loop prints three stars because j takes the values 1, 2, and 3.
4. After the inner loop completes, the newline statement moves the cursor to the next row.
5. The outer loop increments i and starts another row.
6. This process repeats until the outer loop finishes its three iterations.

Output

```
* * *
* * *
* * *
```

Dry run summary

| Outer iteration | Inner iterations | Stars printed |
| --------------- | ---------------- | ------------- |
| 1               | 3                | 3             |
| 2               | 3                | 3             |
| 3               | 3                | 3             |
| Total           | 9                | 9             |

Hinglish explanation

Outer loop three rows control karta hai. Har row ke liye inner loop three stars print karta hai. Inner loop complete hone ke baad newline execute hota hai. Is tarah three rows aur three columns ka pattern banta hai.

## Drill 8 · Basic prime checking

Code

```
int n = 9;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i < n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

if (isPrime) {
    cout << "Prime";
} else {
    cout << "Not Prime";
}
```

Line-by-line explanation

1. Initialize `n` to 9.
2. Initialize the Boolean variable `isPrime` to true, assuming the number is prime until a divisor proves otherwise.
3. Check whether n is less than or equal to 1. Since n is 9, this condition is false.
4. Start the for loop with i equal to 2.
5. Check whether `n % i == 0`.
6. When i equals 3, the remainder becomes zero.
7. This proves that 9 has a divisor other than 1 and itself.
8. Set `isPrime` to false.
9. Execute break because additional divisor checks are unnecessary.
10. The final if-else checks `isPrime` and prints `Not Prime`.

Output: Not Prime

Hinglish explanation

9 se start karte hain aur isPrime ko initially true rakhte hain. Divisors check karte waqt 3 milta hai jo 9 ko completely divide karta hai. Isliye isPrime false ho jaata hai aur break loop stop kar deta hai. Final output Not Prime hota hai.

## Drill 9 · Optimized prime checking

Code

```
int n = 29;
bool isPrime = true;

if (n <= 1) {
    isPrime = false;
}

for (int i = 2; i * i <= n; i++) {
    if (n % i == 0) {
        isPrime = false;
        break;
    }
}

cout << (isPrime ? "Prime" : "Not Prime");
```

Line-by-line explanation

1. Initialize n to 29.
2. Assume the number is prime initially.
3. Reject numbers less than or equal to 1.
4. Initialize the divisor-checking variable i to 2.
5. The condition `i * i <= n` restricts the search to possible divisors up to the square root of n.
6. Check whether the remainder of `n / i` is zero.
7. If a divisor is found, mark the number as non-prime and exit the loop.
8. If no divisor is found, `isPrime` remains true.
9. The ternary operator selects the appropriate output string.

For n = 29, the loop checks:

| i | i × i | Condition        | Divisor? |
| - | ----- | ---------------- | -------- |
| 2 | 4     | 4 ≤ 29           | No       |
| 3 | 9     | 9 ≤ 29           | No       |
| 4 | 16    | 16 ≤ 29          | No       |
| 5 | 25    | 25 ≤ 29          | No       |
| 6 | 36    | 36 ≤ 29 is false | Stop     |

Output: Prime

Hinglish explanation

29 ke liye hum divisors 2 se check karna start karte hain. Condition `i * i <= n` hume square root tak hi checking karne deti hai. Koi divisor nahi milta, isliye number prime hai.

# 12 · Descriptive questions for exams and revision

These questions are particularly useful for written examinations and explaining concepts without code.

Q49. Explain the different types of loops in C++.

English answer

C++ provides three main types of loops:

1. For loop: Used when the repetition structure can conveniently be controlled using initialization, condition, and update in one statement.
2. While loop: Used when repetition depends on a condition checked before each iteration.
3. Do-while loop: Used when the body must execute at least once before checking the condition.

Hinglish explanation

For loop mein initialization, condition aur update ek saath likhte hain. While mein pehle condition check hoti hai. Do-while mein pehle body execute hoti hai.

Q50. Differentiate between break and continue statements.

English answer

The break statement terminates the nearest enclosing loop or switch, whereas the continue statement skips the remaining statements in the current loop iteration and proceeds to the next iteration.

Hinglish explanation

Break poora nearest loop stop karta hai. Continue sirf current iteration skip karta hai aur next iteration par le jaata hai.

Q51. Explain nested loops with an example.

English answer

A nested loop is a loop placed inside another loop. The inner loop executes its iterations for every iteration of the outer loop.

```
for (int i = 1; i <= 2; i++) {
    for (int j = 1; j <= 2; j++) {
        cout << i << "," << j << '\n';
    }
}
```

Output:

```
1,1
1,2
2,1
2,2
```

Hinglish explanation

Inner loop outer loop ke har round mein complete execute hota hai. Is example mein outer two times aur inner har baar two times chalta hai.

Q52. Explain the algorithm for checking whether a number is prime.

English answer

To check whether a number is prime:

1. Read the input number.
2. If it is less than or equal to 1, classify it as non-prime.
3. Check possible divisors starting from 2.
4. If any divisor divides the number exactly, classify it as non-prime.
5. Otherwise, classify it as prime.

Hinglish explanation

Pehle n check karte hain. Agar n, 1 ya usse chhota hai toh non-prime. Otherwise divisors check karte hain. Koi divisor mil gaya toh non-prime, warna prime.

Q53. Explain the optimization used in prime number checking.

English answer

The optimized prime-checking algorithm examines divisors only up to the square root of the input number. This works because every factor pair of a number must contain at least one factor less than or equal to its square root. This reduces the time complexity from \\(O(n)\\) to \\(O(\sqrt n)\\).

Hinglish explanation

Hume square root se aage divisors check karne ki zarurat nahi. Agar koi factor square root se bada hai toh uska corresponding smaller factor pehle mil chuka hoga. Isse algorithm faster ho jaata hai.

Q54. What is the difference between entry-controlled and exit-controlled loops?

English answer

An entry-controlled loop checks its condition before executing the loop body. A do-while loop is exit-controlled because it checks the condition after executing the body.

Hinglish explanation

Entry-controlled loops mein pehle condition check hoti hai. Exit-controlled loop mein pehle body execute hoti hai aur baad mein condition check hoti hai.

# 13 · Technical vocabulary dictionary

These are terms I particularly want you to become comfortable using while explaining your code.

| Technical term   | Meaning                                              |
| ---------------- | ---------------------------------------------------- |
| Iteration        | One execution of a loop body                         |
| Loop counter     | Variable that tracks iterations                      |
| Initialization   | Setting the initial value                            |
| Condition        | Expression evaluated as true or false                |
| Update           | Changing a variable's value                          |
| Termination      | Ending the loop                                      |
| Infinite loop    | Loop that does not terminate naturally               |
| Accumulator      | Variable that maintains a running result             |
| Nested loop      | Loop inside another loop                             |
| Divisor          | Number that divides another number exactly           |
| Remainder        | Amount left after division                           |
| Prime number     | Number with exactly two distinct positive divisors   |
| Composite number | Number with more than two distinct positive divisors |
| Optimization     | Improving resource efficiency                        |
| Time complexity  | How execution requirements grow with input size      |
| Entry-controlled | Condition checked before the body                    |
| Exit-controlled  | Condition checked after the body                     |
| Control flow     | Order in which program statements execute            |

# 14 · How to explain code like an engineer

For Module 4, I want you to adopt this five-part explanation framework.

## The L-I-C-U-O framework

A speaking structure for explaining any loop

L · Logic

What is the purpose of the loop? What problem is it solving?

I · Initialization

What are the starting values of the variables?

C · Condition

What determines whether another iteration executes?

U · Update

Which values change during each iteration, and how?

O · Output

What does the program produce, and why?

For example, if somebody asks you to explain a loop that calculates the sum of natural numbers:

> The purpose of this loop is to calculate the sum of the first N natural numbers. We initialize the sum variable to zero and the loop counter to one. The loop continues while the counter is less than or equal to N. During every iteration, the current counter value is added to the accumulator. The counter is then incremented. Once the condition becomes false, the loop terminates and the accumulated sum is printed.

That's the kind of explanation I want you to develop naturally.

# 15 · Module 4 final revision checklist

## Q&A mastery tracker

Module 4

Loop fundamentals and terminology

For loop and execution order

While loop

Do-while loop

Nested loops

Break statement

Continue statement

Natural numbers and summation

Basic prime checking

Optimized prime checking

Nine code-reading drills

Descriptive questions

Technical vocabulary and spoken explanations

Revision progress

# 0%

0 of 13 sections reviewed.

## My recommended study sequence

1. First day: Study the definitions and understand the three loops.
2. Second day: Revise break, continue, nested loops, and summation.
3. Third day: Study prime checking and optimization. Practise all nine code-reading drills.
4. Fourth day: Attempt to explain five programs aloud without looking at the answers.

Don't aim to memorize 54 answers word for word. Understand the important terms, reproduce the definitions in your own English, and use Hinglish whenever it helps recover the meaning.
