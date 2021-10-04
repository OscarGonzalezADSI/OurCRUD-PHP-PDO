
def createFile(fileName,content):
    file = open(fileName,"w")
    file.write(content)
    file.close()
