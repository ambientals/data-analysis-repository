"""Function that checks if the string is identical to its reversed version or not. This code is based on SoloLearn lectures and has educational purposes; no copyright infringement is intended."""

def is_palindrome(s):
    if s == s[::-1]:
        print(f"{s} is palindrome")
    else:
        print(f"{s} is not palindrome")

is_palindrome("RADAR")