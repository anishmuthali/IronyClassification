import _pickle as pickle

def remove_hashtag(tweet_dict):
    s = tweet_dict['text']
    for hashtag in tweet_dict['hashtags']:
        hash = "#" + hashtag['text']
        s = s.replace(hash, '')
    return s

filename = input("Enter filename: ")
f = open(filename + ".pickle", mode="rb")
d = pickle.load(f)
keep = []
discard = []
f.close()
i = 0
for item in d:
    curr_tweet = remove_hashtag(item)
    if "http" in curr_tweet:
        discard.append(curr_tweet)
        i+=1
        continue
    if "@" in curr_tweet:
        discard.append(curr_tweet)
        i+=1
        continue
    print(str(i) + "/" + str(len(d)))
    print(curr_tweet)
    action = input("Enter action: ")
    if action == "k":
        keep.append(curr_tweet)
    elif action == "d":
        discard.append(curr_tweet)
    elif action == "u":
        updated = input("Enter updated tweet: ")
        keep.append(updated)
    i+=1

keep_filename = filename + "_keep.pickle"
keep_file = open(keep_filename, mode="wb")
pickle.dump(keep, keep_file)
keep_file.close()

discard_filename = filename + "_discard.pickle"
discard_file = open(discard_filename, mode="wb")
pickle.dump(discard, discard_file)
discard_file.close()
