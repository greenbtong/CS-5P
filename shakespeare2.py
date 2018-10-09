#Brian Tong
#btong1@ucsc.edu
#programming assignment 4
#user inputs a file name to be read. program counts the # of times the word appears. user types the words to see how many times the word appears.

import string

def main(file):
 dic = {}
 read = ""
#                              open file
 x = open(file,"r")
#                              read file
 read = x.read()
#                              no punctuation
 for c in string.punctuation:
  read = read.replace(c,"") 
#                              lower case and split
 read = read.lower().split()
#                              create dictinary with words as key words
#                              word count into dictinary(list)
 for k in read:
  if k in dic:
   dic[k] += 1
  if k not in dic:
   dic[k] = 1
#                              return the dictinary with word count
 return dic