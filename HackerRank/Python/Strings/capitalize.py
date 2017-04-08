def capitalize(string):
    words = string.split(' ')
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    s = " ".join(words)
    return s

    #return (' '.join(word.capitalize() for word in string.split(' ')))