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


