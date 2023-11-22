def find(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1


print(find("hello world", "helloworld"))
