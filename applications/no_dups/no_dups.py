def no_dups(s):
    # Implement me.
    # initialize a dictionary to store cached values
    cache = {}
    # pass to a variable an empty string which will be filled with unique words
    unique_words = ""
    # split words in a list
    list_words = s.split(" ")
    # for each word in the list
    for word in list_words:
        # check if the word is in the cache
        if word in cache:
            # if so do nothing and go to next iteration
            continue
        else:
            # else the unique word is not empty
            if unique_words:
                # cache the word and save a count as value
                cache[word] = 1
                # chain new word to the unique words string
                unique_words = f"{unique_words} {word}" 
            else:
                # else cache the new word
                cache[word] = 1
                # set the unique string to be the the word
                unique_words = word
    # return the unique words string
    return unique_words


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))