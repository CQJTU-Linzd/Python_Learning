srcFile = open("README.md")
destFile = open("README1.md", "w")


text = srcFile.read()
destFile.write(text)


srcFile.close()
destFile.close()