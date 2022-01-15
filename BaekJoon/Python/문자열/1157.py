
words = input().upper()
uniqueWords = list(set(words))

wordsCount = []
for i in uniqueWords:
    wordsCount.append(words.count(i))

if wordsCount.count(max(wordsCount)) > 1:
    print("?")
else:
    maxIndex = wordsCount.index(max(wordsCount))
    print(uniqueWords[maxIndex])