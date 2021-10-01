#  File: TestCipher.py

#  Description:

#  Student's Name:

#  Student's UT EID:
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys

def make_railroad (strng, key):
    railroad = []
    key = int(key)
    for i in range(key):
        row = []
        for col in range(len(strng) - 1):
            row.append('-')
        railroad.append(row)

    return railroad



#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):
    railroad = make_railroad(strng,key)
    x = 0
    y = 0
    move = 1
    key = int(key)
    for char in strng:
        railroad[x][y] = char
        y += 1
        x += move
        if y >= len(strng) - 1:
            break
        elif x > key - 1:
            move = -1
            x -= 2
        elif x < 0:
            move = 1
            x += 2
   
    final = ""
    for row in range(len(railroad)):
        count = 0
        for i in range(len(railroad[0])):
            if railroad[row][count] != '-':
                final = final + railroad[row][count]
            count += 1
       


    return  final

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):
    railroad = make_railroad(strng,key)
    x = 0
    y = 0
    move = 1
    key = int(key)
    for char in strng:
        railroad[x][y] = '*'
        y += 1
        x += move
        if y >= len(strng) - 1:
            break
        elif x > key - 1:
            move = -1
            x -= 2
        elif x < 0:
            move = 1
            x += 2
   

    strngCount = 0
    for row in range(len(railroad)):
        count = 0
        for i in range(len(railroad[0])):
            if railroad[row][count] == '*':
                railroad[row][count] = strng[strngCount]
                strngCount += 1
            count += 1

    final = ""
    x = 0
    y = 0
    move = 1
    for char in strng:
        if railroad[x][y] != '-':
            final = final + railroad[x][y]
        y += 1
        x += move
        if y >= len(strng) - 1:
            break
        elif x > key - 1:
            move = -1
            x -= 2
        elif x < 0:
            move = 1
            x += 2


    return  final

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  strng = strng.lower()
  new = ""
  for char in strng:
    if 97 <= ord(char) <= 122:
      new = new + char    
     
  return new # placeholder for the actual return statement

def long_phrase(strng,passphrase):
  
  count = 0
  miniCount = 0
  phrase = ""
  while count < len(strng)+1:
    if count + len(passphrase) <= len(strng):
        phrase = phrase + passphrase
        count += len(passphrase)
    else:
        phrase = phrase + passphrase[miniCount]
        miniCount += 1
        count += 1
       
       
  return phrase        

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character (p, s):
  LETTERS = 'abcdefghijklmnopqrstuvwxyz'
  keyNum = ord(s) - 97
  for i in range(0, keyNum):
    LETTERS = LETTERS + LETTERS[i]

  for j in range(0, keyNum):
    LETTERS = LETTERS[1:]
  keyNum2 = ord(p) - 97
  finalLetter = LETTERS[keyNum2]

  return finalLetter # placeholder for actual return statement
 
#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character (p, s):
  LETTERS = 'abcdefghijklmnopqrstuvwxyz'
  keyNum = ord(p) - 97
  while True:
    LETTERS = LETTERS + LETTERS[0]
    LETTERS = LETTERS[1:]
    if LETTERS[keyNum] == s:
      break

  return LETTERS[0]
 

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  long_phrase1 = long_phrase(strng, phrase)
  finalstrng = ""
  for i in range(len(strng)-1):
    finalstrng = finalstrng + encode_character(strng[i],long_phrase1[i])
   
 
  return finalstrng

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  long_phrase1 = long_phrase(strng, phrase)
  finalstrng = ""
  for i in range(len(strng)-1):
    finalstrng = finalstrng + decode_character(long_phrase1[i],strng[i])
  return finalstrng

def main():
  # read the plain text from stdin
  railstrng = sys.stdin.readline()

  # read the key from stdin
  key1 = sys.stdin.readline()

  # encrypt and print the encoded text using rail fence cipher
  print(rail_fence_encode(railstrng,key1))

  # read encoded text from stdin
  railstrng2 = sys.stdin.readline()
   
  # read the key from stdin
  key2 = sys.stdin.readline()

  # decrypt and print the plain text using rail fence cipher
  print(rail_fence_decode(railstrng2,key2))

  # read the plain text from stdin
  vstrng = sys.stdin.readline()

  # read the pass phrase from stdin
  passtrng = sys.stdin.readline()
  passtrng = passtrng.strip()
  print(long_phrase(vstrng,passtrng))


  # encrypt and print the encoded text using Vigenere cipher
  print(vigenere_encode ( vstrng, passtrng ))

  # read the encoded text from stdin
  vstrng2 = sys.stdin.readline()
 

  # read the pass phrase from stdin
  passtrng2 = sys.stdin.readline()

  # decrypt and print the plain text using Vigenere cipher
  print(vigenere_decode ( vstrng2, passtrng2 ))

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()