import _pickle as pickle

f = open("goodreads_irony_keep.pickle", mode="rb")
d = pickle.load(f)
f.close()
edit_d = []
for item in d:
    edit_item = item[1:len(item)-2]
    edit_d.append(edit_item)
f = open("goodreads_irony_edited.pickle", mode="wb")
pickle.dump(edit_d,f)
f.close()
