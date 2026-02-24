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
    content = file.read().split() 

#strip the punctuation from each word before checking
clean_up = [word.strip(string.punctuation) for word in content]

#create variable to hold the misspelled words
misspelled = spell.unknown(clean_up)

#check if theres any mistakes
if not misspelled:
    print("No mistakes found.") 

#display the misspelled words, and display suggestion
else:
    print("Number of misspelled words: ",len(misspelled))
    for word in misspelled:
        print(f"'{word}' -> suggested: {spell.correction(word)}")