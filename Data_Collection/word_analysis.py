import _pickle as pickle
import re
import nltk

common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us", "is"]

f = open("goodreads_irony_edited.pickle", mode="rb")
quotes = pickle.load(f)
f.close()
interesting_words = {}
for quote in quotes:
    quote = quote.lower()
    word_list = re.sub("[^\w]", " ",  quote).split()
    for word in word_list:
        if word in common_words or len(word) < 3:
            pass
        else:
            if word not in interesting_words:
                interesting_words[word] = 1
            else:
                interesting_words[word] += 1
f = open("goodreads_interesting.pickle", mode="wb")
pickle.dump(interesting_words, f)
f.close()
