words = ["Hello World", "   fly me   to   the moon "]


def length_of_last_word(s):
    s = s.split(" ")
    s = reversed(s)
    for word in s:
        if word != "":
            return len(word)


for word in words:
    print(length_of_last_word(word))
