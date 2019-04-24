import _pickle as pickle

files = ['twitter_irony_2014_keep.pickle', 'twitter_irony_2015_keep.pickle','twitter_irony_2017_keep.pickle', 'twitter_irony_2018_keep.pickle']
combined = []
for file in files:
    f = open(file, mode="rb")
    d = pickle.load(f)
    combined.extend(d)
    f.close()
f = open('twitter_irony_all.pickle', mode="wb")
pickle.dump(combined, f)
f.close()
