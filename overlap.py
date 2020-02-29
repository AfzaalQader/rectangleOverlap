x1 = int(input('Please enter X coordinate of 1st rectangle:	'))
y1 = int(input('Please enter Y coordinate of 1st rectangle:	'))
width1 = int(input('Please enter width of 1st rectangle:	'))
height1 = int(input('Please enter height of 1st rectangle:	'))

x2 = int(input('Please enter X coordinate of 2nd rectangle:	'))
y2 = int(input('Please enter Y coordinate of 2nd rectangle:	'))
width2 = int(input('Please enter width of 2nd rectangle:	'))
height2 = int(input('Please enter height of 2nd rectangle:	'))

#Left uper corner coerdinnate A(pointX1,pointY1)
#Left bottom corner coordinate B(pointX1,pointY1 + height1)
#Right uper corner coordinate C(pointX1 + width1,pointY1)
#Right bottom corner coordinate D(pointX1 + width1, pointY1 + height1)
#Euqtions of first rectangle 
#top

def point_check(pointX,pointY):
	if((pointX >= x1 and pointX <= x1 + width1) and (pointY >= y1 and pointY <= y1 + height1)):
		return False
	else:
		return True

#Starting point recctangle 2 is (pointX2,pointY2)
#Left bottom corner coordinate (pointX2,pointY2 + height2)
#Right uper corner coordinate (pointX2 + width2,pointY2)
#Right bottom corner coordinate (pointX1 + width2,pointY2 + height2)

top_left = point_check(x2,y2)
print(top_left)
top_right = point_check(x2 + width2,y2)
print(top_right)
bottom_left = point_check(x2,y2 + height2)
print(bottom_left)
bottom_right = point_check(x2 + width2,y2 + height2)
print(bottom_right)
if(top_left == False or top_right == False or bottom_left == False or bottom_right == False):
	print('Both Rectangles are overlaped')
else:
	print('Both Rectangles are not overlaped')