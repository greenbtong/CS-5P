#Brian Tong
#btong1@ucsc.edu
#Programming assignment 2
#The user imputs a range of grades and the program outputs the average

def main():
  m = 0
  x = eval(input("How many grades will you be entering? "))
  while ((type(x) != type(3)) or (x <= 0)):
    print("You can't enter", x, "grades!", end="")
    x = eval(input("  How many grades will you be entering? "))
  for y in range(x):
    v = eval(input("Please enter a grade between 0 and 100: "))
    while v < 0 or v > 100:
      print("Your number is out of range!", end="")
      v = eval(input("  Please enter a grade between 0 and 100: "))
    m = m + v
  m = m / (x)
  if m >= 70:
    print("Your class did great!  The average was", m)
  else:
    print("Your class did poorly.  The average was", m)

main()