dict = {"hello" : 56, "at": 23, "test": 43, "this": 43}
for elem in sorted(dict.items(), reverse=True):
    print(elem[0], " ::", elem[1])
