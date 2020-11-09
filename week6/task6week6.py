def find(letter, word, index):
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1


def count(letter, word):
    counter = 0
    index = 0
    while index < len(word):
        result = find(letter, word, index)
        if result == -1:
            return counter
        else:
            counter += 1
        index = result + 1
    return counter
    
print (count("a", "banana"))