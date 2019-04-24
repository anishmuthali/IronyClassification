import _pickle as pickle

filename = input("Enter filename: ")
f = open(filename + ".pickle", mode="rb")
d = pickle.load(f)
keep = []
discard = []
f.close()
i = 0

for item in d:
    print(str(i) + "/" + str(len(d)))
    print(item)
    action = input("Enter action: ")
    if action == "k":
        keep.append(item)
    elif action == "d":
        discard.append(item)
    i+=1

keep_filename = filename + "_keep.pickle"
keep_file = open(keep_filename, mode="wb")
pickle.dump(keep, keep_file)
keep_file.close()

discard_filename = filename + "_discard.pickle"
discard_file = open(discard_filename, mode="wb")
pickle.dump(discard, discard_file)
discard_file.close()
