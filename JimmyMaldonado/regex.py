text = " hi hi hi http://google.com hi hi"

startIndex = text.find("http://")

substring = text[startIndex:len(text)]

endIndex = substring.find(" ")

print(substring[0:endIndex])


