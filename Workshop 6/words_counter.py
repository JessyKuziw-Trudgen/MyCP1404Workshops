count = 0
dictator = {}
words = input("Enter words:").split()
for word in words:
    if word in dictator:
        count = dictator[word] + 1
        dictator.update({word: count})
        count = 0
    else:
        count += 1
        dictator.update({word: count})
        count = 0
for word in sorted(dictator):
    print("{} {}".format(word, dictator[word]))
