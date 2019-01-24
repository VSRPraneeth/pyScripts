fw = open("sample.txt", "w")
fw.write("Writing some shit in my txt file\n")
fw.write("I like soccer\n")
fw.close()

fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()
