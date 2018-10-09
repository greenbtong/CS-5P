#Brian Tong
#btong1@ucsc.edu	
#programming assignment 6
#user inputs a jumble word and program outputs un-jumble words

import string

# This python program takes a string as a parameter and returns a list of all possible permutations of the string. This python program uses recursion.
def permute(orig):

    #base case

    if orig == "":

        return([""])

    #recursive step

    else:

        first_char = orig[0]

        remainder = orig[1:]

        # small_list will be a list containing all permutations of the the string remainder

        small_list = permute(remainder)

        full_list = []

        for partial_word in small_list:

            #iterate over all possible positions in partial_word

            for i in range(len(partial_word)+1):

                new_word = partial_word[:i] + first_char + partial_word[i:]

                full_list = full_list + [new_word]

        return(full_list)


# READS FILE, GETS DICTIONARY LIST, COMPARES ANAGRAM AND DICTIONARY LIST, AND PRINTS POSSIBLE WORDS
def main(file):
 read = ""
 list = [""]
# READ FILE
 x = open(file,"r") 
 read = x.read()
# SPLIT TXT INTO A LIST
 read = read.lower().split()
# ASKS USER FOR JUMBLED WORD
 word = input("Please enter a jumbled word:  ")
# NO PUNCTUATION
 for c in string.punctuation:
  word = word.replace(c,"")
# LOWERCASE
 word = word.lower()
# UNSCRAMBLE
 word = permute(word)
# CHECK IF THE ANAGRAM LIST MATCH THE DICTIONARY LIST
 for k in read:
  for t in word:
   if k == t:
    list.append(k)
# REMOVE DUPILICATES
 list = duplicate(list)
# PRINT LIST
 if len(list) == 2:
  print("Your word is " + list[1] +".")
 elif len(list) > 2:
  print("Your words are:")
  for i in range(len(list)-1):
   print(list[i+1])
 else:
  print("Your word cannot be unjumbled.")

def duplicate(x):
 s = []
 for i in x:
  if i not in s:
   s.append(i)
 return s
    