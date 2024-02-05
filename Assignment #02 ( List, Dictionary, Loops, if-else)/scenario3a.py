word_list = ["apple", "banana", "apple", "orange", "banana", "grape", "apple"]
word_list2 = []

word_list.count("apple")
for word in word_list:
    if not(word in word_list2):
        print(f"Frequency of {word}: {word_list.count(word)}")
        word_list2.append(word)