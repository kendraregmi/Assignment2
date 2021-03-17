# 12. Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(word):
    reversed_word= word [::-1]
    if word==reversed_word:
        print("It is palindrome")
    else:
        print("not palindrome")
word= input('Enter the string')
is_palindrome(word)