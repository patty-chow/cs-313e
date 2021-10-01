#  File: MagicSquare.py

#  Description: We are creating a matrix where all the rows, columns, and diagonals add up to the same number and outputs the sum of the numbers adjacent to a certain number if that number exists on the grid.

#  Student's Name: Patty Chow

#  Student's UT EID: mpc2468
 
#  Partner's Name: Natalie Castillo

#  Partner's UT EID: nac2732

#  Course Name: CS 313E

#  Unique Number: 52900

#  Date Created: 09/07/2021

#  Date Last Modified: 09/10/2021

import sys
#this reads the input and separates the grid length from the numbers that are going to be tested
def read_input ( ):
  n = 0
  num_list = []

  line = sys.stdin.readline()
  n = int(line)

  while (line != ''):
    line = sys.stdin.readline()
   
    if line == '':
      break
    num_list.append(int(line))


  return n, num_list


def make_matrix (n):
    #self-explanitory. this makes the matrix of teh specified length consisting of 0s.
    matrix = []
    for i in range(0, n):
        row = []
        for col in range(0, n):
            row.append(0)
        matrix.append(row)

    return matrix

       
# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

def make_square ( n ):
    #look up
    matrix = make_matrix(n)
    x = -1
    y = (n + 1)/2 - 1
    y = int(y)

    for num in range(1, n**2 + 1):
      if num == 1:
        matrix[x][y] = num
      elif x  > n - 1  and y > n - 1:
        matrix[n-2][n-1] = num
        x = n - 2
        y = n - 1
      elif x > n - 1:
        x = 0
        matrix[x][y] = num
      elif y > n - 1:
        y = 0
        matrix[x][y] = num
           
      elif matrix[x][y] != 0:
        x -= 2
        y -= 1
        matrix[x][y] = num
         
      else:
        matrix[x][y] = num
      x += 1
      y += 1
     
    return matrix



# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square ( magic_square ):
    #look up
  for row in range(len(magic_square)):
    for col in range(len(magic_square)):
      if col == len(magic_square)-1:
        print('{num:>3}'.format(num = magic_square[row][col]))
      else:
        print('{num:>3}'.format(num = magic_square[row][col]), end = '')
                 
       
 

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
def check_square ( magic_square ):
    #look up
    n = len(magic_square)
    add = n * (n**2 + 1) / 2
    while True:
      #checking if all rows equal "add"
      for line in magic_square:
        if sum(line) != add:
          return False
          break
      #checking if all columns equal "add"
      for i in range(n):
        count = 0
        for line in magic_square:
          count += line[i]
        if count != add:
          return False
          break
      #checking if main L-R diagonal equals "add"
      sumDiag1 = 0
      for j in range(n):
        sumDiag1 += magic_square[j][j]
      if sumDiag1 != add:
        return False
        break
      #checking if main R-L diagonal equals "add"
      sumDiag2 = 0
      for k in range(n):
        sumDiag2 += magic_square[k][n - k - 1]
      if sumDiag2 != add:
        return False
        break
      return True
      break

def in_square(square, n):
    #this functions checks if the number stated in the text function is in the grid. if it isn't, it returns a 0.
  count = 0
  x = 0
  y = 0
  for row in range(len(square)):
    for col in range(len(square)):
      if square[row][col] == n:
        count += 1
        x = row
        y = col
  return count, x, y
 
             

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square -
#         if n is outside the range return 0
def sum_adjacent_numbers (square, n):
    #look up!
    count,x,y = in_square(square, n)
    if count == 0:
        return 0
    else: 
        pain = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= len(square) or y + j >= len(square) or x + i < 0 or y + j < 0:
                    k = 0
                elif i==0 and j==0:
                    k = 0
                else:
                    k = square[x + i][y + j]
                pain += k
    
    return pain


 

def main():
  # read the input file from stdin
  n, num_list = read_input()
 

  # create the magic square
  square = make_square(n)
 

  # print the sum of the adjacent numbers
  for num in num_list:
      print(sum_adjacent_numbers (square, num))
      

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()