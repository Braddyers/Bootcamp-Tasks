#Initialize variables with the sentence and an empty string for the final results
sentence = "I went outside today to look at the flowers in the garden."
final_sentence = ""

#Alternate character:

#Loop through each character in a sentence
for i in range(len(sentence)):

    if i % 2 == 0:

        #Make the character case uppercase if the index is even
        final_sentence += sentence[i].upper()
    
    else:
        #Make the character case lowercase if the index is odd      
        final_sentence += sentence[i].lower()

print(final_sentence)

#Alternate word:

#Split the sentence into a list of words
separate_words = sentence.split()

#Create a new list to store the modified words
modified_words = []

#Loop through each word in the sentence
for i in range(len(separate_words)):

    if i % 2 == 0:

        #Make the word uppercase
        modified_words.append(separate_words[i].upper())

    else:

        #Make the word lowercase
        modified_words.append(separate_words[i].lower())

#Join the listed words back together to make a single string again
final_sentence = " ".join(modified_words)

print(final_sentence)
