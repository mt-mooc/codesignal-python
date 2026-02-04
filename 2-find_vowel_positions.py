"""
Write a function that takes a string s, iterates through it, and collects 
all 0-based positions of vowels in it to a list.

Note that you should not use any Python built-in string methods to solve 
this task.

For example, print(solution("Hello WORLD")) should output [1, 4, 7]. 
Here, 'e' is a vowel, and its position in the string "Hello" is 1. 
'o' is also a vowel, and its position is 4. 
The last vowel is O at position 7.
"""

def solution(s):
    # Define vowels as a string (both lowercase and uppercase)
    vowels = "aeiouAEIOU"

    # Create an empty list to store positions
    positions = []

    # Iterate through the string with index
    for i in range(len(s)):
        # Check if current character is in vowels
        if s[i] in vowels:
            # Add the position to our list
            positions.append(i)

    return positions


# Test the function
print(solution("Hello WORLD"))  # Should output [1, 4, 7]
print(solution("Python"))     # [4] - only 'o'
print(solution("AEIOU"))      # [0, 1, 2, 3, 4] - all vowels
print(solution("xyz"))        # [] - no vowels
