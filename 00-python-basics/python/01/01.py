# # Ask User for their name

# name = input("Whats Your Name? ")

# # Say Hello to user
# print("Hello,",name)

# # Print bye
# print("Bye")
# #length of name
# print(len(name))
# #Print Experiments

# #remove white space from string and capitalize
# name = name.strip().title()

# #split user's name into first name and last name
# first , last = name.split(" ")

# # print("Hello,", name, sep="")

# print(f"Hello, {first}")


# Calculator

# x = float(input("Whats x? "))
# y = float(input("Whats y? "))

# z = round(x+y)
# print(z)


# def hello(to="world"):
#     print("hello,", to)

# def square(n):
#     return pow(n,2)


# functions


# def main():



# Indoor Voice

# name = input("Write Anything: ").lower()
# print(name)

#playback

# name = input("Write Anything: ").replace(" ", "...")
# print(name)

#making faces

    # def convert():
    #     replace(":)", "🙂")
    #     replace(":(", "🙁")
    
# emoji = convert(":(")
# convert()
# print("Hello :)")

#einstein

    # c = 300000000
# m = int(input("Enter Mass: "))
# E = m*c*c
# print("E = ",E,"Joules")



#Tip Calculator
#     dollars = dollars_to_float(input("How much was the meal?(in dollars) "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"leave ${tip:2f}")

# def dollars_to_float(d):
#     return float(d)

# def percent_to_float(p):
#     return float(p)/100

# main()

# b = ':'
# c = ")"
# s1 = b + 2*c

# f = "a"
# g = "b"
# h = "3"
# s2 = (f+g+h)*int(h)
# print(s1, s2) 

# verb = input("Choose a Verb: ")
# print(f"I can {verb} better than you!")
# print((verb+" ") *5)

# num = int(input("Number: "))
# if num >0:
#     print("Positive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")

# yearly_salary = float(input("Yearly Salary: "))
# portion_saved = float(input("Portion Saved(10% = 0.1): "))
# cost_of_dream_home = float(input("Cost Of Dream Home: "))
# semi_annual_raise = float(input("Semi Annul Raise(0.1 for 10%): "))
# portion_down_payment = 0.25 # 25% Down Payment Required
# amount_saved = 0.0 #Starting Savings
# r = 0.05 #Annual Rate of return(5%)


# # Calculate Required Down Payment Target
# total_down_payment = cost_of_dream_home * portion_down_payment
# months = 0

# while amount_saved < total_down_payment:
#     # 1. Calculate monthly salary and monthly deposit based on current yearly_salary
#     monthly_salary = yearly_salary / 12
#     monthly_saving = monthly_salary * portion_saved
    
#     # 2. Calculate monthly investment return using amount saved at START of month
#     monthly_return = amount_saved * (r/12)
#     amount_saved +=monthly_saving + monthly_return
#     # 3. Increment Month Counter
#     months += 1
#     if months%6 == 0:
#         yearly_salary += yearly_salary*semi_annual_raise

# print(f"Months: {months}")


# secret_word = input("Secret Word: ")

# first = secret_word[0]
# last = secret_word[-1]
# middle = secret_word[(len(secret_word)//2)]

# result = (first + middle + last).upper()
# print(result)

# # String Slicing And Palindrome

# my_string = "racecar"
# reversed_string = my_string[::-1] # Revese the String
# print("Palindrome" if my_string == reversed_string else "Not Palindrome")



# Largest of Odd
# x = int(input("X = "))
# y = int(input("Y = "))
# z = int(input("Z = "))


# if x%2!=0 and y%2 != 0 and z%2 != 0:
#     print(max(x,y,z))
# if x%2!=0 and y%2 != 0 and z%2 == 0:
#     print(max(x,y))
# if x%2!=0 and y%2 == 0 and z%2 != 0:
#     print(max(x,z))
# if x%2==0 and y%2 != 0 and z%2 != 0:
#     print(max(y,z))
# if x%2!=0 and y%2 == 0 and z%2 == 0:
#     print(x)
# if x%2==0 and y%2 != 0 and z%2 == 0:
#     print(z)
# if x%2==0 and y%2 == 0 and z%2 != 0:
#     print(z)
# if x%2==0 and y%2 == 0 and z%2 == 0:
#     print(min(x,y,z))

# answer = min(x,y,z)
# if x%2 != 0:
#     answer = x
# if y%2 != 0 and y>answer:
#     answer = y
# if z%2 != 0 and z>answer:
#     answer = z 
# print(answer)

###################
# Tou can uncomment each of these examples
# and try running them yourself

# To batch comment/uncomment, select the lines and then
# on Windows hit CTRL+1 or on Mac hit CMD+1
###################



###################
# EXAMPLE: while loops 
####################
# where = input("You are in the Lost Forest. Go left or right? ")
# while where == "right":
#     where = input("You are in the Lost Forest. Go left or right? ")
# print("You got out of the Lost Forest! \o/")



###########################################

# Fun Lost Forest code, run it on your own!
#where = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while where.lower() == "right":
#    where = input("You are in the Lost Forest\n****************\n******       ***\n  (â•¯Â°â–¡Â°ï¼‰â•¯\n     ï¸µ \n    â”»â”â”»\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")

    
###########
## EXAMPLE    
###########
# n = int(input('Please enter a non-negative integer: '))
# while n > 0:
#     print('x')
#     n = n-1  # the same as n -= 1
    

################ YOU TRY IT ###################
## EXAMPLE: infinite loop, be careful!
# To stop it, click the shell and hit CTRL+c or 
# the red square at the top of the shell
##############################################
# while True:
#     print("noooooooo")



############### YOU TRY IT ################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# sad = ":("
# i = 1
# while where == "right":
    
#     if i>2: print(sad)
#     where = input("Go left or right? ")
#     i+=1
# print("You got out!")


# fact = 1
# n = int(input("Number: "))
# i = 1
# while(i<=n):
#     fact *= i
#     i+=1

#############
## EXAMPLE: counter
#############

## With while loop
# n = 0
# while n < 5:
#     print(n)
#     n = n+1

## With for loop
#for n in range(5):
#    print(n)

###########
## EXAMPLE: factorial
###########

## With while loops
# x = 6
# i = 1
# factorial = 1
# while i <= x:
#     factorial *= i
#     i += 1
# print(f'{x} factorial is {factorial}')

## With for loops
# factorial = 1
# # for i in range(1, x+1, 1):
# #     factorial *= i
# # print(f'{x} factorial is {factorial}')

# for i in range(1, 4, 1):
#     factorial *=i
# print(f"factorial: {factorial}")

################ YOU TRY IT ################
# for i in range(1,4,1):
#     print(i)
# for j in range(1,4,2):
#     print(j*2)
# for me in range(4,0,-1):
#     print("$"*me)


###########################################

###############
## EXAMPLE: sum
###############

#mysum = 0
#for i in range(10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(7, 10):
#    mysum += i
#print(mysum)

######

#mysum = 0
#for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
#print(mysum)

################ YOU TRY IT ################
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 3
# end = 5
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

###########################################



#########################################################
##################### AT HOME ###########################
#########################################################

# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.
# x = int(input("X = "))
# i = 5
# while (i<=x):
#     if i%5 == 0:
#         print(i)
#     i+=5
# for _ in range(5,x+1,5):
#     print(_)



# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
x = int(input("X = "))
sum = 0
while(x>0):
    last = x%10
    sum +=  last
    x//=10

print(sum)



#########################################################
##################### END AT HOME ###########################
#########################################################


#########################################################
##################### ANSWERS AT HOME ###########################
#########################################################

# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. If x = 14, it prints 5 and 10.

# x = 15
# for i in range(1,x+1):
#     if i%5 == 0:
#         print(i)


# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
# n = 1234
# total = 0
# while True:
#     r = n%10
#     total += r 
#     n = n//10
#     if n == 0:
#         break
# print(total)

#########################################################
##################### END ANSWERS AT HOME ###########################
#########################################################




#########################################
############### ANSWERS TO LECTURE ##########################
#########################################
# You Try It 1: 
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
###################
# where = input("Go left or right? ")
# counter = 0
# while where == "right":
#     counter = counter + 1
#     if counter > 2:
#         print(":(")
#     where = input("Go left or right? ")
# print("You got out!")



# Your Try It 2: 
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 

# mysum = 0
# start = 1
# end = 3
# for i in range(start, end+1):
#     mysum += i
# print(mysum)

#########################################
############### END ANSWERS TO LECTURE ##########################
#########################################



