#Brian Tong
#btong1@ucsc.edu
#programming assignment 5
#the program prints out "the ants go marching"

#list with lyrics
list1 = ["to suck his thumb,", "to tie his shoe,", "to climb a tree,", "to shut the door,", "to take a dive,", "to pick up sticks,", "to look up to heaven,", "to shut the gate,", "to check the time,", "to say the end,"], ["And they all go marching down...\nIn the ground...\nTo get out...\nOf the rain.\nBoom! Boom! Boom!"]
list2 = ["one" , "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

#for loop to print out the lyrics
def main():
 for x in range(10):
  print("The ants go marching " + list2[x] + " by " + list2[x] + ", hurrah! Hurrah!") 
  print("The ants go marching " + list2[x] + " by " + list2[x] + ", hurrah! Hurrah!") 
  print("The ants go marching " + list2[x] + " by " + list2[x] + ",")
  print("The little one stops " + list1[0][x])
  print(list1[1][0]) 

main()
