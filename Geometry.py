#  File: OfficeSpace.py

#  Description: This program takes an office space and employees desired cubicles in order to understand the unallocated and contested spaces.

#  Student Name: Patty Chow

#  Student UT EID: mpc2468 

#  Partner Name: Natalie Castillo

#  Partner UT EID: nac2732

#  Course Name: CS 313E

#  Unique Number: 52590

#  Date Created: 09/21/2021

#  Date Last Modified:

import sys

# Input: Takes the width and height of a rectangle
# Output: Returns a 2D list filled with zeros with the same 
#           width and height
def office_space(w,h):
    office = []
    for i in range(h):
        row = []
        for col in range(w):
            row.append(0)
        office.append(row)

    return office


# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    w = rect[2] - rect[0]
    h = rect[3] - rect[1]
    return w * h 

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect1, rect2):
    if (rect2[0] < rect1[0] < rect2[2] or rect2[0] < rect1[2] < rect2[2]) or (rect1[0] < rect2[0] < rect1[2] or rect1[0] < rect2[2] < rect1[2]):
        if rect1[0] < rect2 [0] < rect1[2]:
            x1 = rect2[0]
        else:
            x1 = rect1[0]
        if rect1[1] < rect2 [3] < rect1[3]:
            y1 = rect1[1]
        else:
            y1 = rect2[1]
        if rect1[0] < rect2 [0] < rect1[2]:
            x2 = rect1[2]
        else:
            x2 = rect2[2]
        if rect1[1] < rect2 [3] < rect1[3]:
            y2 = rect2[3]
        else:
            y2 = rect1[3]
        return(x1,y1,x2,y2)
    else:
        return (0,0,0,0)
    

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    uspace = 0 
    for i in range(len(bldg[0])):
        for col in range(len(bldg)):
            if bldg[i][col] == 0:
                uspace += 1 

    return uspace
    

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    cspace = 0 
    for i in range(len(bldg[0])):
        for col in range(len(bldg)):
            if bldg[i][col] > 1:
                cspace += 1 

    return cspace

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    pass

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    pass

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  pass
  assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  return "all test cases passed"

def main():
  # read the data
  line = line = sys.stdin.readline()
  line = line.strip()
  officecoords = line.split()
  w = int(officecoords[0])
  h = int(officecoords[1])

  office = (0,0,w,h)
 
  line = sys.stdin.readline()
  line = line.strip()
  n = int(line)
  
  employeeDic = {}
  for i in range(n):
      line = sys.stdin.readline()
      line = line.strip()
      data = line.split()
      employeeDic[data[0]] = (int(data[1]),int(data[2]),int(data[3]),int(data[4]))  

  
  cubicles = list(employeeDic.values())

  # run your test cases
  '''
  print (test_cases())
  '''

  # print the following results after computation

  # compute the total office space

  # compute the total unallocated space

  # compute the total contested space

  # compute the uncontested space that each employee gets

if __name__ == "__main__":
  main()