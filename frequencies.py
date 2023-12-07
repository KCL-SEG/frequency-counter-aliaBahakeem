def frequencies(items):
    frequencies = {}
    for item in items:
        item_str = str(item)

        if item_str in frequencies:
            frequencies[item_str] += 1
        else:
            frequencies[item_str] = 1

    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
# This will output: { 'a': 2, 'b': 3, 'c': 1 }

print(frequencies([100, 'Hello', '100', '100', 100]))
# This will output: { '100': 4, 'Hello': 1 }
