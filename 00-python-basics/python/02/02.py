# x = 10
# y = 15

# if x!=y:
#     print("X is not equal y")
# else:
#     print("x is equal to y")

# AND

# score = int(input("Score: "))

# if score >=90 and score <=100:
#     print("Grade: A")
# elif score>=80 and score<90:
#     print("Grade: B")
# elif score>=70 and score<80:
#     print("Grade: C")
# elif score>=60 and score<70:
#     print("Grade: D")
# else:
#     print("Grade: F")


#Slightly Optimized
# if score >=90 and score <=100:
#     print("Grade: A")
# elif score>=80 and score<90:
#     print("Grade: B")
# elif score>=70 and score<80:
#     print("Grade: C")
# elif score>=60 and score<70:
#     print("Grade: D")
# else:
#     print("Grade: F")

#Optimized

# if score >=90:
#     print("Grade: A")
# elif score>=80:
#     print("Grade: B")
# elif score>=70:
#     print("Grade: C")
# elif score>=60:
#     print("Grade: D")
# else:
#     print("Grade: F")

# def main():
#     x = int(input("What's x? "))
#     print(is_even(x))

# def is_even(n):
#     return n%2==0

# Deep Thought
    # ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    # if ans in ["42" ,"forty-two" ,"forty two"]:
    #     print("Yes")
    # else:
    #     print("No")
    
    # Home Fedral

    # greeting = input("Greeting: ").strip().lower()
    # if greeting.startswith("hello"):
    #     print("$",0)
    # elif greeting.startswith("h") and greeting != "hello":
    #     print("$",20)
    # else: 
    #     print("$",100)

    # file extension
    # file = input("File name: ").strip().lower()
    # if file.endswith(".gif"):
    #     print("image/gif")
    # elif file.endswith(".jpg"):
    #     print("image/jpg")
    # elif file.endswith(".jpeg"):
    #     print("image/jpeg")
    # elif file.endswith(".png"):
    #     print("image/png")
    # elif file.endswith(".pdf"):
    #     print("application/pdf")
    # elif file.endswith(".text"):
    #     print("text/txt")
    # elif file.endswith(".zip"):
    #     print("application/zip")
    # else:
    #     print("application/octet-stream")

    # Math Interpreter
    # expr = input("Expression: ").strip()
    # x, y, z = expr.split(" ")
    # x, z = float(x), float(z)
    # if y == "+":
    #     print(f"{x+z:.1f}")
    # elif y == "-":
    #     print(f"{x-z:.1f}")
    # elif y == "*":
    #     print(f"{x*z:.1f}")
    # elif y == "/": 
    #     print(f"{x/y}:.1f")
    # Math Interpreter
    # expr = input("Expression: ").strip()
    # x, y, z = expr.split(" ")
    # x, z = float(x), float(z)
    # if y == "+": res = x+z
    # elif y == "-": res = x-z
    # elif y == "*": res = x*z
    # elif y == "/": res = x/z
    # print(f"{res:.1f}")

    # Meal Time

    # def convert(time):
    #     hour, minute = time.split(":")
    #     return float(hour) + (float(minute)/60.0)
    
    # t = convert(input('Time: ').strip())
    # if 7.0<= t <=8.0: print("Breakfast Time")
    # elif 12.0 <= t <=13.0: print("Lunch Time")
    # elif 18.0 <= t <=19.0: print("Dinner Time")
# main() 



# num_x = int(input('How many times should I print the letter X? '))
# #concatenate X to to_print num_x times
# x = 1
# to_print = ''
# while(x<=num_x):
#     to_print = to_print + 'X'
#     x+=1
# print(to_print)

# while len(to_print)< num_x:
#     to_print += 'X'
# print(to_print)


# numbers = input("Enter 10 Numbers: ").strip()

# numbers = numbers.split(" ")
# print("Enter 10 Numbers")
# n = 1
# largest = None
# while(n<=10):
#     num = int(input(f"Number {n}:"))
#     if num % 2 != 0:
#         if largest is None:
#             largest = num
#         else:
#             largest = max(largest, num)
#     n+=1
    
# print(f"Largest = {largest}" if largest is not None else "No Odd Numbers")

# total = 0
# for i in range(3, 1000, 2):
#     isPrime = True
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             isPrime = False
#     if isPrime:
#         total += i
    
    
# print(total)

#P3 Descending range() with Inclusive Lower Bound and Parity Tracking

# high= 10
# low = 2
# step = 2
# even_count = 0
# even_sum = 0

# for i in range(high, low-1, -step):
#     if i%2 == 0:
#         even_count += 1
#         even_sum += i
# print(even_count, even_sum)
    

#P4 Iterative Multiplicative Power Without * or **

# base = int(input("Base: "))
# exp = int(input("Exp: "))

# result = 1 # Handles exp = cleanly

# for i in range(exp):
#     #Compute Product  = result * base using repeated addition
#     product = 0
#     for i in range(base):
#         product += result
#     result = product

# print(f"Result: {result}")
# result = 1
# for i in range(4):
#     product = 0
#     for j in range(3):
#         product += result
#     result = product

steps = 0
n = 6
while n!=1:
    if n%2 == 0:
        n//=2
    else:
        n = 3*n+1
    steps+=1
print(steps)