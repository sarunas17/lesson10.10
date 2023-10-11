# write a program witch takes at least 5 minimum words (use only 1 input) separated by comma . 
# From those words , make a dictionary where the key is a letter and value is a number of the frequency the letter did appear in all those words. 
# Letters should be in alphabetical order.
# Everything should be done thorugh github workflow.

words = input("Enter at least 5 words separated by comma: ")
words_splited = words.replace(" ", "").split(",")
letters_dictionary = {}

for word in words_splited:
    for letter in word:
        if letter.isalpha():
            letters_dictionary[letter] = letters_dictionary.get(letter, 0) + 1

            # print(letters_dictionary)

sorted_letter_dictionary = dict(sorted(letters_dictionary.items()))
print(sorted_letter_dictionary)

