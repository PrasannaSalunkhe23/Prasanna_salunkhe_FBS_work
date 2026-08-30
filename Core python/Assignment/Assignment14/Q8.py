#8.Write a python program to find all the anagram and group them 
#together from a given list of strings.
string = ['eat' , 'tea', 'tan','ate','nat','bat']
groups = []
for word in string:
    found = False
    for group in groups:
        if len(word) == len(group[0]):
            is_anagram = True

            for ch in set(word):
                if word.count(ch) != group[0].count(ch):
                    is_anagram = False
                    break

            if is_anagram:
                groups.append(word)
                found = True
                break

    if not found:
        groups.append([word])

print("List:", string)

print("Grouped Anagrams:")

for group in groups:
    print(group)
