def main():
    camel = input("camelCase: ").strip()
    snake = []
    for ch in camel:
        if ch.isupper():
            snake.append("_" + ch.lower())
        else: snake.append(ch)
    print("Snake: ", "".join(snake))

    kebab = []
    for ch in camel:
        if ch.isupper():
            kebab.append("-"+ch.lower())
        else:
            kebab.append(ch)
    print("Kebab: ", "".join(kebab))
main()