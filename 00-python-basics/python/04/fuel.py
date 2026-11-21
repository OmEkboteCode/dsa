def main():
#     pct = fuel()
#     if pct <=1: print('E')
#     elif pct>=93: print('F')
#     else: print(f"{pct}%")

# def fuel():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             x,y = map(int, fraction.split("/"))
#             if x>y: raise ValueError('X>Y')
#             return round((x/y)*100)
#         except (ValueError, ZeroDivisionError):
#             pass
    # x, y = f.split("/")
    # if y == 0 or y>x:

    #     percentage = (int(x)/int(y))*100
    #     print(percentage)
    #     if percentage>= 93:
    #         print("F")
    #     elif percentage<=1:
    #         print("E")
    #     else:
    #         print(percentage)
    while True:
        try:
            x,y = int(input("X =")), int(input("Y ="))
            print(round(x/y, 2))
            print(f"{x/y:.2f}")
            break
        except ValueError: print('Enter Whole Integers Only')
        except ZeroDivisionError: print('Denominator cannot be zero')

    
main()