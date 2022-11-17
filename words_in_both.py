#Author: Sophia Philips
#GitHub Username: sophiacphilips
#Date: 11/16/22
#This code takes two sentences and finds words that exist in both.

def words_in_both(sent_1, sent_2):
    """this takes two sentences and finds shared words among the sets, then lists them as a string"""
    sent_1=sent_1.lower().split(" ") #changing all letters to lower case and splitting sentences into strings
    sent_2=sent_2.lower().split(" ") #same as above comment for sent_2
    common_words = [] #creating empty list to fill with iterated words
    for word in sent_1:#iterating using word
        if word in sent_2 and word not in common_words: #if the word appears in both sentences it will list it, but it won't list it twice, if it appears more than once
            common_words.append(word) #adding string of common words to result
    return set(common_words)

print(words_in_both("She is a jack of all trades", "Jack was tallest of all"))