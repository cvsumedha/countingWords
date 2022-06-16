introstring = input("Enter your introduction :  ")
print(introstring)
wordCount = 1
characterCount = 0
for i in introstring:
    characterCount = characterCount+1
    if (i == " "):
        wordCount = wordCount+1
print("Number of words in the string")
print(wordCount)
print("Number of character in the string")
print(characterCount)
