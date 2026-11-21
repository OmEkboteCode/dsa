# while
# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# while i <= 6:
#     print(i)
#     if i == 3:
#         break
#     i+=1
    
# for _ in range(10):
#     print(_)


# print("meow\n" * 3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n>0:
#         break

# for _ in range(n):
#     print("Hi")

# def main():
#     n = get_number()
#     meow(n)

# def get_number():
#     while True:
#         n = int(input("What's n? "))
#         if n>0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

#MCs

# mcs = ["Sunny", "Kael", "Astron", "Julian", "Damon"]

# for i in range(len(mcs)):
#     print(i+1, mcs[i])

#Dictionary

# mcs = {
#     "SS": "Sunny",
#     "YMPOV": "Samuel",
#     "HA": "Astron",
#     "Author POV": "Ren",
# }

# for mc in mcs:
#     # print(mc)
#     print(mc, mcs[mc], sep=": ")

# mcs = [
#     {"Name": "Sunny", "Title": "SS", "FML": "Nephis"},
#     {"Name": "Samuel", "Title": "YMPOV", "FML": "Juliana"},
#     {"Name": "Astron", "Title": "HA", "FML": "Irina"},
#     {"Name": "Kael", "Title": "Final Boss", "FML": None}
# ]

# for mc in mcs:
#     print(mc["Name"], mc["Title"], mc["FML"], sep=", ")



# COLUMNS
# def main():
#     print_column(6)

# def print_column(height):
#     print("#\n" * height, end="")
# main()

# ROWS
# def main():
#     print_row(4)

# # for i in range(4):
# #     print("#", end="")

# def print_row(width):
#     print("?" * width)

# main()

#SQUARE
# def main():
#     print_square(5)

# # def print_square(size):
# #     for i in range(size):
# #             print("#"*size)
# def print_square(size):
#     for i in range(size):
#         for j in range(i):
#             print("#", end="")
#         print()

# main()


# mysum = 0
# for i in range(5, 11, 2):
#     mysum += i
#     if mysum == 5:
#         break
#         mysum += 1
# print(mysum)


################ YOU TRY IT ################
# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)
# count = 0
# for i in range(5):
#     # i is 0,1,2,3,,
#     if i % 2 == 0: count+=1
# print(count)


#############################################

####################
## EXAMPLE: looping over characters
## These 3 code snippets do the same thing
####################

# s = "demo loops - fruit loops"
# for index in range(len(s)):
#     if s[index] == 'i' or s[index] == 'u':
#         print("There is an i or u")

######
      
# s = "demo loops - fruit loops"
# for char in s:
#     if char == 'i' or char == 'u':
#         print("There is an i or u")

#####

# s = "demo loops - fruit loops"
# for char in s:
#     if char in 'iu':
#         print("There is an i or u")


#
####################
## EXAMPLE:  robot cheerleaders
####################
# an_letters = "aefhilmnorsxAEFHILMNORSX"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# for w in word:
#     if w in an_letters:
#         #print(f'Give me an {c}: {c}') # with f-strings
#         print("Give me an " + w + ": " + w)
#     else:
#         #print(f'Give me a {c}: {c}') # with f-strings
#         print("Give me a " + w + ": " + w)
# print("What does that spell?")
# for i in range(times):
#     print(word, "!!!")


############### YOU TRY IT ####################
# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 

# your code here
# s = 'abcddea'
# letters = ""
# for c in s: 
#     if c not in letters:
#         letters += c
# print(len(letters))

##############################################




####################
## EXAMPLE: guessing perfect square roots
#################### 

# x = int(input("Enter an integer: "))
# guess = 0
# while guess**2 < x:
#     guess += 1
# if guess**2 == x:
#     print(f'Square root of {x} is {guess}')
# else:
#     print(f'{x} is not a perfect square')



####################
## EXAMPLE:  square root with negative flag
#################### 
# guess = 0
# neg_flag = False
# x = int(input("Enter a positive integer: "))
# if x < 0:
#     neg_flag = True
# while guess**2 < x:
#     guess = guess + 1
# if guess**2 == x:
#     print(f'Square root of {x} is {guess}')
# else:
#     print(f'{x} is not a perfect square')
#     if neg_flag:
#         print(f'Just checking... did you mean {-x} ?')



################ YOU TRY IT ##################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 

# your code here
# secret = 4
# seen = False
# for i in range(1,11):
#     if i == secret: seen = True
# print("Found" if seen else "Not Found")
        


################################################


#################### YOU TRY IT ###################
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, prints that it didn't find it. 

# your code here   
secret = 4

    
####################################################

####################
## EXAMPLE:  cube root
####################

# # finding a perfect cube of positive numbers
# cube = int(input("Enter an integer: "))
# for guess in range(cube+1):
#     if guess**3 == cube:
#         print(f'Cube root of {cube} is {guess}')



# finding perfect cube with negative numbers
# cube = int(input("Enter an integer: "))
# for guess in range(abs(cube)+1):
#     if guess**3 == abs(cube):
#         if cube < 0:
#             guess = -guess
#         print(f'Cube root of {str(cube)} is {str(guess)}')
        


# finding cube root with error message
# cube = int(input("Enter an integer: "))
# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess**3 != abs(cube):
#     print(f'{cube} is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
#     print(f'Cube root of {str(cube)} is {str(guess)}')

# for guess in range(abs(cube)+1):
#     if guess**3 >= abs(cube):
#         break
# if guess **3 != abs(cube):
#     print(f'{cube} is not a perfect cube')
# else:
#     if cube < 0:
#         guess = -guess
#     print(f'cube of {str(cube)} is {str(guess)}')

###################
# EXAMPLE: word problems
################### 
    
# this code is very slow for large numbers!
# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             total = (alyssa + ben + cindy == 10)
#             two_less = (ben == alyssa-2)
#             twice = (cindy == 2*alyssa)
#             if total and two_less and twice:
#                 print(f"Alyssa sold {alyssa} tickets")
#                 print(f"Ben sold {ben} tickets")
#                 print(f"Cindy sold {cindy} tickets")

# this code is better -- only one loop!
# for alyssa in range(1001):
#     ben = max(alyssa-20,0)
#     cindy = alyssa*2
#     if ben + cindy + alyssa == 1000:
#         print(f'Alyssa sold {alyssa} tickets')
#         print(f'Ben sold {ben} tickets')
#         print(f'Cindy sold {cindy} tickets')



###################
# EXAMPLE: floating point
################### 
# x = 0
# for i in range(10):
#     x += 0.1
# print(x == 1)
# print(x, 'is the same as?', 10*0.1)


###################
## EXAMPLE: Convert to binary
## use Python Tutor to go step-by-step: http://pythontutor.com/
###################

## Only positive numbers
# num = 1507
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# num = 1507
# result = ''
# if num ==0:
#     result = 0
# while num>0:
#     result = str(num%2) + result
#     num//=2
# print(result)

## Can handle negative numbers
# num = -15
# if num < 0:
#     is_neg = True
#     num = abs(num)
# else:
#     is_neg = False
# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2
# if is_neg:
#     result = '-' + result



#############
## EXAMPLE
# protip: use Python Tutor to go step-by-step: http://pythontutor.com/
#############

# x = float(input('Enter a decimal number between 0 and 1: '))

# p = 0
# while ((2**p)*x)%1 != 0:
#     print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
#     p += 1

# num = int(x*(2**p))

# result = ''
# if num == 0:
#     result = '0'
# while num > 0:
#     result = str(num%2) + result
#     num = num//2

# for i in range(p - len(result)):
#     result = '0' + result

# result = result[0:-p] + '.' + result[-p:]
# print(f'The binary representation of the decimal {str(x)} is {str(result)}')


#################
## EXAMPLE: successive addition
#################

# x = 0
# for i in range(10):
#     x += 0.125
# print(x == 1.25)

#######

#x = 0
#for i in range(10):
#    x += 0.1
#print(x == 1)
#
#print(x, '==', 10*0.1)


# s = "aaabbcdddda"

# max_run = 0
# curr_run = 0
# prev_char = ''
# for c in s:
#     if c == prev_char: 
#         curr_run+=1
#     else: 
#         curr_run = 1 
#         prev_char = c
#     max_run = max(max_run, curr_run)
# print(max_run)

####################################################
##################### AT HOME ######################
######################################################
# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, start to write your code with a smaller example, then test it on the above text.

# text1 = "abc"
# text2 = "cde"
# # your code here
# seen = ""
# count = 0
# for ch in text1:
#     if ch in text2 and ch not in seen: 
#         seen += ch
#         count += 1
    

####################################################
##################### END AT HOME ######################
######################################################



########################################################
############# ANSWERS TO AT HOME #######################
#######################################################
# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, write your code with a smaller example.

# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# count = 0
# already = ""
# for i in text1:
#     if i in text2 and i not in already:
#         count += 1
#         already += i
# print(count)

####################################################
##################### END ANSWERS TO AT HOME ######################
######################################################

######################################################
############# ANSWERS TO LECTURE #####################
######################################################
# You Try It 1:
# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)

# evens = 0
# for i in range(5):
#      if i % 2 == 0:
#          evens += 1
# print(evens)


# You Try It 2:
# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 

# your code here
# s='abca'
# seen = ""
# for char in s:
#     if char not in seen:
#         seen += char
# print(len(seen))



# You Try It 3:
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 

# your code here
# one way
# secret = 6
# for i in range(1, 11):
#     if i == secret:
#         print("found")

# another way
# secret = 6
# if secret in range(1, 11):
#     print("found")


# You Try It 4:
# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, prints that it didn't find it. 

# your code here
# one way
# secret = 7
# found_flag = False
# for i in range(1, 11):
#     if i == secret:
#         found_flag = True
#         print("found")
# if found_flag == False:
#     print("not found")


######################################################
############# END ANSWERS TO LECTURE #####################
######################################################


# m = 80

# for k in range(m+1):
#     if k**4 == m:
#         print(f"Fourth Root: {k}")
#         break
#     if k**4 > m:
#         print("No Exact Fourth Root")
#         break


# First Multiple Of a Target Above a Threshold

# step_val = 5
# limit = 50
# for i in range(1, limit+1):
#     if i > 20 and i % step_val == 0: 
#         print(f"First Match: {i}") 
#         break
#     else:
#         print("None Found")

#Binary Palindrome Check Using Bit Extraction

# n = 10
# bin_rep = ""
# if n == 0:
#     bin_rep = '0'
# while n>0:
#     bin_rep = str(n%2) + bin_rep
#     n//=2
# is_palindrome = bin_rep == bin_rep[::-1]
# print(f"Binary: {bin_rep}")
# print(f"Palindrome: {is_palindrome}")

# target_sum = 15
# found_num = False
# for i in range(1, 200):
#     num = i
#     total = 0
#     while num>0:
#         total += num%10
#         num//=10
#     if total == target_sum:
#         print(f"Smallest Number: {i}")
#         found_num = True
#         break
# if not found_num:
#     print("No match in range")

# a = [1,2,3]
# b = a
# b.append(4)
# print(a)
# print(b)

