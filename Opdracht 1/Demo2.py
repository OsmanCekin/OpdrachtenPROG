def wordcount(text):
    wordList = text.split()

    counters = {}
    for word in wordList:
        if word in counters:
            counters[word] += 1
        else:
            counters[word] = 1

    for word in counters:
        if counters[word] == 1:
            print('{:8} appears (counters) time')