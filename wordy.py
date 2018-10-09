#Brian Tong
#btong1@ucsc.edu
#programing assignment 3
#User inputs a sentense and program outputs the number count and average word length

import string

def main(): 
  pun = [".", "!", "?"]
  x = input("Please write a sentence. ")
  for i in range(3): 
   x = x.replace(pun[i], "")
  split = x.split()
  print("Your sentence has", len(split) , "words.")
  average = sum(len(y) for y in split)/len(split)
  print("The average word length of your sentence is approximately ", round(average, 2), end="")
  print(".")

main()
 
