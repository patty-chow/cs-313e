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
        if rect1[1] < rect2 [1] < rect1[3]:
            y1 = rect2[1]
        else:
            y1 = rect1[1]
        if rect1[0] < rect2 [2] < rect1[2]:
            x2 = rect2[2]
        else:
            x2 = rect1[2]
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
    for i in range(len(bldg)):
        for col in range(len(bldg[0])):
            if bldg[i][col] == 0:
                uspace += 1 

    return uspace
    

# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    cspace = 0 
    for i in range(len(bldg)):
        for col in range(len(bldg[0])):
            if bldg[i][col] > 1:
                cspace += 1 

    return cspace

# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    cspace = 0 
    for y in range(rect[3]-rect[1]):
        for x in range(rect[2]-rect[0]):
            if y >= len(bldg):
                break
            elif x >= len(bldg[0]):
                break
            else:
                if bldg[y][x] == 1:
                    cspace += 1 

    return cspace

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    office = office_space(office[2],office[3])
    for cubicle in cubicles:
        rect = cubicle
        for y in range(rect[3]-rect[1]):
            for x in range(rect[2]-rect[0]):
                if y >= len(office):
                    break
                elif x >= len(office[0]):
                    break
                else:
                    office[y][x] += 1
            
    return office

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert area ((0,0,2,2)) == 4

  assert overlap((0,0,2,2),(3,3,5,5)) == (0,0,0,0)

  assert unallocated_space([[1, 2, 0], [0, 0, 0], [0, 1, 2]]) == 5

  assert contested_space([[2, 2, 1, 1, 1], [2, 1, 3, 0, 0], [2, 0, 2, 0, 2], [2, 2, 0, 0, 2], [2, 3, 2, 3, 2]]) == 15

  assert uncontested_space([[888], [888]], (0, 0, 1, 2)) == 0

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
  roffice = request_space(office,cubicles)

  # compute the total office space
  print("Total", area(office))

  # compute the total unallocated space
  print("Unallocated", unallocated_space(roffice))

  # compute the total contested space
  print("Contested", contested_space(roffice))

  # compute the uncontested space that each employee gets
  for key in employeeDic:
      print(key, uncontested_space(roffice,employeeDic[key]))

if __name__ == "__main__":
  main()