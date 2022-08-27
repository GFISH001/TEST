def palindrome_check():
    i = 0
    word = ""
    palin = ""
    letter = input("palindrome :")
    word += letter
    while i < len(word):
        palin += word[len(word)-1-i]
        i += 1
    print(word)
    print(palin)
palindrome_check()