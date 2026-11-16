def main():
    # inp = input("Input: ").strip()
    # short = []
    # for ch in inp:
        
    #     if ch in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'o', 'i', 'u']:
    #         continue
    #     else:
    #         short.append(ch)
    # print("Output: ", "".join(short))

    # vowels = "aeiouAEIOU"
    # short = []
    # for char in inp:
    #     if char.isalpha() and char not in vowels:
    #         short.append(char)
    # print("Output: ", "".join(short))

    text = input("Input: ")
    vowels = "aeiouAEIOU"
    consonant = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels: 
            consonant +=1
    print(f"Consonants: {consonant}")


    
main()

        