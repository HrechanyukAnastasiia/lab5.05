def long_words(dictionary):
    long_words_list = []
    for word in dictionary:
        if len(word) >= 5:
            long_words_list.append(word)
    return long_words_list
dict1 = {'dog', 'cat', 'tee', 'phone', 'computer', 'turtle'}
print(long_words(dict1))
