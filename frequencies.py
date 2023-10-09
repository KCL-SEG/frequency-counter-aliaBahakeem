"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
  

    frequency_dictonary = {}
    for item in items:
       item_str = str(item)

        if item_str in frequency_dictionary:
           frequency_dictonary[item_str] += 1
        else:
            frequency_dictonary[item_str] = 1

    return frequency_dictonary

# Test cases
result = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(result)  
    return frequencies
