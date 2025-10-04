line=input("enter a line o text:")
words=line.split()
word_count={word:words.count(word)for word in set(words)}
print("word occurences",word_count)
