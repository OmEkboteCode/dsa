def main():
    plate = input("Plate: ").strip()
    print('Valid' if is_valid(plate) else 'Invalid')

def is_valid(plate):
    if  not 2<= len(plate) <=6 or not plate.isalnum() or not plate[:2].isalpha():
        return False
    saw_digit = False
    for ch in plate:
        if ch.isdigit():
            if not saw_digit and ch == '0':
                return False
            saw_digit = True
        elif saw_digit:
            return False
    return True

def is_valid1(u):
    if 4<=len(u)<=10 or not u[0].islower() or not u.isalnum:
        return False
    else:
        return True

main()