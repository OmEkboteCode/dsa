x = 18
guess = 0.0
increment = 0.001
epsilon = 0.01
num_guesses = 0

while abs(guess**2 -x) >= epsilon:
    guess += increment
    num_guesses +=1
print("Number of Guesses:", num_guesses)
print(guess, "is close to square root of", x)