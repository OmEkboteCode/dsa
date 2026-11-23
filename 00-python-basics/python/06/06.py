# Recall the approximation method code to find the square root
# x = 54321
# epsilon = 0.01
# num_guesses = 0
# guess = 0.0
# increment = 0.0001   # try it with 0.00001
# while abs(guess**2 - x) >= epsilon and guess**2 <= x:
#     # abs(guess**2 - x) >= epsilon finds a "good enough" answer
#     # guess**2 <= x ensures we stop looking when the guess becomes unreasonable
#     guess += increment
#     num_guesses += 1
# print(f'num_guesses = {num_guesses}')

# # this "if" is for the case when we stopped the loop due to an unreasonable guess
# if abs(guess**2 - x) >= epsilon:
#     print(f'Failed on square root of {x}')
#     print(f'Last guess was {guess}')
#     print(f'Last guess squared is {guess*guess}')
# # this "else" is for the case when we stopped the loop due to being within epsilon of x
# else:
#     print(f'{guess} is close to square root of {x}')


#####################
## EXAMPLE: fast square root using bisection search
# #####################

# x = 0.5  # try 0.5
# epsilon = 0.01
# num_guesses = 0
# low = 0.0
# high = x
# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     # uncomment to see each step's guess, high, and low 
#     #print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     num_guesses += 1
# print(f'num_guesses = {str(num_guesses)}')
# print(f'{str(guess)} is close to square root of {str(x)}')



############### YOU TRY IT ###################
# x = 0.5
# epsilon = 0.01
# # choose the low endpoint
# low = 0.0
# # choose the high endpopint
# high = x

# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#     print(f'low = {str(low)} high = {str(high)} guess = {str(guess)}')
#     if guess**2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')

#####################################################


#####################
## Code for square root with all x values
#####################
# x = 0.5
# epsilon = 0.01
# if x >=1:
#     low = 1.0
#     high = x
# else:
#     low = x
#     high = 1.0
# guess = (high + low)/2

# while abs(guess**2 - x) >= epsilon:
#    print(f'low = {str(low)} high {str(high)} guess = {str(guess)}')
#    if guess**2 < x:
#        low = guess
#    else:
#        high = guess
#    guess = (high + low)/2.0
# print(f'{str(guess)} is close to square root of {str(x)}')


################# YOU TRY IT #######################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube

# guess = (high+low)/2

# while abs(guess**3-cube) > epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# print(f"{str(guess)} is close to cube root of {str(cube)}")


# your code here


#####################################################


######## Cube root for all cubes ############
# cube = -27
# neg = False
# if cube < 0:
#     neg = True
# cube = abs(cube)
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
# if neg == True:
#     guess = -guess
# print(f'{guess} is close to the cube root of {cube}')


########################
## EXAMPLE: Newton-Raphson to find roots
######################
# epsilon = 0.01
# k = 24  # try 54321
# guess = k/2.0
# num_guesses = 0

# while abs(guess*guess - k) >= epsilon:
#     num_guesses += 1
#     guess = guess - (((guess**2) - k)/(2*guess))
# print(f'num_guesses = {str(num_guesses)}')
# print(f'Square root of {str(k)} is about {str(guess)}')


#################################################################
################# ANSWERS TO YOU TRY IT #######################
#################################################################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon

# cube = 27
# epsilon = 0.01
# low = 0
# high = cube
# guess = (high + low)/2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube :
#         low = guess
#     else:
#         high = guess
#     guess = (high + low)/2.0
#     numGuesses += 1
# print('numGuesses =', numGuesses)
# print(guess, 'is close to the cube root of', cube)

#################################################################
#################################################################
#################################################################


# Discrete Integer Guessing Via Bisection Search
# target = 742
# low = 0
# high = 1000
# count = 0

# while low <= high:
#     mid = (low + high)//2
#     if mid == target:
#         break
#     elif mid>target:
#         high = mid -1
#     else:
#         low = mid+1
# print(f"Count: {count}")
# print(f"answer: {mid}")
    

#Square Roots Bounds For Numbers Between 0 and 1

# x = 0.25
# epsilon = 0.0001
# low = 0.0
# high = max(1.0, x)
# num_guesses = 0
# guess = (low+high)/2.0

# while abs(guess**2-x) >= epsilon:
#     num_guesses +=1
#     if guess*2<x:
#         low = guess
#     else:
#         high = guess
#     guess = (low+high)/2.0

#First Occurance of Sorted Sequence

# nums = [2,4,4,4,7,9,10]
# target = 4
# num_guesses = 0
# low = 0
# high = len(nums)-1
# ans = -1

# while low<=high:
#     num_guesses +=1
#     mid = (low+high)//2
#     if nums[mid] == target:
#         ans = mid
#         high = mid - 1 # Keep Searching left half for an earlier occurrence
#     elif nums[mid]< target:
#         low = mid+1
#     else:
#         high = mid - 1
# print(f"First index: {ans}") #Outputs: 1

target = 20.0
epsilon = 0.0001

low = 0.0
high = target
guesses = 0

mid = (low+high)/2.0
while abs((mid**3+2*mid)-target)>= epsilon:
    guesses +=1
    if (mid**3+2*mid)<target:
        low = mid
    else:
        high = mid
    mid = (low+high)/2.0
