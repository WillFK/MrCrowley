import os
ext = ['txt', 'json', 'xml']
keys = ['text', 'title', 'message']
occurrences = {key: 0 for key in keys}
print(occurrences)
for root, dir, files in os.walk("./assets"):
    for file in files:
        if file.endswith(tuple(ext)):
            print('reading file...'+file)
            content = open(root+'/'+file, 'r').read()
            for key in keys:
                count = content.count(key)
                if count > 0:
                    print('\r'+str(count)+' occurrences of '+key)
                    occurrences[key] = occurrences[key] + count
print(occurrences)
