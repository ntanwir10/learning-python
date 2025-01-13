# Find and display on the screen which character occupies the fifth position within the following word: "computer" in python

word = "computer"
print(word[4]) # 0 based index, so 4th position is 5th character

 #index of the first occurrence of the word "practice" in the following sentence

sentence = "In theory, theory and practice are the same. In practice, they are not."

print(sentence.index("practice")) # 44

#Take every third character starting from the ninth to the end of the sentence, and print the result.

"Never trust a computer you can't throw out a window" [8::3] # 'aomr tcm o o'

# Concatenate the text "Repetition" 15 times and display the result on the screen.

print("Repetition" * 15)    # RepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetitionRepetition

#display on the screen the length (in number of characters) of the word electroencephalographist.

print(len("electroencephalographist")) # 24


######TEXT-PARSER###

text  = input("Enter a text of your choice: ")

letters = []

text = text.lower()

letters.append(input("Enter the the first letter: ")).lower()
letters.append(input("Enter the the second letter: ")).lower()
letters.append(input("Enter the the thrid letter: ")).lower()

print("\n")

print("LETTER REPITITIONS")

letter_repetition1 = text.count(letters[0])
letter_repetition2 = text.count(letters[1])
letter_repetition3 = text.count(letters[2])

print(f"We have found the letter '{letters[0]}' repeated {letter_repetition1} times.")

print(f"We have found the letter '{letters[1]}' repeated {letter_repetition2} times.")

print(f"We have found the letter '{letters[2]}' repeated {letter_repetition3} times.")

print("\n")
print("NUMBER OF WORDS")

words = text.split()
print(f"We have found {len(words)} words in your text.")

first_letter = text[0]
last_letter = text[-1]
print(f"The initial letter is {first_letter}, the final letter is {last_letter}")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text = ' '.join(words)
print(f"If we order your text in reverse, we get: '{inverted_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")

is_python = 'python' in text
dic = {True: "was", False: "was not"}

print(f"The word 'Python' {dic[is_python]} found in the text.")
