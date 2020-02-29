pointX1 = int(input('Please enter X coordinate of 1st rectangle:	'))
pointY1 = int(input('Please enter Y coordinate of 1st rectangle:	'))
width1 = int(input('Please enter width of 1st rectangle:	'))
height1 = int(input('Please enter height of 1st rectangle:	'))

pointX2 = int(input('Please enter X coordinate of 2nd rectangle:	'))
pointY2 = int(input('Please enter Y coordinate of 2nd rectangle:	'))
width2 = int(input('Please enter width of 2nd rectangle:	'))
height2 = int(input('Please enter height of 2nd rectangle:	'))

#Left uper corner coerdinnate A(pointX1,pointY1)
#Left bottom corner coordinate B(pointX1,height1)
#Right uper corner coordinate C(width1,pointY1)
#Right bottom corner coordinate D(width1,height1)
#Euqtions of first rectangle 
#top

def point_check(pointX,pointY):
	"""This will check the point weather this point within a rectangle or not here PointY1,height1,PointX1 and width1 is constant"""
	eq1 = pointY - pointY1
	eq2 = pointY - height1
	eq3 = pointX - pointX1
	eq4 = pointX - width1
	if((eq1 <= 0 and eq2 >= 0) and (eq3 >= 0 and eq4 <= 0)):
		return False
	else:
		return True

#Starting point recctangle 2 is (pointX2,pointY2)
#Left bottom corner coordinate (pointX2,height2)
#Right uper corner coordinate (width2,pointY2)
#Right bottom corner coordinate (width2,height2)

top_left = point_check(pointX2,pointY2)
top_right = point_check(width2,pointY2)
bottom_left = point_check(pointX2,height2)
bottom_right = point_check(width2,height2)

if(top_left == True or top_right == True or bottom_left == True or bottom_right == True):
	print('Both Rectangle are overlaped')
else:
	print('Both Rectangle are not overlaped')