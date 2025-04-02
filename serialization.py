import pickle

hackers = {"neut":1, "geohot":100,"neo":1000}

for key, value in hackers.items():
    print(key,value)


serialised = pickle.dumps(hackers)
print(serialised)

hacker_v2 = pickle.loads(serialised)
print(hacker_v2)

for key,valye in hacker_v2.items():
    print(key, value)

# with open('hackers.pickle','wb') as handle:
#     pickle.dump(hackers, handle)


with open("hackers.pickle","rb") as handle:
    hackers_v3 = pickle.load(handle)

print(hackers_v3)