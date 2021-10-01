#  File: WordSearch.py
#  Description: Given a square grid of letter and a list of words this program attempts to find each word in said grid.
#  Student Name: Patty Chow
#  Student UT EID: mpc2468
#  Partner Name: Natalie Castillo
#  Partner UT EID: nac2732
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created: 09/02/2021
#  Date Last Modified: 09/03/2021

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search
def read_input ( ):
  grid = []
  words = []

  n = sys.stdin.readline()
  n = int(n)
  blank = sys.stdin.readline()

  for i in range(n):
    line = sys.stdin.readline()
    line = line.strip()
    wordList = []
    for j in line:
      if j != " ":
        wordList.append(j)
    grid.append(wordList)

  blank = sys.stdin.readline()
  k = sys.stdin.readline()
  k = int(k)

  for i in range(k):
    word = sys.stdin.readline()
    word = word.strip()
    words.append(word)

  return grid, words


# Inpput:2-D list that is the grid of letters and
#         a word to search
# Output: A tuple containing the cooridantes of the first letter in the word
#         only if the word is found horizontally left to right. Otherwise,
#         returns an empty tuple
def hL(grid, word):
  cord = tuple()
  x = 0
  for row in grid:
    my_str = ""
    x += 1
    for letter in row:
      my_str = my_str + letter

    if my_str.find(word) != -1:
      y = my_str.find(word) + 1
      cord = (x, y)
       
  return cord
 

# Inpput:2-D list that is the grid of letters and
#         a word to search
# Output: A tuple containing the cooridantes of the first letter in the word
#         only if the word is found horizontally right to left. Otherwise,
#         returns an empty tuple
def hR(grid, word):
  cord = tuple()
  x = 0
  for row in grid:
    my_str = ""
    x += 1
    for letter in row:
      my_str = letter + my_str

    if my_str.find(word) != -1:
      y = len(my_str) - my_str.find(word)
      cord = (x, y)
     
  return cord

# Inpput:2-D list that is the grid of letters and
#         a word to search
# Output: A tuple containing the cooridantes of the first letter in the word
#         only if the word is found vertically up and down. Otherwise,
#         returns an empty tuple

def upDown(grid, word):
  upStr = ""
  y =  0
  cord = tuple()
  for y in range(len(grid)):
    upStr = ""
    for row in grid:
      upStr = upStr + row[y]
     

    if upStr.find(word) != -1:
        x = upStr.find(word) + 1
        cord = (x, y + 1)
 
  return cord

def downUp(grid, word):
  downStr = ""
  y =  0
  cord = tuple()
  for y in range(len(grid)):
    downStr = ""
    for row in grid:
      downStr = row[y] + downStr
      #print(downStr)

    if downStr.find(word) != -1:
        x = len(grid) - downStr.find(word)
        cord = (x, y + 1)

  return cord


'''
# Inpput:2-D list that is the grid of letters and
#         a word to search
# Output: A tuple containing the cooridantes of the first letter in the word
#         only if the word is found vertically down and up. Otherwise,
#         returns an empty tuple
def downUp(grid, word):
  cord = tuple()
  downStr = ""
  y = len(grid[0]) - 1
  for row in grid:
    downStr = row[y] + downStr

  if downStr.find(word) != -1:
      x = len(downStr) - downStr.find(word)
      y += 1
      cord = (x, y)
     
  y -= 1
  return cord
'''

def diagTL(grid,word):
  #starts from the top left corner (s) and goes up, checked
  # ex. S, KI, ALN
  cord = tuple()
  for i in range(0, len(grid)):
    diagTLStr = ""
    x = i
    y = 0
    while (0 <= x <= len(grid) - 1):
      diagTLStr = diagTLStr + grid[x][y]
      x -= 1
      y += 1

    if diagTLStr.find(word) != -1:
      x = i - diagTLStr.find(word) + 1
      y = diagTLStr.find(word) + 1
      cord = (x,y)
      break

  return cord
 
def diagBL(grid,word):
  #starts to the right of the bottom left corner at L and
  #goes all the was to the bottom right corner T
  cord = tuple()
  for i in range(0, len(grid)):
    diagBLStr = ""
    x = len(grid) - 1
    y = i
    while (0 <= y <= len(grid) - 1):
      diagBLStr = diagBLStr + grid[x][y]
      x -= 1
      y += 1

    if diagBLStr.find(word) != -1:
      x = len(grid) - diagBLStr.find(word)
      y = i + 1 + diagBLStr.find(word)
      cord = (x,y)
      break
       
  return cord

def diagBR(grid,word):
  #Starts to the right of the top right corner at E, checked
  # and continues down all the way to T
  cord = tuple()
  for i in range(1, len(grid)):
    diagBRStr = ""
    x = i
    y = len(grid) -1
    while (len(grid) - 1 >= x >= 0):
      diagBRStr = diagBRStr + grid[x][y]
      x += 1
      y -= 1

    if diagBRStr.find(word) != -1:
      x = i + 1 + diagBRStr.find(word)
      y = len(grid) - diagBRStr.find(word)
      cord = (x,y)
      break
       
  return cord

def diagTR(grid,word):
  #Starts at the top right corner at I
  # and continues down all the way to T
  cord = tuple()
  for i in range(len(grid)):
    diagTRStr = ""
    x = i
    y = len(grid) -1
    while (len(grid) - 1 >= x >= 0 and len(grid) - 1 >= y >= 0):
      diagTRStr = diagTRStr + grid[x][y]
      x += 1
      y -= 1

    if diagTRStr.find(word) != -1:
      x = i + 1 + diagTRStr.find(word)
      y = len(grid) - diagTRStr.find(word)
      cord = (x,y)
      break
       
  return cord

def diagBLR(grid,word):
  #Starts to the right of the top right corner at E
  # and continues down all the way to T
  cord = tuple()
  for i in range(0, len(grid)):
    diagBLRStr = ""
    x = i
    y = 0
    while (len(grid) - 1 >= x >= 0):
      diagBLRStr = diagBLRStr + grid[x][y]
      x += 1
      y += 1

     
    if diagBLRStr.find(word) != -1:
      x = i + 1 + diagBLRStr.find(word)
      y = diagBLRStr.find(word) + 1
      cord = (x,y)
      break
       
  return cord


def diagTLR(grid,word):
  #starts from the top left corner (s) and goes up
  # ex. S, KI, ALN
  cord = tuple()
  for i in range(0, len(grid)):
    diagTLRStr = ""
    x = i
    y = 0
    while (len(grid) - 1 >= x >= 0):
      diagTLRStr = diagTLRStr + grid[x][y]
      x -= 1
      y += 1

    if diagTLRStr.find(word) != -1:
      x = i - diagTLRStr.find(word) + 1
      y = diagTLRStr.find(word)
      cord = (x,y)
      break

  return cord  

def diagTRUp(grid, word):
  #starts from the top right corner (s) and goes down
  #ex. 
  cord = tuple()
  for i in range(0, len(grid)):
    diagTRUstr = ""
    x = 0
    y = i
    while len(grid) - 1 >= y >= 0:
      diagTRUstr = diagTRUstr + grid[x][y]
      x += 1 
      y -= 1

    if diagTRUstr.find(word) != -1:
      x = diagTRUstr.find(word) + 1
      y = i - diagTRUstr.find(word) + 1
      cord = (x,y)
      break
  
  return cord

def diagBRUp(grid, word):
  #starts from the bottom right corner (T) and goes up diagonally and backwards, checked
  #ex. EW, EFM, KIER, etc.
  cord = tuple()
  for i in range(0, len(grid)-1):
    diagBRUstr = ""
    x = i
    y = len(grid) - 1 
    while len(grid) - 1 >= x >= 0:
      diagBRUstr = diagBRUstr + grid[x][y]
      x -= 1
      y -= 1

    if diagBRUstr.find(word) != -1:
      x = i + 1 - diagBRUstr.find(word)
      y = len(grid) - diagBRUstr.find(word)
      cord = (x, y)
      break

  return cord

def diagBRDown(grid, word):
  #starts from the bottom right corner (T) and goes left diagonally and backwards, checked
  #ex. E, LS, TNS, etc.
  cord = tuple()
  for i in range(0, len(grid)):
    diagBRUstr = ""
    x = len(grid) - 1 
    y = i
    while len(grid) - 1 >= y >= 0:
      diagBRUstr = diagBRUstr + grid[x][y]
      x -= 1
      y -= 1

    if diagBRUstr.find(word) != -1:
      x = len(grid) - diagBRUstr.find(word)
      y = i + 1 - diagBRUstr.find(word)
      cord = (x, y)
      break

  return cord
   
def diagTLUp(grid, word):
  #starts from the top left corner (S) and goes left diagonally and forwards, checked
  #ex. I, WE, MFE
  cord = tuple()
  for i in range(0, len(grid)):
    diagTLUstr = ""
    x = 0
    y = i
    while len(grid) - 1 >= y >= 0:
      diagTLUstr = diagTLUstr + grid[x][y]
      x += 1
      y += 1
  
    if diagTLUstr.find(word) != -1:
      x = diagTLUstr.find(word) + 1
      y = i + 1 + diagTLUstr.find(word)
      cord = (x, y)
      break
  
  return cord


    


   


   
# Input: a 2-D list representing the grid of letters and a single
#        string representing the word to search
# Output: returns a tuple (i, j) containing the row number and the
#         column number of the word that you are searching
#         or (0, 0) if the word does not exist in the grid

def find_word (grid, word):
  if hL(grid,word) != tuple():
    return hL(grid,word)
 
  elif hR(grid, word) != tuple():
    return hR(grid,word)
 
  elif upDown(grid, word) != tuple():
    return upDown(grid,word)

  elif downUp(grid, word) != tuple():
    return downUp(grid,word)

  elif diagTL(grid,word) != tuple():
    return diagTL(grid,word)

  elif diagBL(grid,word) != tuple():
    return diagBL(grid,word)

  elif diagBR(grid,word) != tuple():
    return diagBR(grid,word)

  elif diagTR(grid,word) != tuple():
    return diagTR(grid,word)
 
  elif diagBLR(grid,word) != tuple():
    return diagBLR(grid,word)
 
  elif diagTLR(grid,word) != tuple():
    return diagTLR(grid,word)

  elif diagTRUp(grid, word) != tuple():
    return diagTRUp(grid, word)

  elif diagBRUp(grid, word) != tuple():
    return diagBRUp(grid, word)

  elif diagBRDown(grid, word) != tuple():
    return diagBRDown(grid, word)
  
  elif diagTLUp(grid, word) != tuple():
    return diagTLUp(grid, word) 

  else:
    return (0,0)
 
 


def main():
  # read the input file from stdin
  word_grid, word_list = read_input()
 
  # find each word and print its location
  for word in word_list:
    location = find_word (word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":
  main()