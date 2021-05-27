import math
#given values can be changed based upon polygon
polygon = [[1,1],[4,6],[7,0],[4,1],[0,0]]
#final list
sides = []
pt1 = 0
pt2 = 1
polygonSide = -1
#this value is based upon how many sides the polygon has
for i in polygon:
    polygonSide +=1

for i in polygon:
    #assigns the x and y values
    x1 = polygon[pt1][0]
    y1 = polygon[pt1][1]
    x2 = polygon[pt2][0]
    y2 = polygon[pt2][1]
    #adds to the pt values so that when running the loop again it will use the next index position for each value
    pt1 += 1
    pt2 += 1
    #makes it calculate the x2 and y2 at index 0 once it has passed the length of polygon, done in order to calculate the last side
    if pt2 > polygonSide:
        pt2 = 0
    sides.append(math.sqrt((x2-x1)**2 + (y2-y1)**2))

print ('The perimiter of your polygon is ' + (str(sum(sides))) + ' units.')

#TEST CASES BELOW
#Square
polygon = [[0,0],[0,3],[3,3],[3,0]]
sides = []
pt1 = 0
pt2 = 1
polygonSide = -1
for i in polygon:
    polygonSide +=1
for i in polygon:
    x1 = polygon[pt1][0]
    y1 = polygon[pt1][1]
    x2 = polygon[pt2][0]
    y2 = polygon[pt2][1]
    pt1 += 1
    pt2 += 1
    if pt2 > polygonSide:
        pt2 = 0
    sides.append(math.sqrt((x2-x1)**2 + (y2-y1)**2))
print ('The perimiter of the Square is ' + (str(sum(sides))) + ' units.')
#Rectangle
polygon = [[0,0],[6,0],[6,3],[0,3]]
sides = []
pt1 = 0
pt2 = 1
polygonSide = -1
for i in polygon:
    polygonSide +=1
for i in polygon:
    x1 = polygon[pt1][0]
    y1 = polygon[pt1][1]
    x2 = polygon[pt2][0]
    y2 = polygon[pt2][1]
    pt1 += 1
    pt2 += 1
    if pt2 > polygonSide:
        pt2 = 0
    sides.append(math.sqrt((x2-x1)**2 + (y2-y1)**2))
print ('The perimiter of the Rectangle is ' + (str(sum(sides))) + ' units.')
#Hexagon
polygon = [[0,0],[0,3],[3,6],[6,6],[6,3],[3,3]]
sides = []
pt1 = 0
pt2 = 1
polygonSide = -1
for i in polygon:
    polygonSide +=1
for i in polygon:
    x1 = polygon[pt1][0]
    y1 = polygon[pt1][1]
    x2 = polygon[pt2][0]
    y2 = polygon[pt2][1]
    pt1 += 1
    pt2 += 1
    if pt2 > polygonSide:
        pt2 = 0
    sides.append(math.sqrt((x2-x1)**2 + (y2-y1)**2))
print ('The perimiter of the Hexagon is ' + (str(sum(sides))) + ' units.')
