"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    
    frequency_dictonary = {}

   
    for item in items:
       
        item_string = str(item)

       
        if item_string in frequency_dict:
            
            frequency_dictonary[item_string] += 1
        else:
            
            frequency_dictonary[item_string] = 1

    return frequency_dictionary


result = frequencies(['a', 'a', 'b', 'b', 'b', 'c'])
print(result) 
