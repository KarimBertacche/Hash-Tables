import re

def word_count(s):
    # Implement me.
    # create instance of cache using dictionary 
    cache = {}
    # use replace method to substitute all symbols with empty spaces
    s = s.replace("\r", " ").replace("\t", " ").replace("\n", " ")
    # check if the string contains any of the given patterns using regex
    s = re.sub("[^0-9a-zA-Z' ]+", "", s)

    # store a list of all words
    list_words = s.split(" ")
    # iterate each word in the list
    for word in list_words:
        # if te word results in an empty string 
        if word == "":
            # then just move to next iteration
            continue
        # else lower case the all word
        word = word.lower()
        # check if the word is in the cache keys
        if word in cache.keys():
            # if so increase count by one
            cache[word] += 1
        else:
            # else set in cache with the initial count to one
            cache[word] = 1

    # return cached words with their respective counts
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))