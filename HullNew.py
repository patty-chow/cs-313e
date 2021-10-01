
#  File: Hull.py

#  Description:

#  Student Name: Patty Chow

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  '''def print_point(self):
      print('(' + str(self.x) + ',' + str(self.y) + ')')'''

  
  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# Input: p, q, r are Point objects
# Output: compute the determinant and return the value
def det (p, q, r):
  det = ((q.x * r.y) - (q.y * r.x)) - ((p.x * r.y) - (p.y * r.x)) + ((p.x * q.y) - (p.y * q.x))

  return det

# Input: sorted_points is a sorted list of Point objects
# Output: computes the convex hull of a sorted list of Point objects
#         convex hull is a list of Point objects starting at the
#         extreme left point and going clockwise in order
#         returns the convex hull
def convex_hull (sorted_points):  
  upper_hull = []
  upper_hull.append(sorted_points[0])
  upper_hull.append(sorted_points[1])

  for p in range(2, len(sorted_points)):
      upper_hull.append(sorted_points[p])
      while len(upper_hull) >= 3 and det(upper_hull[-3], upper_hull[-2], upper_hull[-1]) > 0:
        useless = upper_hull.pop(-2)


  lower_hull = []
  lower_hull.append(sorted_points[-1])
  lower_hull.append(sorted_points[-2])

  for p in range(len(sorted_points)-3, -1, -1):
    lower_hull.append(sorted_points[p])
    while len(lower_hull) >= 3 and det(lower_hull[-3], lower_hull[-2], lower_hull[-1]) > 0:
        useless = lower_hull.pop(-2)

  uselessFirst = lower_hull.pop(0)
  uselessLast = lower_hull.pop(-1)

  convex_hull = upper_hull + lower_hull

  return convex_hull



# Input: convex_poly is  a list of Point objects that define the
#        vertices of a convex polygon in order
# Output: computes and returns the area of a convex polygon
def area_poly (convex_poly):
  det = 0
  p = len(convex_poly)
  for i in range(len(convex_poly)):
      det += convex_poly[i].x * convex_poly[(i+1)%p].y
          
  for i in range(len(convex_poly)):
    det -= convex_poly[(i+1)%p].x * convex_poly[i].y

  return (1/2) * abs(det)

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
  # write your own test cases
  assert det(Point(3,2),Point(4,2),Point(5,-1)) == -3
  assert det(Point(3,2),Point(4,2),Point(5,2)) == 0
  assert det(Point(3,2),Point(4,2),Point(5,6)) == 4


  return "all test cases passed"

def main():
  # create an empty list of Point objects
  points_list = []

  # read number of points
  line = sys.stdin.readline()
  line = line.strip()
  num_points = int (line)

  # read data from standard input
  for i in range (num_points):
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    x = int (line[0])
    y = int (line[1])
    points_list.append (Point (x, y))

  # sort the list according to x-coordinates
  sorted_points = sorted (points_list)

  
  # print the sorted list of Point objects
  """
  for p in sorted_points:
    print (str(p))
    """


  # get the convex hull
  chull = convex_hull(sorted_points)
  # run your test cases
  # print your results to standard output

  # print the convex hull
  print('Convex Hull')
  for i in range(len(chull)):
    print(chull[i])
  print()
  # get and print the area of the convex hull
  print('Area of Convex Hull =', area_poly(chull))

if __name__ == "__main__":
  main()