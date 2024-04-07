import os

def metaData(filePath):
    if os.path.exists(filePath):
        fileMetaData = {
            "File Name" : os.path.basename(filePath),
            "File size(in bytes)" : os.path.getsize(filePath),
            "Creation Time" : os.path.getctime(filePath),
            "Last Modified Time" : os.path.getmtime(filePath)
        }
    else:
        return None
    return fileMetaData

file = open("new.txt", "x")
file.close()

data = metaData("new.txt")

for key, value in data.items():
    print(f"{key} and {value}")

