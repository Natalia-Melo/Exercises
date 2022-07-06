# Ask for user input
import random

#Import a random phrase from a .txt file
with open('phrases.txt') as file:
    lines = file.readlines()

# Select a random phrase from the template
n = random.randint(0,len(lines)-1)
print(n)
phrase = lines[n]

# Split sentences into a list of words
list_words = phrase.split()
print(list_words)

# Function to substitute strings
def substitution(string):
    if string == 'noun':
        return input('Please input a noun: ')
    if string == 'adverb':
        return input('Please input an adverb: ')
    if string == 'adjective':
        return input('please input an adjective: ')

    return string

#Iterate through the list
final_list = []
for i in list_words:
    final_list.append(substitution(i))

final_sentence = " ".join(final_list)
print(final_sentence)
