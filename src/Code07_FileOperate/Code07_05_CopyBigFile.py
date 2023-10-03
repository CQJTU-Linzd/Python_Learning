srcFile = open("README.md")
destFile = open("README1.md", "w")


while True:
    text = srcFile.readline()
    if not text:
        break
    destFile.write(text)


srcFile.close()
destFile.close()