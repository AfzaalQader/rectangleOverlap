pointX1 = int(input('Please enter X coordinate of 1st rectangle:	'))
pointY1 = int(input('Please enter Y coordinate of 1st rectangle:	'))
width1 = int(input('Please enter width of 1st rectangle:	'))
height1 = int(input('Please enter height of 1st rectangle:	'))
pointX2 = int(input('Please enter X coordinate of 2nd rectangle:	'))
pointY2 = int(input('Please enter Y coordinate of 2nd rectangle:	'))
width2 = int(input('Please enter width of 2nd rectangle:	'))
height2 = int(input('Please enter height of 2nd rectangle:	'))

#Starting point rectangle 1 is (pointX1,pointY1)
#Left bottom corner coordinate (0,height1)
#Right uper corner coordinate (width1,0)
#Right bottom corner coordinate (width1,height1)

#Starting point recctangle 2 is (pointX2,pointY2)
#Left bottom corner coordinate (0,height2)
#Right uper corner coordinate (width2,0)
#Right bottom corner coordinate (width2,height2)

if((pointX2 >= pointX1) and (pointX2 <= width1)):
	if((pointY2 >= pointY1) and (pointY2 <= height1)):
		print('Both rectangle are overlaped')
	else:
		print('Both rectangle are not overlaped')
else:
	print('Both rectangle are not overlaped')