import sys
import string
from spellchecker import SpellChecker

#get the number of argv  
args = sys.argv 

spell = SpellChecker()
#get the size of arguments, we want 2, this script file and the file we are spell checking 
number_of_args = len(args) 

#make sure we have 2 arguments 
if number_of_args != 2:
    raise Exception("Invalid number of arugments, 2 are needed")

#after checking for arguments we get the file name 
filename = args[1]  

#read the file 
with open(filename,"r") as file:
    content = file.read()

#strip the punctuation from each word before checking
clean_up = [word.strip(string.punctuation) for word in content.split()]

#split the content into sentences 
sentences = content.split('.') 

#check each sentence for a word that isnt uppercase at the start 
print("***CAPITALIZATION ERROR:")
for i, sentnce in enumerate(sentences):
    sentnce = sentnce.strip() 
    if len(sentnce) == 0:
        continue 
    first_word = sentnce.split()[0] 

    if not first_word[0].isupper():
        print(f"Sentence {i+1} does not start with an uppercase letter: '{first_word}'")

#create variable to hold the misspelled words
misspelled = spell.unknown(clean_up)

#check if theres any mistakes
print("\n***MISSPELLED WORDS AND SUGGESTION SPELLING:")

#check if theres any mistakes
if not misspelled:
    print("No mistakes found.") 

#display the misspelled words, and display suggestion
else:
    print("Number of misspelled words: ",len(misspelled))
    for word in misspelled:
        print(f"'{word}' -> suggested: {spell.correction(word)}")
