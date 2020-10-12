import math
Side1= float(input("Enter first side:"))
Side2= float(input("Enter second side:"))
Angle= float(input("Enter angle:"))

if ((Side1<=0)or(Side2<=0) or (Angle<=0)):
     print("Please enter correct data.\nThe sides of a triangle, the angle must be numbers >0\n")
elif Angle>=180:
     print("Please enter correct data.\nThe angle must be lower than 180")
else:
     Angle=Angle*math.pi/180;
     Side3= math.sqrt(Side1*Side1+Side2*Side2-2*Side1*Side2*math.cos(Angle))
     print (Side3)


