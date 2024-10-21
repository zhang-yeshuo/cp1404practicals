"""
Word Occurrences
Estimate: 25 minutes
Actual:   35 minutes
"""

def count_words():
    text = input("Text: ")
    words = text.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    longest_word = max(word_count.keys(), key=len)
    max_length = len(longest_word)
    sorted_word_count = dict(sorted(word_count.items()))
    for word, count in sorted_word_count.items():
        print(f"{word:{max_length}} : {count}")


count_words()

