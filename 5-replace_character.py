'''
Given a string input_string, return a new string in which all occurrences
of character c1 are replaced by c2.
Cannot use any built-in string methods or functions like replace().

For example: replace_character("hello, world", "o", "a") → "hella, warld"
'''

def replace_character(input_string, c1, c2):
    # Build the result string character by character
    result = ""

    for char in input_string:
        # If current character matches c1, use c2 instead
        if char == c1:
            result += c2
        else:
            result += char

    return result


# Test the function
print(replace_character("hello, world", "o", "a"))  # Should output "hella, warld"
print(replace_character("banana", "a", "o"))         # Should output "bonono"
print(replace_character("mississippi", "s", "z"))    # Should output "mizzizzippi"
print(replace_character("hello", "x", "y"))          # Should output "hello" (no match)
