import pprint
bibleText = open('./bible.txt')
bibleLetters = bibleText.read()
count = {}

for character in bibleLetters:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)