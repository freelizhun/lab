import fileiter


x = iter(fileiter.FileIterable(1))
for i in x:
    print i
