# find the largset word in a given string
#examples
#input: "fun&!! time"
# Output: time

def easy_longest_word(string):
    count = 0
    maximum = 0
    for char in string:
        if char.isalnum():
            count += 1
        else:
            maximum = max(maximum, count)
            count = 0
    maximum = max(maximum, count)
    return maximum

string = 'fun!@#$# times'
print(easy_longest_word(string))


def naive_longest_word(string):
    count = 0
    maximum = 0
    words = []
    word = []
    for char in string:
        if char.isalnum():
            count += 1
            word.append(char)
        else:
            if word not in words and word:
                words.append(''.join(word))
                print(words)
                print(word)
                word = []
            maximum = max(maximum, count)
            count = 0
    maximum = max(maximum, count)
    if word not in words and word:
        words.append("".join(word))
        print(words)
        print(word)
    for item in words:
        if len(item) == maximum:
            return item

print(naive_longest_word(string))