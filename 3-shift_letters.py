'''
Given a string, return a new string where every letter is shifted to its
right by one place in alphabetical order. The last letters z and Z should
be replaced with the first ones: a and A, respectively.
If the character isn't a letter, it should stay the same.

For example, given "abc123XYz!", the function should return "bcd123YZa!".
'''

def solution(s):
    # Define alphabets to check if a character is a letter
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Build the result string
    result = ""

    for char in s:
        # Check if it's a lowercase letter
        if char in lowercase:
            # Handle wrap-around for 'z'
            if char == 'z':
                result += 'a'
            else:
                # Shift to the next letter using ASCII values
                result += chr(ord(char) + 1)

        # Check if it's an uppercase letter
        elif char in uppercase:
            # Handle wrap-around for 'Z'
            if char == 'Z':
                result += 'A'
            else:
                # Shift to the next letter using ASCII values
                result += chr(ord(char) + 1)

        # Not a letter, keep it unchanged
        else:
            result += char

    return result


# Test the function
print(solution("abc123XYz!"))  # Should output "bcd123YZa!"
print(solution("Hello World")) # Should output "Ifmmp Xpsme"
print(solution("xyz"))         # Should output "yza"
print(solution("XYZ"))         # Should output "YZA"
print(solution("123!@#"))      # Should output "123!@#" (no change)
