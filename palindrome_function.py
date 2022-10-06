def multiply(x,y):
    result = x*y
    return result

def is_palindrome(string):
    backwards = string[::-1]
    return backwards == string
    return string[::-1].casefold() == string.casefold()

word = input("please enter word to check:")
if is_palindrome(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not  a palindrome".format(word))


def palindrom_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    #return string[::-1].casefold() == string.casefold()
    return is_palindrome(word)
word = input("enter your sentence to be checked")
if palindrom_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not  a palindrome".format(word))

